# Stock Portfolio Performance Tracker

## Overview
A Python-based utility that tracks stock portfolio performance by calculating invested capital, current market value, and percentage gain or loss for individual stock holdings. The application saves portfolio performance records to a CSV file for future reference.

## Features
- Accepts stock ticker symbols, purchase prices, and share quantities.
- Loads supported ticker symbols from an S&P 500 CSV dataset.
- Retrieves the latest available stock prices using Yahoo Finance.
- Calculates invested amount and current market value.
- Computes individual and overall portfolio gain or loss.
- Exports transaction summaries to `portfolio_summary.csv`.
- Handles invalid numerical input and unavailable stock prices.

## Technologies Used
- Python 3
- CSV module
- File handling
- `yfinance` library

## Project Structure
```text
Stock-Portfolio-Tracker/
├── portfolio.py
├── sp500_tickers.csv
├── portfolio_summary.csv  # Generated when the program runs
└── README.md
```

## Requirements
- Python 3.9 or later
- Internet connection for retrieving stock prices
- `yfinance` Python package

## Installation and Setup

1. Clone or download this repository.
2. Open the project folder in PyCharm.
3. Install the required dependency:

   ```bash
   python -m pip install yfinance
   ```

4. Ensure the S&P 500 ticker dataset is saved in the project folder as `sp500_tickers.csv`.

## How to Run

Execute the following command in the terminal:

```bash
python portfolio.py
```

Follow the prompts to enter a stock ticker, purchase price, and number of shares. Enter `done` when you have finished adding holdings.

The program displays individual holding performance and an overall portfolio summary, then saves the results to `portfolio_summary.csv`.

## Calculations

- **Invested Amount** = Buy Price × Quantity
- **Current Market Value** = Current Price × Quantity
- **Gain/Loss** = Current Market Value − Invested Amount
- **Gain/Loss (%)** = (Gain/Loss ÷ Invested Amount) × 100

## Output
The generated CSV contains the date, ticker symbol, buy price, quantity, current price, invested amount, current value, gain/loss, and gain/loss percentage.

## Limitations
- Stock prices depend on the availability and accuracy of Yahoo Finance data.
- Prices may be delayed and should not be treated as guaranteed real-time market quotes.
- The application is intended for educational purposes and is not financial advice.

