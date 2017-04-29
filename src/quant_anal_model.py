### Import and process data from Yahoo API

from pandas_datareader import data # pip install pandas_datareader
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np
from pdb import set_trace

def plot_sector_weighting(dc_sec, key, plot_dir):
    df_sec = pd.DataFrame(dc_sec[key], index=[key])
    srt_idx = np.argsort(df_sec[df_sec.index==key].values[0])[::-1]
    srted_labels = df_sec.columns[srt_idx]
    srted_values = df_sec[df_sec.index==key].values[0][srt_idx]
    n_bars = len(srted_labels)
    plt.figure()
    plt.title("Weighting of Sectors in S&P 500 as of %s" % df_sec.columns.tolist()[0])
    plt.bar(range(n_bars), srted_values, color="g", align="center")
    plt.xticks(range(n_bars), srted_labels, rotation=75)
    plt.ylabel("Sector Weighting")
    plt.xlim([-1, n_bars])
    plt.tight_layout()
    plt.savefig(plot_dir + "snp_sector_weighting.png")
    plt.close()

def plot_normalized(data_panel, plot_dir):
    # plot normalized price for comparison
    # Normalize data
    for item in data_panel.items:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(data_panel[item]['indexed'].index, data_panel[item]['indexed'], label=item+'-indexed')
        ax.plot(data_panel[item]['inv_value'].index, data_panel[item]['inv_value'], label=item+'-str_inv_value')
        ax.set_xlabel('Date')
        ax.set_ylabel('Indexed Value')
        ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                   ncol=3, mode="expand", borderaxespad=0.)
        plt.savefig(plot_dir + item + '_index_strat_plot.png')
        plt.close()

def plot_with_averages(data_panel, plot_dir):
    # create separate plot for each intrument with rolling averages
    for item in data_panel.items:
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.plot(data_panel[item]['inst_price'].index, data_panel[item]['inst_price'], label=item)
        ax.plot(data_panel[item]['short_avg'].index, data_panel[item]['short_avg'], label='20 days rolling')
        ax.plot(data_panel[item]['long_avg'].index, data_panel[item]['long_avg'], label='100 days rolling')
        ax.set_xlabel('Date')
        ax.set_ylabel('Adjusted closing price ($)')
        ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                   ncol=3, mode="expand", borderaxespad=0.)
        plt.savefig(plot_dir + item + '_plot.png')
        plt.close()

def create_data_panel(all_panel_data, use_price='Adj Close'):
    # Create dictionary with only time series of data and indexed series.
    # The index is the major axis of the DataFrame

    # The index is the major axis of the DataFrame
    df_price = all_panel_data.ix['Adj Close']

    # Getting all weekdays over Major_axis
    all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

    # Reindex df_price using all_weekdays as the new index
    df_price = df_price.reindex(all_weekdays)

    # Replace nan values with latest available price for each instrument. Nans are inserted for any days the market is not open; such as, holidays.
    df_price = df_price.fillna(method='ffill')
    # print df_price.head(), "\n"
    # print df_price.describe()
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
    # Get each instrument as a time series and create time series indexed based on earliest date in time series
    data_series = {}
    for ticker in tickers:
        data_series[ticker] = {'inst_price': df_price.ix[:, ticker]}
    for key in data_series.keys():
        data_series[key]['indexed'] = data_series[key]['inst_price']/data_series[key]['inst_price'].ix[data_series[key]['inst_price'].index.min()]

    return pd.Panel.from_dict(data_series)

if __name__ == '__main__':

    # Define file locations
    plot_dir = '../plots/'
    data_dir = '../data/'

    # Define the instruments to download. Initially; S&P 500, Dow, and Nasdaq
    tickers = ['^GSPC', '^DJI', '^IXIC']

    # Define data source
    data_source = 'yahoo'

    # Select dates for desired data
    start_date = '2000-01-01'
    end_date = dt.date.today().strftime("%Y-%m-%d")

    # Use pandas_datareader.data.DataReader to load the desired data.
    all_data_panel = data.DataReader(tickers, data_source, start_date, end_date)

    # print all_data_panel
    # print all_data_panel.items
    '''
    <class 'pandas.core.panel.Panel'>
    Dimensions: 6 (items) x 4342 (major_axis) x 3 (minor_axis)
    Items axis: Open to Adj Close
    Major_axis axis: 2000-01-03 00:00:00 to 2017-04-05 00:00:00
    Minor_axis axis: ^DJI to ^IXIC
    Index([u'Open', u'High', u'Low', u'Close', u'Volume', u'Adj Close'], dtype='object')
    '''

    # Create panel with only time series of data and indexed series.
    # The index is the major axis of the DataFrame
    data_panel = create_data_panel(all_data_panel, use_price='Adj Close')

    # Calculate the short(20) and long(100) day moving averages of the prices
    short_window = 20
    long_window = 100
    long_only = True

    for item in data_panel.items:
        data_panel[item]['short_avg'] =  data_panel[item]['inst_price'].rolling(window=short_window).mean()
        data_panel[item]['long_avg'] = data_panel[item]['inst_price'].rolling(window=long_window).mean()
        # Implement trade strategy of buying anytime instrument price and short rolling average are above long average. Specify long and short positions
        data_panel[item]['long_pos'] = \
            (data_panel[item]['inst_price'] > data_panel[item]['long_avg']) & \
            (data_panel[item]['short_avg'] > data_panel[item]['long_avg'])
        data_panel[item]['short_pos'] = \
            (data_panel[item]['inst_price'] < data_panel[item]['long_avg']) & \
            (data_panel[item]['short_avg'] < data_panel[item]['long_avg'])
        data_panel[item]['long_pct_gain'] = \
            data_panel[item]['indexed'].pct_change().fillna(0) * data_panel[item]['long_pos'].shift(1).fillna(False)
        data_panel[item]['short_pct_gain'] = \
            data_panel[item]['indexed'].pct_change().fillna(0) * data_panel[item]['short_pos'].shift(1).fillna(False) * -1.0
        data_panel[item]['total_pct_gain'] = data_panel[item]['long_pct_gain']
        if not long_only:
            data_panel[item]['total_pct_gain'] += data_panel[item]['short_pct_gain']
        data_panel[item]['inv_value'] = \
            (data_panel[item]['total_pct_gain'] + 1.0).cumprod()

    investment_value = 1.00

    data_panel['^GSPC'].to_csv(data_dir + 'S&P_trade_data.csv')

    # # plot each instrument with rolling averages
    # plot_with_averages(data_series, plot_dir):
    #
    # plot normalized instrument data
    plot_normalized(data_panel, plot_dir)

    # # plot S&P sector makekeup
    # dict_sec = {'12/31/2016': {'Consum. Disc.': 0.1203,
    #   'Consum. Stap.': 0.0937,
    #   'Energy': 0.0756, 'Financials': .1481, 'Health Care': .1363, 'Industrials': .1027, 'IT': .2077, 'Materials': .0284, 'Telecoms': .0266, 'Utilities': .0317, 'Real Estate': .0289}}
    #
    # sector_date = '12/31/2016'
    # plot_sector_weighting(dict_sec, sector_date, plot_dir)
