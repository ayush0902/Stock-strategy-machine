Stock Analysis Using Candlestick Patterns and Volume Filtering

Overview

This script analyzes NSE (National Stock Exchange) F&O stocks by filtering stocks based on trading volume and candlestick patterns. It then plots Japanese candlestick charts with support and resistance levels to help traders identify potential trade opportunities.

Features
	•	Fetches a predefined list of NSE F&O stocks.
	•	Filters stocks with high trading volume compared to the last 10-day Exponential Moving Average (EMA).
	•	Identifies key candlestick patterns (e.g., Marubozu, Doji, Hammer, Engulfing, Morning Star, etc.).
	•	Plots the last 52 days of candlestick data along with support and resistance levels.

Dependencies

The following Python libraries are required to run this script:
	•	yfinance (for fetching stock data)
	•	pandas (for data manipulation)
	•	numpy (for calculations)
	•	matplotlib (for plotting charts)
	•	mplfinance (for candlestick charts)

You can install them using:

pip install yfinance pandas numpy matplotlib mplfinance

How It Works

Step 1: Fetch NSE F&O Stock List
	•	The script starts by fetching a predefined list of NSE F&O stocks.

Step 2: Filter Stocks Based on Trading Volume
	•	Downloads the last 20 days of stock data from Yahoo Finance.
	•	Computes the 10-day EMA of trading volume.
	•	Selects stocks where today’s volume is greater than yesterday’s EMA volume.

Step 3: Identify Stocks Based on Candlestick Patterns
	•	Checks if the stock forms any key candlestick patterns (like Bullish Engulfing, Hammer, Doji, etc.).
	•	If a pattern is found, the stock moves to the next step.

Step 4: Plot Candlestick Chart with Support & Resistance
	•	Plots Japanese candlestick charts for selected stocks.
	•	Calculates support and resistance levels based on the highest and lowest prices in the last 10 days.
	•	Draws support and resistance lines on the chart.

Usage

To run the script, simply execute:

python script.py

The output will show:
	•	Filtered stocks based on volume and candlestick patterns.
	•	Candlestick charts with support & resistance levels.

Example Output
	•	Text Output:

Step 1: F&O Stocks fetched: ["RELIANCE.NS", "TCS.NS", ...]
Step 2: Stocks filtered by volume: ["RELIANCE.NS", "INFY.NS"]
Step 3: Stocks filtered by candlestick patterns: ["RELIANCE.NS"]


	•	Graphical Output:
	•	A candlestick chart for “RELIANCE.NS” with support and resistance levels plotted.

Notes
	•	The F&O stock list is predefined; you can modify it as needed.
	•	The script does not make buy/sell recommendations but helps in technical analysis.
	•	Ensure that Yahoo Finance is accessible, as it fetches real-time stock data from there.
