
import csv
import os
from datetime import datetime

# Input and output files
DATASET_FILE = "sp500_tickers.csv"
OUTPUT_FILE = "portfolio_summary.csv"


def load_tickers():
    """Load available stock ticker symbols from the CSV dataset."""
    tickers = []

    if not os.path.exists(DATASET_FILE):
        print(f"Dataset not found: {DATASET_FILE}")
        return tickers

    with open(DATASET_FILE, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames:
            for row in reader:
                # Support common ticker column names
                for column in ("Symbol", "symbol", "Ticker", "ticker"):
                    if row.get(column):
                        tickers.append(row[column].strip().upper())
                        break

    return tickers


def get_current_price(ticker):
    """Fetch the latest available price using yfinance."""
    try:
        import yfinance as yf

        stock = yf.Ticker(ticker)
        history = stock.history(period="5d")

        if history.empty:
            return None

        return float(history["Close"].dropna().iloc[-1])

    except Exception:
        return None


def save_summary(records):
    """Write portfolio records to a CSV file."""
    fieldnames = [
        "Date",
        "Ticker",
        "Buy Price",
        "Quantity",
        "Current Price",
        "Invested Amount",
        "Current Value",
        "Gain/Loss",
        "Gain/Loss (%)"
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def main():
    print("=" * 45)
    print(" STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 45)

    available_tickers = load_tickers()

    if available_tickers:
        print(f"Loaded {len(available_tickers)} ticker symbols.")
    else:
        print("Dataset unavailable or ticker column not recognized.")
        print("You can still enter a ticker manually.")

    portfolio = []
    total_invested = 0.0
    total_current_value = 0.0

    while True:
        ticker = input(
            "\nEnter stock ticker (or 'done' to finish): "
        ).strip().upper()

        if ticker == "DONE":
            break

        if not ticker:
            print("Please enter a ticker symbol.")
            continue

        if available_tickers and ticker not in available_tickers:
            print("Ticker not found in the supplied dataset.")
            print("Please select a ticker from the dataset.")
            continue

        try:
            buy_price = float(input("Enter your buy price: "))
            quantity = int(input("Enter number of shares: "))

            if buy_price <= 0 or quantity <= 0:
                print("Price and quantity must be positive.")
                continue

        except ValueError:
            print("Enter a valid numeric price and whole-number quantity.")
            continue

        current_price = get_current_price(ticker)

        if current_price is None:
            print("Unable to fetch a current price for this ticker.")
            print("Check the ticker, internet connection, or try again.")
            continue

        invested = buy_price * quantity
        current_value = current_price * quantity
        gain_loss = current_value - invested
        gain_loss_percent = (gain_loss / invested) * 100

        portfolio.append({
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Ticker": ticker,
            "Buy Price": round(buy_price, 2),
            "Quantity": quantity,
            "Current Price": round(current_price, 2),
            "Invested Amount": round(invested, 2),
            "Current Value": round(current_value, 2),
            "Gain/Loss": round(gain_loss, 2),
            "Gain/Loss (%)": round(gain_loss_percent, 2)
        })

        total_invested += invested
        total_current_value += current_value

        print(f"\nStock: {ticker}")
        print(f"Current price: {current_price:.2f}")
        print(f"Invested amount: {invested:.2f}")
        print(f"Current value: {current_value:.2f}")
        print(f"Gain/Loss: {gain_loss:.2f} ({gain_loss_percent:.2f}%)")

    if not portfolio:
        print("\nNo valid holdings entered. No summary generated.")
        return

    save_summary(portfolio)

    total_gain_loss = total_current_value - total_invested
    total_gain_loss_percent = (
        total_gain_loss / total_invested
    ) * 100

    print("\n" + "=" * 45)
    print(" PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"Total invested: {total_invested:.2f}")
    print(f"Current market value: {total_current_value:.2f}")
    print(f"Total gain/loss: {total_gain_loss:.2f}")
    print(f"Overall return: {total_gain_loss_percent:.2f}%")
    print(f"\nCSV summary saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
