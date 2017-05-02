# Quant_Analysis_Project  
Apply machine learning including neural networks through financial quantitative analysis to identify profitable investment strategies.  

## Utilize Yahoo API for Financial Data  
* http://www.learndatasci.com/python-finance-part-yahoo-finance-api-pandas-matplotlib/

## Deciding on Index  

<img align="right" src="/plots/saved_plots/indexed_instruments_plot.png" alt="Normalized Indexes" width=51% hspace=1% vspace=2%>   

<img align="right" src="/plots/saved_plots/^GSPC_None_plot.png" alt="S&P Plot w Averages" width=51% hspace=1% vspace=2%>  

Normalizing data based on first trading day of dataset. The plots are all very similar.

For this analysis it is important that we have a limited, yet diverse, set of securities to choose from. It is also important that we have a benchmark to compare the success of our trading strategies to.  

The weighting methodology of the indexes is of concern. The weighting applied within the S&P 500 is based on direct market capitalization, so large companies have a larger impact on movements in the S&P 500. The Dow is price weighted, so companies with higher security prices will have a larger impact on index movements. Price weighting is also more difficult to track over time, given activities such as share splits or buybacks. Also, the effect of dividends needs to be taken into account. The NASDAQ uses a modified market capitalization weighting. This modified weighting complicates our calculations when breaking the indexes down into individual securities for analysis.  

The S&P 500 is made up of 500 companies, which is a manageable number of companies to use for analysis. The NASDAQ only has 100 companies, which is manageable; however, financial companies are excluded which limits potential diversification in our constructed subset portfolio. The Dow only includes 30 blue chip companies, which limits our ability to construct a diverse portfolio from a subset of these companies.

The S&P 500 covers the below sectors allowing better cross sector diversification.

<img align="center" src="/plots/saved_plots/snp_sector_weighting.png" alt="S&P 500 Sector Weighting" width=90% hspace=1% vspace=2%>  

* http://siblisresearch.com/data/sp-500-sector-weightings/


Based on this initial analysis of three common indexes, the S&P 500 will be used as the benchmark and a portfolio will be constructed from a subset of the companies within the S&P 500.

## Analysis of a Technical Trading Strategy's Effectiveness

As a first step in developing a trading algorithm, the application of a technical trading strategy was implemented. This strategy may or may not be incorporated into the final portfolio construction and trading strategy, but it is none-the-less a good exercise. That being said, I am a bit torn about the use of technical trading strategies. I am a CFA Charterholder and trading based on technical indicators is against everything that the Efficient Market Hypothesis (EMH) teaches. It is typically assumed by fundamental analysts that developed markets are Strong-Form EMH; however, I feel this presents a conundrum.

**The strom-form EMH implies that the market is efficient, reflects all information (both public and private), future rates of return are independent of past rates of return, and security prices adjust nearly instantaneously to new information; therefore, no investor should be able to profit above the average investor even with new information.**

* The conundrum; why would you ever conduct fundamental analysis if all available information is already incorporated into a security price?
* To go beyond that; if all available information has already been incorporated into a security price, then why would you trade based on anything other than the security price (past and present)?

This is not my position, but I do feel it is important to acknowledge technical trading techniques (with a grain of salt).

<img align="right" src="/plots/saved_plots/^GSPC_None_plot.png" alt="S&P Plot w Averages" width=70% hspace=1% vspace=2%>  

In the plot of the S&P 500 index to the right, you can see plots of both a 20 day rolling average ("short avg") and 100 day rolling average ("long avg"). From looking at the plot, you can see that if you were to execute long/short trades anytime the short-term rolling average and the price of the S&P 500 move from below/above the long-term rolling average to above/below, you might be able to generate profit.

<img align="left" src="/plots/saved_plots/^GSPC_20_100_plot.png" alt="S&P Plot w 20/100" width=70% hspace=1% vspace=2%>

Let's try it! In the plot below, the green line represents the value of an investment that was made on the first trading day of 2000 in the same amount as the value of the S&P at the time. It does show some potential, but what happened in the periods 2010 through mid-2012 and early-2014 through early-2016? Well, maybe that proves technical trading strategies just don't work? Or, maybe the arbitrary use of 20 day and 100 day rolling averages doesn't work?

The use of 20 day and 100 day averages kind of makes sense. The 20 day average happens inside of a month and the 100 day average happens just outside of a quarter. By trading on these two averages, you potentially capture the effects of quarterly reports from companies being released by straddling earnings calls. This is one thought. There are however other milestones that could be straddled; though, it is difficult to say if this is a factor at all. If it is, it does make sense to look at rolling windows as long as just over one year and potentially as short as 5 days (inside of one week). Let's run this analysis and see what happens.

I have run the analysis and now have to decide whether, or not, to post this publicly. I may have just come up with a $1,000,000 strategy!!!

<img align="right" src="/plots/saved_plots/^IXIC_115_120_norm_plot.png" alt="S&P Plot w 115/120" width=70% hspace=30% vspace=2%>

The chart to the right represents an annual return of 9.09%. Or a 339% return since January 1st, 2000 --- $1.00 becomes $4.39. Not bad, but is this a million dollar idea? My guess is "no". It took me not much time to find rolling averages that would perform like this. I can't imagine others have not done the same.

