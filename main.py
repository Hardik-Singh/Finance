import yfinance as yf
from datetime import datetime
from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get("/")
async def root():
    def get_history():
        companies = ['AMZN', 'GOOG', 'BTC-USD', 'TSLA', 'META']
        df_list = []
        for ticker in companies:
            data = yf.download(ticker, start="2024-03-01",group_by="Ticker", period='2d')
            data['ticker'] = ticker  # Add ticker column
            df_list.append(data)

        tickers_hist = pd.concat(df_list)
        return tickers_hist

    
    history = get_history()
    history.to_csv("data.csv")
    
    return {"message": history.to_string()}
