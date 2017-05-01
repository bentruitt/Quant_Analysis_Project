# Quant_Analysis_Project  
Apply machine learning including neural networks through financial quantitative analysis to identify profitable investment strategies.  

## Utilize Yahoo API for Financial Data  
* http://www.learndatasci.com/python-finance-part-yahoo-finance-api-pandas-matplotlib/

## Deciding on Index  

<img style="float:right" src="/plots/saved_plots/indexed_instruments_plot.png" alt="NASDAQ Plot" width=51% hspace=1% vspace=2%>   

<img style="float:right" src="/plots/saved_plots/^GSPC_None_plot.png" alt="S&P Plot" width=51% hspace=1% vspace=2%>  

Normalizing data based on first trading day of dataset. The plots are all very similar.

For this analysis it is important that we have a limited, yet diverse, set of securities to choose from. It is also important that we have a benchmark to compare the success of our trading strategies to.  

The weighting methodology of the indexes is of concern. The weighting applied within the S&P 500 is based on direct market capitalization, so large companies have a larger impact on movements in the S&P 500. The Dow is price weighted, so companies with higher security prices will have a larger impact on index movements. Price weighting is also more difficult to track over time, given activities such as share splits or buybacks. Also, the effect of dividends needs to be taken into account. The NASDAQ uses a modified market capitalization weighting. This modified weighting complicates our calculations when breaking the indexes down into individual securities for analysis.  

The S&P 500 is made up of 500 companies, which is a manageable number of companies to use for analysis. The NASDAQ only has 100 companies, which is manageable; however, financial companies are excluded which limits potential diversification in our constructed subset portfolio. The Dow only includes 30 blue chip companies, which limits our ability to construct a diverse portfolio from a subset of these companies.

The S&P 500 covers the below sectors allowing better cross sector diversification.

<img style="float:center" src="/plots/saved_plots/snp_sector_weighting.png" alt="S&P 500 Sector Weighting" width=90% hspace=1% vspace=2%>  

* http://siblisresearch.com/data/sp-500-sector-weightings/


Based on this initial analysis of three common indexes, the S&P 500 will be used as the benchmark and a portfolio will be constructed from a subset of the companies within the S&P 500.

## Analysis of a Technical Trading Strategy's Effectiveness

As a first step in developing a trading algorithm, the application of a technical trading strategy was implemented. This strategy may or may not be incorporated into the final portfolio construction and trading strategy, but it is none-the-less a good exercise. That being said, I am a bit torn about the use of technical trading strategies. I am a CFA Charterholder and trading based on technical indicators is against everything that the Efficient Market Hypothesis (EMH) teaches. It is typically assumed by fundamental analysts that developed markets are Strong-Form EMH; however, I feel this presents a conundrum.

**The strom-form EMH implies that the market is efficient, reflects all information (both public and private), future rates of return are independent of past rates of return, and security prices adjust nearly instantaneously to new information; therefore, no investor should be able to profit above the average investor even with new information.**

* The conundrum; why would you ever conduct fundamental analysis if all available information is already incorporated into a security price?
* To go beyond that; if all available information has already been incorporated into a security price, then why would you trade based on anything other than the security price (past and present)?

This is not my position, but I do feel it is important to acknowledge technical trading techniques (with a grain of salt).

<img style="float:right" src="/plots/saved_plots/^GSPC_None_plot.png" alt="S&P Plot" width=70% hspace=1% vspace=2%>  

In the plot of the S&P 500 index to the right, you can see plots of both a 20 day rolling average ("short avg") and 100 day rolling average ("long avg"). From looking at the plot, you can see that if you were to execute long/short trades anytime the short-term rolling average and the price of the S&P 500 move from below/above the long-term rolling average to above/below, you might be able to generate profit.

<img style="float:left" src="/plots/saved_plots/^GSPC_20_100_plot.png" alt="S&P Plot" width=70% hspace=1% vspace=2%>

Let's try it! In the plot below, the green line represents the value of an investment that was made on the first trading day of 2000 in the same amount as the value of the S&P at the time. It does show some potential, but what happened in the periods 2010 through mid-2012 and early-2014 through early-2016? Well, maybe that proves technical trading strategies just don't work? Or, maybe the arbitrary use of 20 day and 100 day rolling averages doesn't work?

The use of 20 day and 100 day averages kind of makes sense. The 20 day average happens inside of a month and the 100 day average happens just outside of a quarter. By trading on these two averages, you potentially capture the effects of quarterly reports from companies being released by straddling earnings calls. This is one thought. There are however other milestones that could be straddled; though, it is difficult to say if this is a factor at all. If it is, it does make sense to look at rolling windows as long as just over one year and potentially as short as 5 days (inside of one week). Let's run this analysis and see what happens.

I have run the analysis and now have to decide whether, or not, to post this publicly. I may have just come up with a $1,000,000 strategy!!!

<img style="float:right" src="/plots/saved_plots/^IXIC_115_120_norm_plot.png" alt="S&P Plot" width=70% hspace=1% vspace=2%>

The chart to the right represents an annual return of 9.09%. Or a 339% return since January 1st, 2000 --- $1.00 becomes $4.39. Not bad, but is this a million dollar idea? My guess is "no". It took me not much time to find rolling averages that would perform like this. I can't imagine others have not done the same.

**“There is no such thing as a new idea. It is impossible. We simply take a lot of old ideas and put them into a sort of mental kaleidoscope. We give them a turn and they make new and curious combinations. We keep on turning and making new combinations indefinitely; but they are the same old pieces of colored glass that have been in use through all the ages.” -- Mark Twain**

Why is this not a million dollar idea --- *over-fitting*. I tested pretty much every combination of short and long rolling averages to find the one that would perform the best. In addition, I did this for the NASDAQ, S&P500, and DOW. I picked the NASDAQ results, because they were the best. There is no guarantee that applying these rolling averages will outperform the underlying security into the future. If the behavior of the underlying security changes, it could go from profitable to generating losses. You can, in fact, see periods of losses in the line representing the strategy. If the market where to go back to its behavior during one of these times, it could generate losses; and if long enough, it could wipe out any profits.

## What do we do next? Wait and see...
