import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt

ticker = ['VOLV-B.ST', 'NOVO-B.CO', 'RATO-B.ST', 'ASAP.ST',
              'EPI-B.ST', '2020.OL', 'ERIC-B.ST', 'ABB.ST',
              'SAS.ST', 'TELIA.ST', 'T', 'ANOT.ST', 'BPF-UN.TO']


def getAllData():
    for t in range(len(ticker)):
        getDataForRSI(t)
        

def getDataForRSI(t):

    start = dt.datetime(2021, 9, 1)
    end = dt.datetime.now()

    try:
        
        data = web.DataReader(ticker[t], 'yahoo', start, end)
        # print(data)

        delta = data['Adj Close'].diff(1)
        # print('Delta before droping NA: {0}'.format(delta))
        delta.dropna(inplace=True) # Get rid of all values that are not a number
        # print('Delta after droping NA: {0}'.format(delta))

        positive = delta.copy()
        negative = delta.copy()

        positive[positive < 0] = 0 # We only have zero or something positive
        negative[negative > 0] = 0
        # print('Positive: {0}'.format(positive))
        # print('Negative: {0}'.format(negative))

        days = 14 # days period for the RSI

        average_gain = positive.rolling(window=days).mean()
        average_loss = abs(negative.rolling(window=days).mean())

        relative_strength = average_gain/ average_loss
        # print('Relative Strength: {0}'.format(relative_strength))

        RSI = 100.0 - (100.0 / (1.0 + relative_strength))
        # print('RSI: {0}'.format(RSI))
        
    except Exception as e:
        print('Error: {0}'.format(e))

    plotRSI(ticker[t], data, RSI)
    # plotRSIexp(ticker[t], data, RSI) # Plot using plotly express.

# Plot using plotly express

def plotRSIexp(ticker_name, data, rsi):

    combined = pd.DataFrame()
    combined['Adj Close'] = data['Adj Close']
    combined['RSI'] = rsi

    fig = px.line(combined, x = combined.index, y = [combined['Adj Close'], combined['RSI']],
                                                title = ticker_name)
    
    """
    fig.add_hline(y = 100.0, line_dash = 'dash', line_color = '#ff0000', annotation_text = '100%')
    fig.add_hline(y = 90.0, line_dash = 'dash', line_color = '#ffaa00', annotation_text = '90%')
    fig.add_hline(y = 80.0, line_dash = 'dash', line_color = '#00ff00', annotation_text = '80%')
    fig.add_hline(y = 70.0, line_dash = 'dash', line_color = '#cccccc', annotation_text = '70%')
    
    fig.add_hline(y = 30.0, line_dash = 'dash', line_color = '#cccccc', annotation_text = '30%')
    fig.add_hline(y = 20.0, line_dash = 'dash', line_color = '#00ff00', annotation_text = '20%')
    fig.add_hline(y = 10.0, line_dash = 'dash', line_color = '#ffaa00', annotation_text = '10%')
    fig.add_hline(y = 0.0, line_dash = 'dash', line_color = '#ff0000', annotation_text = '0%')
    """
    fig.add_hrect(y0 = 10, y1 = 90, line_width = 0, fillcolor = 'red', opacity = 0.2)
    fig.add_hrect(y0 = 20, y1 = 80, line_width = 0, fillcolor = 'yellow', opacity = 0.3)
    fig.add_hrect(y0 = 30, y1 = 70, line_width = 0, fillcolor = 'green', opacity = 0.4)    

    fig.show()

    
        
# Plot the results of the RSI
def plotRSI(ticker_name, data, rsi):

    combined = pd.DataFrame()
    combined['Adj Close'] = data['Adj Close']
    combined['RSI'] = rsi

    plt.figure(figsize=(12,8))

    ax1 = plt.subplot(211)
    ax1.plot(combined.index, combined['Adj Close'], color='lightgray')

    ax1.set_title('Adjusted Close Price {0}'.format(ticker_name), color='white')

    ax1.grid(True, color='#555555')
    ax1.set_axisbelow(True)
    ax1.set_facecolor('black')
    ax1.figure.set_facecolor('#121212')
    ax1.tick_params(axis='x', colors = 'white')
    ax1.tick_params(axis='y', colors = 'white')

    ax2= plt.subplot(212, sharex=ax1)
    ax2.plot(combined.index, combined['RSI'], color='lightgray')
    
    ax2.axhline(0, linestyle='--', alpha=0.5, color='#ff0000')
    ax2.axhline(10, linestyle='--', alpha=0.5, color='#ffaa00')
    ax2.axhline(20, linestyle='--', alpha=0.5, color='#00ff00')
    ax2.axhline(30, linestyle='--', alpha=0.5, color='#cccccc')
    
    ax2.axhline(70, linestyle='--', alpha=0.5, color='#cccccc')
    ax2.axhline(80, linestyle='--', alpha=0.5, color='#00ff00')
    ax2.axhline(90, linestyle='--', alpha=0.5, color='#ffaa00')
    ax2.axhline(100, linestyle='--', alpha=0.5, color='#ff0000')

    ax2.set_title('RSI value', color='white')
    ax2.grid(False)
    ax2.set_axisbelow(True)
    ax2.set_facecolor('black')
    ax2.tick_params(axis='x', colors = 'white')
    ax2.tick_params(axis='y', colors = 'white')

    # plt.show()
    plt.savefig('RSI/{0}-{1}.png'.format(ticker_name, dt.datetime.now().strftime('%Y-%m-%d')))


def GetRSIForAllStocks(period = 14, stockList = ticker):

    start = dt.datetime(2021, 9, 1)
    end = dt.datetime.now()

    try:
        for s in range(len(stockList)):
            data = web.DataReader(stockList[s], 'yahoo', start, end)
            print("Row data {0}".format(data.tail(20)))

            delta = data['Close'].diff(1)
            print('Delta before droping NA: {0}'.format(delta.tail(20)))
            delta.dropna(inplace=True) # Get rid of all values that are not a number
            # print('Delta after droping NA: {0}'.format(delta.tail(20)))
            
            positive = delta.copy()
            negative = delta.copy()

            positive[positive < 0] = 0 # We only have zero or something positive
            negative[negative > 0] = 0
            # print('Positive: {0}'.format(positive))
            # print('Negative: {0}'.format(negative))

            # days = 14 # days period for the RSI

            average_gain = positive.rolling(window=period).mean()
            average_loss = abs(negative.rolling(window=period).mean())

            relative_strength = average_gain/ average_loss
            # print('Relative Strength: {0}'.format(relative_strength))

            RSI = 100.0 - (100.0 / (1.0 + relative_strength))
            # print('RSI: {0}'.format(RSI))
            print("RSI for {0} is: {1}".format(stockList[s], RSI.tail(20)))
        
    except Exception as e:
        print('Error: {0}'.format(e))
