import requests as req
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import time

def price(symbol ="BTC", comparison_symbol=["USD"], e=''):
    try:
        url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
                .format(symbol.upper(), ','.join(comparison_symbol).upper())
        if e!='':
            url +='&e=' + e
        data = req.get(url)
        return data.json()
    except:
        #return "Unavailable to get the data for {} in {} from {}".format(symbol.upper(), ','.join(comparison_symbol).upper(), e)
        return -1

def historicalData(symbol="BTC", comparison_symbol="USD", all_data=True, limit=1, aggregate=1, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    if all_data:
        url += '&allData=true'
    page = req.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df

def plotGraph(x, y, title="", fig=None):
    if fig == None:
        fig = plt.gcf()
        fig.show()
    plt.title(title)
    plt.plot(x, y)
    fig.canvas.draw()
    #return fig

def realTimeGraph():
    
    x = []
    y=[]
    fig = plt.gcf()
    fig.show()
    pr = 0
    for i in range(100): 
        x.append(i+1)
        data = price()
        if data != -1:
            pr = data["USD"]


        print(i+1)
        print(pr)

        y.append(pr)

        plotGraph(x, y, '', fig)
        #time.sleep(10)
        plt.pause(15)






