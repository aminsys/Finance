# Finance
## A repository for financial analysis and visualization

### FinanceRSINotify.py
The function of the file YFinanceRSINotify.py uses Pandas DataReader to fetch all tickers' information from Yahoo Finance at a given date intervals:

`
data = web.DataReader(stockList[s], 'yahoo', start, end)
`

For the time being, this function gets the tickers information since the 1st of September 2021 till today's date. The function will clean up the the data, calculate the RSI based on the "Close" value of the stock, and writes the RSI into a text file (.txt) along with the stock values at "Open", "High", "Low", "Close", "Adj Close", and "Volume".
