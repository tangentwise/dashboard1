import yfinance as yf
import json
import os

# Agreed Tickers: UPS, FedEx, Expeditors, Amazon
tickers = ["UPS", "FDX", "EXPD", "AMZN"]
data_dict = {}

for t in tickers:
    try:
        print(f"Syncing {t}...")

        # Use the Ticker object method for cleaner data retrieval
        ticker = yf.Ticker(t)
        df = ticker.history(period="2y", interval="1mo")

        if df is not None and not df.empty:
            # Ensure price is a float and handles any potential missing values
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

# Ensure directory matches your logistics folder structure
os.makedirs("last-mile", exist_ok=True)

with open("last-mile/data.json", "w") as f:
    json.dump(data_dict, f, indent=2)

print("Last Mile batch sync complete.")