**“There is no such thing as a new idea. It is impossible. We simply take a lot of old ideas and put them into a sort of mental kaleidoscope. We give them a turn and they make new and curious combinations. We keep on turning and making new combinations indefinitely; but they are the same old pieces of colored glass that have been in use through all the ages.” -- Mark Twain**

Why is this not a million dollar idea --- *over-fitting*. I many combinations of short and long rolling averages to find the one that would perform the best.

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

##### Peformance of All Short/Long Avg Strategies Applied to ^IXIC:

|**L\S**|   10|   25|   40|   55|   70|   85|  100|  115|  130|  145|  160|  175|  190|  205|  220|  235|  250|  265|  280|  295|  310|  325|  340|  355|  370|  385|
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **30**|0.624|0.462| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| **45**|1.334|1.063|1.849| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| **60**|1.591|0.498|1.533|1.270| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| **75**|1.963|0.932|1.366|0.716|2.010| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| **90**|1.275|0.831|1.136|1.700|1.630|1.029| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**105**|1.038|0.752|0.937|0.898|0.556|0.748|0.855| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**120**|0.558|0.761|1.913|1.276|0.632|1.071|1.753|4.421| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**135**|0.598|1.065|2.766|2.346|1.786|1.921|2.165|2.371|1.569| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**150**|0.656|1.065|2.035|2.254|1.324|1.654|1.869|1.105|1.220|0.880| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**165**|1.023|1.544|2.617|2.268|2.424|2.147|1.646|1.735|1.303|1.422|1.970| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**180**|1.280|1.889|2.304|1.893|2.479|2.037|1.523|0.855|2.076|3.449|2.687|2.078| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**195**|1.322|2.901|2.262|2.146|2.651|2.102|2.431|2.144|1.993|3.047|2.650|2.042|2.874| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**210**|1.472|2.567|1.641|1.478|1.917|2.091|3.068|3.543|3.701|2.782|2.525|2.350|1.994|1.813| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**225**|1.570|1.955|1.324|1.252|2.291|2.185|2.300|2.915|2.243|2.028|1.685|1.763|1.544|1.775|3.606| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**240**|1.645|1.433|0.916|1.144|2.039|2.036|1.743|1.953|1.741|1.939|1.465|1.323|1.787|2.778|1.737|1.523| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**255**|1.539|1.802|1.394|1.765|1.514|1.370|1.739|1.493|1.839|1.465|1.644|1.786|1.859|1.738|1.601|1.552|1.714| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**270**|2.174|1.529|1.605|1.607|1.323|1.040|1.775|2.181|1.658|1.952|2.139|1.863|1.417|1.680|2.734|2.628|2.344|3.056| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**285**|2.139|1.553|1.317|1.660|1.490|1.449|1.593|1.682|1.581|2.227|1.699|1.634|2.129|2.878|2.757|2.737|3.168|3.020|2.443| N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|**300**|1.675|1.311|1.213|1.628|1.210|1.159|1.412|1.413|1.268|1.431|1.474|1.681|1.720|2.305|2.353|2.972|2.683|2.521|2.558|2.504| N/A | N/A | N/A | N/A | N/A | N/A |
|**315**|1.223|0.895|1.206|1.423|1.005|0.974|0.986|1.155|1.455|1.450|1.354|1.447|1.689|2.117|2.533|2.037|2.408|2.212|1.947|1.798|1.620| N/A | N/A | N/A | N/A | N/A |
|**330**|1.262|0.886|1.480|0.992|0.964|0.898|1.105|0.949|1.188|1.129|1.205|1.335|2.203|2.414|2.197|2.173|1.912|1.639|1.385|1.358|1.376|1.224| N/A | N/A | N/A | N/A |
|**345**|1.564|1.503|1.865|1.058|1.331|1.284|0.902|1.078|1.355|1.310|1.682|2.757|2.624|2.994|2.815|2.203|2.005|1.500|1.430|1.468|1.842|1.663|1.525| N/A | N/A | N/A |
|**360**|1.703|1.712|1.867|1.076|1.449|2.012|1.288|1.479|1.774|1.669|2.638|2.977|2.907|3.552|2.644|2.233|1.620|1.568|1.628|2.164|1.781|1.666|1.809|1.556| N/A | N/A |
|**375**|1.675|1.708|2.035|1.506|1.975|1.713|1.530|2.033|2.344|2.375|3.494|3.222|3.231|2.946|2.491|1.761|1.582|1.543|1.777|1.879|1.832|1.784|2.119|2.305|2.224| N/A |

In addition, this was done for the NASDAQ, S&P500, and DOW. The NASDAQ results were picked, because they were the best. There is no guarantee that applying these rolling averages will outperform the underlying security into the future. If the behavior of the underlying security changes, it could go from profitable to generating losses. Periods of losses can be seen in the line representing the strategy. If the market were to go back to its behavior during one of these times, it could generate losses; and if long enough, it could wipe out any profits. Another characteristic worth noting is the increased volatility of the trading strategy versus the underlying security. This seems to represent the classic risk-reward trade off.

## What do we do next? Wait and see...
