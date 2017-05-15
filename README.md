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

The chart to the right represents an annual return of 9.09%. Or a 339% return since January 1st, 2000 --- $1.00 becomes $4.39. The top five performing long average / short average strategies and how they performed over the holding period in comparison to the index are below:

|Short_Long |Ending_Value |
|:---|---:|
|Nasdaq|1.48172545785|
|115_120|4.2331156574|
|130_210|4.04766128707|
|115_210|3.76740325499|
|115_225|3.46787428825|
|145_180|3.44359936136|

 Not bad, but is this a million dollar idea? My guess is "no". It took me not much time to find rolling averages that would perform like this. I can't imagine others have not done the same.

**“There is no such thing as a new idea. It is impossible. We simply take a lot of old ideas and put them into a sort of mental kaleidoscope. We give them a turn and they make new and curious combinations. We keep on turning and making new combinations indefinitely; but they are the same old pieces of colored glass that have been in use through all the ages.” -- Mark Twain**

Why is this not a million dollar idea --- *over-fitting*. I tested many combinations of short and long rolling averages to find the one that would perform the best. I found the one that best fit the data to maximize return. If you run this same analysis over a different time period, you arrive at significantly different outcomes.

##### Peformance of All Short/Long Avg Strategies Applied to ^IXIC:

|**L\S**|   10|   25|   40|   55|   70|   85|  100|  115|  130|  145|  160|  175|  190|  205|  220|  235|  250|  265|  280|  295|  310|  325|  340|  355|  370|  385|
|:----| :---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|   30(bold)|0.677|0.501| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|   45(bold)|1.619|1.290|2.244| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|   60(bold)|1.950|0.611|1.879|1.557| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|   75(bold)|2.365|0.853|1.302|0.599|1.809| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|   90(bold)|1.135|0.705|1.009|1.514|1.274|0.971| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  105(bold)|1.030|0.781|1.035|0.912|0.440|0.709|0.818| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  120(bold)|0.372|0.669|1.365|0.904|0.463|0.971|1.670|4.233| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  135(bold)|0.479|0.900|2.141|1.446|1.533|1.867|2.086|2.400|1.588| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  150(bold)|0.428|0.946|1.652|1.512|1.246|1.640|2.020|1.177|1.141|0.837| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  165(bold)|0.600|1.186|1.786|2.035|2.225|1.985|1.626|1.457|1.214|1.420|1.971| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  180(bold)|0.557|1.028|1.412|1.628|2.245|1.981|1.481|0.788|1.993|3.444|2.597|2.000| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  195(bold)|0.887|2.314|1.266|2.096|2.589|2.053|2.289|2.114|2.142|3.223|2.655|1.777|3.112| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  210(bold)|1.011|1.778|1.242|1.493|1.936|2.112|3.124|3.767|4.048|2.831|2.342|1.852|1.544|1.526| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  225(bold)|1.173|1.597|1.538|1.471|2.048|2.310|2.737|3.468|2.669|2.233|1.605|1.523|1.452|1.632|3.293| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  240(bold)|1.465|1.714|1.103|1.369|2.305|2.661|2.279|2.553|2.301|2.320|1.236|1.399|1.917|2.603|1.473|1.165| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  255(bold)|1.330|2.020|1.424|1.922|1.377|1.246|2.292|1.860|2.211|1.491|1.765|1.877|1.769|1.346|1.254|1.030|1.247| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  270(bold)|1.678|1.445|1.273|1.352|1.124|1.073|1.816|2.062|1.670|1.783|1.954|1.863|1.126|1.101|1.899|1.873|1.447|1.790| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  285(bold)|2.229|1.434|1.126|1.382|1.452|1.235|1.574|1.686|1.317|2.233|1.679|1.365|1.538|2.091|1.802|1.326|1.724|1.820|1.544| N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  300(bold)|1.984|1.260|1.376|1.654|1.267|1.324|1.276|1.376|1.379|1.589|1.483|1.376|1.206|1.877|1.328|1.884|1.648|1.856|2.252|1.892| N/A | N/A | N/A | N/A | N/A | N/A |
|  315(bold)|1.657|0.954|1.612|1.860|1.362|1.036|1.054|1.027|1.560|1.691|1.451|1.410|1.529|1.613|1.891|1.473|2.193|2.293|1.916|1.422|1.049| N/A | N/A | N/A | N/A | N/A |
|  330(bold)|1.720|1.187|1.949|1.432|1.100|1.032|1.053|0.896|1.014|1.199|1.280|1.183|2.265|2.002|1.948|2.021|1.975|1.584|1.175|1.098|0.907|0.717| N/A | N/A | N/A | N/A |
|  345(bold)|1.727|1.537|2.005|1.093|1.244|1.079|0.679|0.759|1.069|1.138|1.370|2.454|1.900|1.948|1.973|1.964|1.576|0.984|0.860|0.764|0.976|0.656|0.603| N/A | N/A | N/A |
|  360(bold)|1.648|1.601|1.998|0.899|1.143|1.631|0.870|1.236|1.232|1.041|1.832|2.023|1.840|2.496|1.887|1.869|1.033|0.886|0.771|0.967|0.680|0.697|0.630|0.634| N/A | N/A |
|  375(bold)|1.525|1.890|2.220|1.414|1.413|1.190|1.227|1.467|1.246|1.451|2.175|1.968|1.941|1.781|1.948|1.394|1.061|0.779|0.869|0.752|0.753|0.533|0.883|1.072|1.177| N/A |
|  390(bold)|1.506|1.829|2.222|1.476|1.508|1.189|1.873|1.583|1.602|1.807|1.765|1.434|1.997|1.896|1.582|1.338|0.883|0.810|0.716|0.728|0.624|0.849|0.905|1.106|0.944|1.140|

In addition, this was done for the NASDAQ, S&P500, and DOW. The NASDAQ results were picked, because they were the best. There is no guarantee that applying these rolling averages will outperform the underlying security into the future. If the behavior of the underlying security changes, it could go from profitable to generating losses. Periods of losses can be seen in the line representing the strategy. If the market were to go back to its behavior during one of these times, it could generate losses; and if long enough, it could wipe out any profits. Another characteristic worth noting is the increased volatility of the trading strategy versus the underlying security. This seems to represent the classic risk-reward trade off.

## What do we do next? Wait and see...
