Stock Analysis Using Candlestick Patterns and Volume Filtering

Overview

This script analyzes NSE (National Stock Exchange) F&O stocks by filtering stocks based on trading volume and candlestick patterns. It then plots Japanese candlestick charts with support and resistance levels to help identify potential trade opportunities.

Features
1. Fetches a predefined list of NSE F&O stocks.
2. Filters stocks with high trading volume compared to the last 10-day Exponential Moving Average (EMA).
3. Identifies key candlestick patterns (e.g., Marubozu, Doji, Hammer, Engulfing, Morning Star, etc.).
4. Plots the last 52 days of candlestick data along with support and resistance levels.

Dependencies

The following Python libraries are required to run this script:
1. yfinance (for fetching stock data)
2. pandas (for data manipulation)
3. numpy (for calculations)
4. matplotlib (for plotting charts)
5. mplfinance (for candlestick charts)


How It Works

Step 1: Fetch NSE F&O Stock List
1. The script starts by fetching a predefined list of NSE F&O stocks.

Step 2: Filter Stocks Based on Trading Volume
1. Downloads the last 20 days of stock data from Yahoo Finance.
2. Computes the 10-day EMA of trading volume.
3. Selects stocks where today’s volume is greater than yesterday’s EMA volume.

Step 3: Identify Stocks Based on Candlestick Patterns
1. Checks if the stock forms any key candlestick patterns (like Bullish Engulfing, Hammer, Doji, etc.).
2. If a pattern is found, the stock moves to the next step.

Step 4: Plot Candlestick Chart with Support & Resistance
1. Plots Japanese candlestick charts for selected stocks.
2. Calculates support and resistance levels based on the highest and lowest prices in the last 10 days.
3. Draws support and resistance lines on the chart.


The output will show:
1. Filtered stocks based on volume and candlestick patterns.
2. Candlestick charts with support & resistance levels.

Example Output
1. Text Output:

Step 1: F&O Stocks fetched: ["RELIANCE.NS", "TCS.NS", ...]
Step 2: Stocks filtered by volume: ["RELIANCE.NS", "INFY.NS"]
Step 3: Stocks filtered by candlestick patterns: ["RELIANCE.NS"]

1. Graphical Output:
2. A candlestick chart for “RELIANCE.NS” with support and resistance levels plotted.

Notes
1. The script does not make buy/sell recommendations but helps in technical analysis.
2. Ensure that Yahoo Finance is accessible, as it fetches real-time stock data from there.
