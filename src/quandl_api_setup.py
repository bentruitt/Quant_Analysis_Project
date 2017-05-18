import quandl

quandl.ApiConfig.api_key = "ZRwSW67EW9XKwU83bFr4"

data = quandl.get(["SF1/MMM_GP_MRQ","SF1/MMM_EPS_MRQ"], authtoken="ZRwSW67EW9XKwU83bFr4")

data2 = quandl.get(["NSE/OIL.1", "WIKI/AAPL.4"])
