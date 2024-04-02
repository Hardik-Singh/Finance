import yfinance as yf
from datetime import datetime
from fastapi import FastAPI

companies = ['AMZN','GOOG','WMT','TSLA','META'] 

tickers = yf.Tickers(companies)
tickers_hist = tickers.history(period='max',start="2024-03-01", interval='1d')


print(tickers_hist)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": tickers_hist}