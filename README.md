# Quant_Analysis_Project  
Apply machine learning including neural networks through financial quantitative analysis to identify profitable investment strategies.  

## Utilize Yahoo API for Financial Data  
* http://www.learndatasci.com/python-finance-part-yahoo-finance-api-pandas-matplotlib/

## Deciding on Index  

<img align="right" src="/plots/index_comp_plot.png" alt="NASDAQ Plot" width=51% hspace=1% vspace=2%>   

<img align="right" src="/plots/dow_plot.png" alt="Dow Plot" width=51% hspace=1% vspace=2%>  

<img align="right" src="/plots/snp_plot.png" alt="S&P Plot" width=51% hspace=1% vspace=2%>  

<img align="right" src="/plots/nasdaq_plot.png" alt="NASDAQ Plot" width=51% hspace=1% vspace=2%>

Normalizing data based on first trading day of dataset. The plots are all very similar.

For this analysis it is important that we have a limited, yet diverse, set of securities to choose from. It is also important that we have a benchmark to compare the success of our trading strategies to.  

The weighting methodology of the indexes is of concern. The weighting applied within the S&P 500 is based on direct market capitalization, so large companies have a larger impact on movements in the S&P 500. The Dow is price weighted, so companies with higher security prices will have a larger impact on index movements. Price weighting is also more difficult to track over time, given activities such as share splits or buybacks. Also, the effect of dividends needs to be taken into account. The NASDAQ uses a modified market capitalization weighting. This modified weighting complicates our calculations when breaking the indexes down into individual securities for analysis.  

The S&P 500 is made up of 500 companies, which is a manageable number of companies to use for analysis. The NASDAQ only has 100 companies, which is manageable; however, financial companies are excluded which limits potential diversification in our constructed subset portfolio. The Dow only includes 30 blue chip companies, which limits our ability to construct a diverse portfolio from a subset of these companies.

The S&P 500 covers the below sectors allowing better cross sector diversification.

| Sector |	12/31/2016 |
|:---|:---:|
| Consum. Disc.	| 12.03% |
| Consum. Stap.	| 9.37% |
| Energy	| 7.56%	|
| Financials	| 14.81%	|
| Health Care	| 13.63%	|
| Industrials	| 10.27%	|
| IT	| 20.77%	|
| Materials	| 2.84%	|
| Telecoms	| 2.66%	|
| Utilities	| 3.17%	|
| Real Estate	| 2.89%	|  

*** http://siblisresearch.com/data/sp-500-sector-weightings/

Based on this initial analysis of three common indexes, the S&P 500 will be used as the benchmark and a portfolio will be constructed from a subset of the companies within the S&P 500.
