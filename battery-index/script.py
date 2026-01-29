import yfinance as yf
import json

# New "Hard Asset" tickers: LITP (Miners), ION (All Metals), LIT (Value Chain), ^DJC (Commodities)
tickers = ["LIT", "LITP", "ION", "GSG"]
df = yf.download(tickers, period="2y", interval="1mo")['Adj Close'].dropna()

data_dict = {t: [{"date": d.strftime('%Y-%m'), "price": round(v, 2)} 
             for d, v in df[t].items()] for t in tickers}

with open('battery-index/data.json', 'w') as f:
    json.dump(data_dict, f)
