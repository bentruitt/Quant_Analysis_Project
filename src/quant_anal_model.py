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

def plot_normalized(data_panel, start_date, plot_dir, strat_name = '20_100'):
    # plot normalized price for comparison
    # Normalize data
    for item in data_panel.items:
        df_temp = data_panel[item].ix[start_date:,:].copy()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(df_temp.index, df_temp['indexed'], label=item+'-indexed')
        ax.plot(df_temp.index, df_temp[strat_name], label=item+'-' + strat_name + '_strat')
        ax.set_xlabel('Date')
        ax.set_ylabel('Indexed Value')
        ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                   ncol=3, mode="expand", borderaxespad=0.)
        plt.xticks(rotation=15)
        plt.savefig(plot_dir + item + '_' + strat_name + '_norm_plot.png')
        plt.close()
        df_temp = None

def plot_with_averages(data_panel, start_date, plot_dir, strat_name = None):
    # create separate plot for each intrument with rolling averages
    sa_name = 'sa_' + str(strat_name)
    la_name = 'la_' + str(strat_name)
    for item in data_panel.items:
        df_temp = data_panel[item].ix[start_date:,:].copy()
        fig = plt.figure()
        plt.title ("Instrument to " + str(strat_name) + " Comparison")
        ax = fig.add_subplot(1,1,1)
        ax.plot(df_temp.index, df_temp['inst_price'], label=item)
        if strat_name != None:
            init_inst_price = df_temp['inst_price'][df_temp.index.min()]
            ax.plot(df_temp.index, \
                init_inst_price * df_temp[strat_name], \
                label=str(strat_name))
            ax.plot(df_temp.index, df_temp[sa_name], label='short avg')
            ax.plot(df_temp.index, df_temp[la_name], label='long avg')
        ax.set_xlabel('Date')
        ax.set_ylabel('Adjusted closing price ($)')
        ax.legend(bbox_to_anchor=(0., .99, 1., 1.02),loc=3, \
            ncol=4, mode="expand", borderaxespad=0.)
        plt.xticks(rotation=15)
        plt.savefig(plot_dir + item + '_' + str(strat_name) + '_plot.png')
        plt.close()
        df_temp = None

def create_data_panel(all_panel_data, pull_start_date, start_date, end_date, use_price='Adj Close'):
    # Create dictionary with only time series of data and indexed series.
    # The index is the major axis of the DataFrame

    # The index is the major axis of the DataFrame
    df_price = all_panel_data.ix['Adj Close']

    # Getting all weekdays over Major_axis
    all_weekdays = pd.date_range(start=pull_start_date, end=end_date, freq='B')

    # Reindex df_price using all_weekdays as the new index
    df_price = df_price.reindex(all_weekdays)

    # Replace nan values with latest available price for each instrument. Nans are inserted for any days the market is not open; such as, holidays.
    df_price = df_price.fillna(method='ffill')
    df_price = df_price.fillna(method='bfill')
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
        trading_start_date = data_series[key]['inst_price'].ix[start_date:].index.min()
        data_series[key]['indexed'] = data_series[key]['inst_price']/data_series[key]['inst_price'].ix[trading_start_date]

    return pd.Panel.from_dict(data_series)

def add_performance_column(data_panel, start_date, short_window, long_window, allow_short):
    sa_name = 'sa_' + str(short_window) + '_' + str(long_window)
    la_name = 'la_' + str(short_window) + '_' + str(long_window)
    for item in data_panel.items:
        data_panel[item][sa_name] =  data_panel[item]['inst_price'].rolling(window=short_window).mean()
        data_panel[item][la_name] = data_panel[item]['inst_price'].rolling(window=long_window).mean()
        # Implement trade strategy of buying anytime instrument price and short rolling average are above long average. Specify long and short positions
        buy = False
        sell = False
        long_pos = []
        short_pos = []
        for i, idx in enumerate(data_panel[item].index):
            if (data_panel[item]['inst_price'][idx] > \
                data_panel[item][la_name][idx]) and \
                (data_panel[item][sa_name][idx] > \
                data_panel[item][la_name][idx]):
                buy = True
                sell = False
            elif (data_panel[item]['inst_price'][idx] < \
                data_panel[item][la_name][idx]) and \
                (data_panel[item][sa_name][idx] < \
                data_panel[item][la_name][idx]):
                buy = False
                sell = True
            long_pos.append(buy)
            short_pos.append(sell)
        long_pos_arr = np.array(long_pos)
        short_pos_arr = np.array(short_pos)
        long_pct_gain_arr = \
            data_panel[item]['indexed'].pct_change().fillna(0) * np.insert(long_pos_arr, 0,False)[:-1]
        short_pct_gain_arr = \
            data_panel[item]['indexed'].pct_change().fillna(0) * np.insert(short_pos_arr, 0,False)[:-1] * -1.0
        total_pct_gain_arr = long_pct_gain_arr
        if allow_short:
            total_pct_gain_arr += short_pct_gain_arr
        total_pct_gain_arr = total_pct_gain_arr * (total_pct_gain_arr.index>=start_date).astype(int)
        data_panel[item][str(short_window) + '_' + str(long_window)] = \
            (total_pct_gain_arr + 1.0).cumprod()

    return data_panel

