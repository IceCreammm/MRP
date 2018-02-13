import pandas_datareader.data as web

# Define the instruments to download. We would like to see stocks and S&P500 index.
tickers = ['^GSPC','^DJI','AA','BAC','HPQ', 'MMM', 'AXP','AAPL','BA','CAT','CVX','CSCO','KO','DWDP','XOM','GE','GS','HD','IBM','INTC','JNJ','JPM',
          'MCD','MRK','MSFT','NKE','PFE','PG','TRV','UNH','UTX','VZ','V','WMT','DIS']

# Define which online source one should use
data_source = 'yahoo'

# We would like all available data from 01/01/2000 until 01/01/2018.
start_date = '2000-01-01'
end_date = '2018-01-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
all_data = web.DataReader(tickers, data_source, start_date, end_date)

etf_tickers = ['SPY','IVV','VTI','VOO','QQQ','AGG','IJH','IWM','IWF','BND','IWD','VTV','IJR','LQD','XLF','VUG','VNQ','DIA','VO','VB','IVW']

 
data_source = 'yahoo'

 
start_date = '2000-01-01'
end_date = '2018-01-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
etf_data = web.DataReader(etf_tickers, data_source, start_date, end_date)

etf_data.to_excel('etf_data.xlsx')