import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
import gzip, cPickle


with gzip.open('etf_data.pkl.gz', 'r') as f:
    etf_data = cPickle.load(f)

print etf_data.items

etf_adj_close = etf_data['Adj Close']

print etf_adj_close.head(10)

print etf_adj_close.tail(10)

with gzip.open('all_data.pkl.gz', 'r') as f:
    stock_data = cPickle.load(f)

stock_adj_close = stock_data['Adj Close']

GSPC = stock_adj_close['^GSPC']

print GSPC.head(10)

print GSPC.tail(10)

from scipy import stats
import statsmodels.api as sm
import statsmodels.tsa as tsa
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import coint

etf_spy = etf_adj_close['SPY']

coint(etf_spy,GSPC)
 
GSPC.corr(etf_spy)

pd.concat([GSPC, etf_spy], axis=1).plot()

etf_spy.plot()

GSPC.plot()

(GSPC - etf_spy).plot() # Plot the spread
plt.axhline((GSPC - etf_spy).mean(), color='red', linestyle='--') # Add the mean
plt.xlabel('Time')
plt.legend(['Price Spread', 'Mean'])


#================================ Test integration I(1) for every individual ETF==========================#

for i in range(etf_adj_close.shape[1]):
    print i

























