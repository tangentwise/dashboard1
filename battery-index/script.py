import yfinance as yf
import json
import os

tickers = ["LIT", "LITP", "ION", "GSG"]
data_dict = {}

for t in tickers:
    try:
        print(f"Syncing {t}...")

        ticker = yf.Ticker(t)
        df = ticker.history(period="2y", interval="1mo")

        if df is not None and not df.empty:
            series = df["Close"].astype(float)

            data_dict[t] = [
                {
                    "date": d.strftime("%Y-%m"),
                    "price": round(v, 2)
                }
                for d, v in series.items()
            ]

            print(f"Successfully added {t} ({len(series)} points)")
        else:
            print(f"No data returned for {t}")

    except Exception as e:
        print(f"Error downloading {t}: {e}")

os.makedirs("battery-index", exist_ok=True)

with open("battery-index/data.json", "w") as f:
    json.dump(data_dict, f, indent=2)

print("Batch sync complete.")
