import pandas as pd
import pandas_datareader as web
import datetime as dt
import pandas_ta as pta

ticker = ['VOLV-B.ST', 'NOVO-B.CO', 'RATO-B.ST',
              'EPI-B.ST', '2020.OL', 'ERIC-B.ST', 'ABB.ST',
              'SAS.ST', 'TELIA.ST', 'T', 'BPF-UN.TO', 'SINCH.ST', 
              'CORE-B.ST', 'VOLCAR-B.ST', 'NIO', 'KO', 'AMD',
              'MSFT', 'AAPL']

def GetRSIForAllStocks(period = 14, stockList = ticker):

    start = dt.datetime(2021, 9, 1)
    end = dt.datetime.now()

    try:
        for s in range(len(stockList)):
            data = web.DataReader(stockList[s], 'yahoo', start, end)
            data_ta = pta.rsi(data["Close"], length=period)
            result = pd.DataFrame({
                "RSI":data_ta.tail(-period),
                "Open":data["Open"].tail(-period),
                "High":data["High"].tail(-period),
                "Low":data["Low"].tail(-period),
                "Close":data["Close"].tail(-period),
                "Adj Close":data["Adj Close"].tail(-period),
                "Volume":data["Volume"].tail(-period)})
            
            

            # print(result)
            filename = stockList[s] + dt.datetime.now().strftime("_%Y%m%d_%H%M%S")
            with open(filename+".txt", "a") as f:
                f.write(result.to_string())
        
    except Exception as e:
        print('Error: {0}'.format(e))

def main():
    print("Running GetRSIForAllStocks from main()...")
    GetRSIForAllStocks(14, ['NOVO-B.CO', 'T', 'VOLV-B.ST', 'VOLCAR-B.ST'])

if __name__ == "__main__":
    main()
