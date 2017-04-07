### Import and process data from Yahoo API

from pandas_datareader import data # pip install pandas_datareader
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

# Define the instruments to download. Initially; S&P 500, Dow, and Nasdaq
tickers = ['^GSPC', '^DJI', '^IXIC']

# Define data source
data_source = 'yahoo'

# Select dates for desired data
start_date = '2000-01-01'
end_date = dt.date.today().strftime("%Y-%m-%d")

# Use pandas_datareader.data.DataReader to load the desired data.
panel_data = data.DataReader(tickers, data_source, start_date, end_date)

# print panel_data
# print panel_data.items
'''
<class 'pandas.core.panel.Panel'>
Dimensions: 6 (items) x 4342 (major_axis) x 3 (minor_axis)
Items axis: Open to Adj Close
Major_axis axis: 2000-01-03 00:00:00 to 2017-04-05 00:00:00
Minor_axis axis: ^DJI to ^IXIC
Index([u'Open', u'High', u'Low', u'Close', u'Volume', u'Adj Close'], dtype='object')
'''

# Create Pandas DataFrame with only adjusted closing prices.
# The index is the major axis of the DataFrame
adj_close = panel_data.ix['Adj Close']

# Getting all weekdays over Major_axis
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# Reindex adj_close using all_weekdays as the new index
adj_close = adj_close.reindex(all_weekdays)

# Replace nan values with latest available price for each instrument. Nans are inserted for any days the market is not open; such as, holidays.
adj_close = adj_close.fillna(method='ffill')
# print adj_close.head(), "\n"
# print adj_close.describe()
'''              ^DJI        ^GSPC        ^IXIC
2000-01-03  11357.509766  1455.219971  4131.149902
2000-01-04  10997.929688  1399.420044  3901.689941
2000-01-05  11122.650391  1402.109985  3877.540039
2000-01-06  11253.259766  1403.449951  3727.129883
2000-01-07  11522.559570  1441.469971  3882.620117

            ^DJI        ^GSPC        ^IXIC
count   4504.000000  4504.000000  4504.000000
mean   12339.254736  1390.437817  2854.799351
std     3087.472396   377.086953  1160.505333
min     6547.049805   676.530029  1114.109985
25%    10281.530029  1128.292481  2030.567504
50%    11210.409668  1300.740051  2450.354980
75%    13786.920166  1520.439972  3627.300110
max    21115.550781  2395.959961  5914.339844
'''

# Get each instrument as a time series
data_series = {}
data_series['dow'] = {'idx': adj_close.ix[:, '^DJI']}
data_series['snp'] = {'idx': adj_close.ix[:, '^GSPC']}
data_series['nasdaq'] = {'idx': adj_close.ix[:, '^IXIC']}

# Calculate the 20 and 100 days moving averages of the closing prices
short_window = 20
long_window = 100
for key in data_series.keys():
    data_series[key]['short'] = data_series[key]['idx'].rolling(window=short_window).mean()
    data_series[key]['long'] = data_series[key]['idx'].rolling(window=long_window).mean()
    data_series[key]['indexed'] = data_series[key]['idx']/data_series[key]['idx'].ix[data_series[key]['idx'].index.min()]
# plot each instrument with rolling averages
plot_dir = '../plots/'
for key in data_series.keys():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(data_series[key]['idx'].index, data_series[key]['idx'], label=key)
    ax.plot(data_series[key]['short'].index, data_series[key]['short'], label='20 days rolling')
    ax.plot(data_series[key]['long'].index, data_series[key]['long'], label='100 days rolling')
    ax.set_xlabel('Date')
    ax.set_ylabel('Adjusted closing price ($)')
    ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=3, mode="expand", borderaxespad=0.)
    plt.savefig(plot_dir + key + '_plot.png')
    plt.close()

# plot normalized index for comparison
# Normalize data
fig = plt.figure()
ax = fig.add_subplot(111)
for key in data_series.keys():
    ax.plot(data_series[key]['indexed'].index, data_series[key]['indexed'], label=key)
ax.set_xlabel('Date')
ax.set_ylabel('Indexed closing price')
ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)
plt.savefig(plot_dir + 'index_comp_plot.png')
plt.close()
