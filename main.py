import yfinance as yf
from datetime import datetime

companies = ['AMZN','GOOG','WMT','TSLA','META'] 

tickers = yf.Tickers(companies)
tickers_hist = tickers.history(period='max',start="2024-03-01", interval='1d',)
tickers_hist