if __name__ == '__main__':

    # Define file locations
    plot_dir = '../plots/'
    data_dir = '../data/'
    output_dir = '../output/'

    # Define the instruments to download. Initially; S&P 500, Dow, and Nasdaq
    tickers = ['^GSPC', '^DJI', '^IXIC']
    ticker_names = {'^GSPC':'S&P500', '^DJI':'DOW', '^IXIC':'Nasdaq'}

    # Define data source
    data_source = 'yahoo'

    # Select dates for desired data
    start_date = str((raw_input("As of what date would you like the data used to start?[yyyy-mm-dd]") or '2000-01-01'))
    end_today_y = bool((raw_input("Would you like to run the model on data through the latest available?[y/n]")!='y') or True)
    if end_today_y:
        end_date = dt.date.today().strftime("%Y-%m-%d")
    else:
        end_date = str(raw_input("What date would you like to run through?[yyyy-mm-dd]"))
    longest_avg = max(int(raw_input("What is the longest window you would like to iterate through in the comparison test?[days]") or 100),100)
    longest_avg = -1 * (-1*longest_avg//15) * 15
    pull_start_date = dt.datetime.strptime(start_date, '%Y-%m-%d') - pd.tseries.offsets.BDay(longest_avg)
    pull_start_date = pull_start_date.strftime('%Y-%m-%d')

    # Create text file for output
    run_time = str(dt.datetime.now().strftime('%Y-%m-%d_%H:%M'))
    print_file = open(output_dir + "roll_avg_strat_" + run_time + ".txt", "w")
    print_file.write("The data for this analysis was pulled from: %s\n" % (data_source))
    print_file.write("This analysis was run on the the tickers: %s\n" % (tickers))
    print_file.write("This analysis was run over the time range: %s to %s\n" % (start_date, end_date))

    # Use pandas_datareader.data.DataReader to load the desired data.
    all_data_panel = data.DataReader(tickers, data_source, pull_start_date, end_date)

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
    data_panel = create_data_panel(all_data_panel, pull_start_date, start_date, end_date, use_price='Adj Close')

    # Calculate the short(20) and long(100) day moving averages of the prices
    short_window = 20
    long_window = 100
    allow_short = True

    # add performance column to data frame for 20/100 strategy
    data_panel = add_performance_column(data_panel, start_date, short_window, long_window, allow_short)

    # add performance columns for short/long strategy across ranges
    strat_list = []
    for l_range in range(30, longest_avg + 15, 15):
        for s_range in range(10, l_range, 15):
            strat_list.append(str(s_range) + '_' + str(l_range))
            data_panel = add_performance_column(data_panel, start_date, s_range, l_range, True)

    investment_value = 1.00

    for item in data_panel.items:
        data_panel[item].to_csv(data_dir + str(ticker_names[item]) + '_trade_data.csv')
    data_panel.to_pickle(data_dir + 'data_panel.pkl')

    # print top n and plot top m trading strategies
    n_print = 5
    m_plot = 5
    for item in data_panel.items:
        srt_idx = np.argsort(data_panel[item][strat_list].iloc[-1,:])
        print_file.write("\n%s\n%s%s\n%s\n" % (item, '{:11}'.format('Short_Long'), '{:13}'.format('Ending_Value'), data_panel[item][strat_list].iloc[-1,:][srt_idx][::-1][:n_print]))
        for strat in data_panel[item][strat_list].iloc[-1,:][srt_idx][::-1][:m_plot].index.tolist():
            plot_normalized(data_panel, start_date, plot_dir, strat)

    # plot each instrument with rolling averages
    plot_with_averages(data_panel, start_date, plot_dir)
    plot_with_averages(data_panel, start_date, plot_dir, strat_name = '20_100')

    # plot normalized instrument data
    plot_normalized(data_panel, start_date, plot_dir, strat_name = '20_100')

    # print grid of short versus long performance
    max_l_range = longest_avg
    for item in data_panel.items:
        print_file.write("\n\nPeformance of All Short/Long Avg Strategies Applied to %s\n\n" % item)
        print_file.write("|     |")
        for s_range in range(10, max_l_range, 15):
            print_file.write("%s|" % '{:5}'.format(s_range))
        print_file.write("\n|:----| ")
        for s_range in range(10, max_l_range, 15):
            print_file.write(":---:|")
        for l_range in range(30, max_l_range + 15, 15):
            print_file.write("\n|%s(bold)|" % '{:5}'.format(l_range))
            for s_range in range(10, max_l_range, 15):
                try:
                    print_file.write("%s|" % '{:^5.3f}'.format(data_panel[item][str(s_range) + '_' + str(l_range)].iloc[-1]))
                except:
                    print_file.write(" N/A |")

    # # plot indexed instruments on same plot
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # for item in data_panel.items:
    #     ax.plot(data_panel[item].index, data_panel[item]['indexed'], label=item+'-indexed')
    # ax.set_xlabel('Date')
    # ax.set_ylabel('Indexed Value')
    # ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
    #            ncol=3, mode="expand", borderaxespad=0.)
    # plt.xticks(rotation=15)
    # plt.savefig(plot_dir + 'indexed_instruments_plot.png')
    # plt.close()

    # # # plot S&P sector makekeup
    # dict_sec = {'12/31/2016': {'Consum. Disc.': 0.1203,
    #   'Consum. Stap.': 0.0937,
    #   'Energy': 0.0756, 'Financials': .1481, 'Health Care': .1363, 'Industrials': .1027, 'IT': .2077, 'Materials': .0284, 'Telecoms': .0266, 'Utilities': .0317, 'Real Estate': .0289}}
    #
    # sector_date = '12/31/2016'
    # plot_sector_weighting(dict_sec, sector_date, plot_dir)

    print_file.close()
