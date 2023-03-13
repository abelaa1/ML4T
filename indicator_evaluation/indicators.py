import matplotlib.pyplot as plt	
import datetime as dt  
import numpy as np  		  	   		  		 			  		 			     			  	 
import math as m 	   		  		 			  		 			     			  	 
import pandas as pd  		  	   		  		 			  		 			     			  	 
from util import get_data, plot_data


def author():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    :return: The GT username of the student  		  	   		  		 			  		 			     			  	 
    :rtype: str  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    return "aaguilar61"

def SMA(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31)):
    # https://www.geeksforgeeks.org/how-to-calculate-moving-average-in-a-pandas-dataframe/ to help code
    sym = []
    sym.append(symbol)
    dates = pd.date_range(sd, ed)  		  	   		  		 			  		 			     			  	 
    prices_all = get_data(sym, dates)  # automatically adds SPY  	
    prices_all.fillna(method="ffill", inplace=True)
    prices_all.fillna(method="bfill", inplace=True)	
    prices_all = prices_all.dropna()	  		 			     			  	 
    prices = prices_all[sym]  # only portfolio symbols 

    sma_days = 100
    sma = prices[symbol].rolling(window=sma_days).mean()

    orders = pd.DataFrame(index=dates)
    orders[symbol] = 0.0

    currentHolding = 0.0
    for x in prices.index:
        if not np.isnan(sma[x]):
            if prices[symbol][x] > (sma[x]*1.1):
                if currentHolding == 0.0:
                    orders[symbol][x] = 1000.0
                    currentHolding = 1000.0
                elif currentHolding == 1000.0:
                    orders[symbol][x] = 0.0
                    currentHolding = 1000.0
                elif currentHolding == -1000.0:
                    orders[symbol][x] = 2000.0
                    currentHolding = 1000.0
            elif prices[symbol][x] < (sma[x]*0.9):
                if currentHolding == 0.0:
                    orders[symbol][x] = -1000.0
                    currentHolding = -1000.0
                elif currentHolding == 1000.0:
                    orders[symbol][x] = -2000.0
                    currentHolding = -1000.0
                elif currentHolding == -1000.0:
                    orders[symbol][x] = 0.0
                    currentHolding = -1000.0
    
    if currentHolding == 1000.0:
        orders[symbol][prices.last_valid_index()] = -1000.0
    elif currentHolding == -1000.0:
        orders[symbol][prices.last_valid_index()] = 1000.0

    plt.plot(sma)
    plt.plot(prices)
    plt.legend(["SMA", "Prices"])
    plt.title("SMA vs Prices (100 day moving average)")
    plt.xlabel("Date")
    plt.ylabel("Prices")
    plt.savefig("images/figure2.png")

    return(orders)

def EMA(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31)):
    # https://www.geeksforgeeks.org/how-to-calculate-an-exponential-moving-average-in-python/ code help
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ewm.html learned about ewm
    sym = []
    sym.append(symbol)
    dates = pd.date_range(sd, ed)  		  	   		  		 			  		 			     			  	 
    prices_all = get_data(sym, dates)  # automatically adds SPY  	
    prices_all.fillna(method="ffill", inplace=True)
    prices_all.fillna(method="bfill", inplace=True)	
    prices_all = prices_all.dropna()	  		 			     			  	 
    prices = prices_all[sym]  # only portfolio symbols 

    ema_days = 30
    ema = prices[symbol].ewm(span=ema_days, adjust=False).mean()

    orders = pd.DataFrame(index=dates)
    orders[symbol] = 0.0

    currentHolding = 0.0
    for x in prices.index:
        if not np.isnan(ema[x]):
            if prices[symbol][x] > (ema[x]*1.1):
                if currentHolding == 0.0:
                    orders[symbol][x] = 1000.0
                    currentHolding = 1000.0
                elif currentHolding == 1000.0:
                    orders[symbol][x] = 0.0
                    currentHolding = 1000.0
                elif currentHolding == -1000.0:
                    orders[symbol][x] = 2000.0
                    currentHolding = 1000.0
            elif prices[symbol][x] < (ema[x]*0.9):
                if currentHolding == 0.0:
                    orders[symbol][x] = -1000.0
                    currentHolding = -1000.0
                elif currentHolding == 1000.0:
                    orders[symbol][x] = -2000.0
                    currentHolding = -1000.0
                elif currentHolding == -1000.0:
                    orders[symbol][x] = 0.0
                    currentHolding = -1000.0
    
    if currentHolding == 1000.0:
        orders[symbol][prices.last_valid_index()] = -1000.0
    elif currentHolding == -1000.0:
        orders[symbol][prices.last_valid_index()] = 1000.0

    plt.plot(ema)
    plt.plot(prices)
    plt.legend(["EMA", "Prices"])
    plt.title("EMA vs Prices (30 day moving average)")
    plt.xlabel("Date")
    plt.ylabel("Prices")
    plt.savefig("images/figure3.png")

    return(orders)

def RSI(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31)):
    # https://www.learnpythonwithrune.org/pandas-calculate-the-relative-strength-index-rsi-on-a-stock/ code help
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.clip.html learned to use clip
    sym = []
    sym.append(symbol)
    dates = pd.date_range(sd, ed)  		  	   		  		 			  		 			     			  	 
    prices_all = get_data(sym, dates)  # automatically adds SPY  	
    prices_all.fillna(method="ffill", inplace=True)
    prices_all.fillna(method="bfill", inplace=True)	
    prices_all = prices_all.dropna()	  		 			     			  	 
    prices = prices_all[sym]  # only portfolio symbols 

    rsi_days = 30

    delta = prices.diff()
    up = delta.clip(lower=0)
    down = -1*delta.clip(upper=0)
    up_gain = up.rolling(window=rsi_days).mean()
    down_loss = down.rolling(window=rsi_days).mean()

    rs = up_gain/down_loss
    rsi = 100.0 - (100.0 / (1.0 + rs))

    orders = pd.DataFrame(index=dates)
    orders[symbol] = 0.0

    currentHolding = 0.0
    upperflag = 0
    lowerflag = 0
    for x in prices.index:
        if not np.isnan(rsi[symbol][x]):
            if rsi[symbol][x] > 70:
                upperflag = 1
            elif rsi[symbol][x] < 30:
                lowerflag = 1
            if upperflag == 1 and rsi[symbol][x] < 70:
                upperflag = 0
                if currentHolding == 0.0:
                    orders[symbol][x] = -1000.0
                    currentHolding = -1000.0
                elif currentHolding == 1000.0:
                    orders[symbol][x] = -2000.0
                    currentHolding = -1000.0
                elif currentHolding == -1000.0:
                    orders[symbol][x] = 0.0
                    currentHolding = -1000.0
            elif lowerflag ==1 and rsi[symbol][x] > 30:
                lowerflag = 0
                if currentHolding == 0.0:
                    orders[symbol][x] = 1000.0
                    currentHolding = 1000.0
                elif currentHolding == 1000.0:
                    orders[symbol][x] = 0.0
                    currentHolding = 1000.0
                elif currentHolding == -1000.0:
                    orders[symbol][x] = 2000.0
                    currentHolding = 1000.0
    
    if currentHolding == 1000.0:
        orders[symbol][prices.last_valid_index()] = -1000.0
    elif currentHolding == -1000.0:
        orders[symbol][prices.last_valid_index()] = 1000.0


    plt.plot(rsi)
    plt.axhline(y=70, color = 'r')
    plt.axhline(y=30, color = 'r')
    plt.legend(["RSI"])
    plt.title("RSI")
    plt.xlabel("Date")
    plt.ylabel("Momentum")
    plt.savefig("images/figure5.png")

    return(orders)

def ROC(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31)):
    # http://www.andrewshamlet.net/2017/07/07/python-tutorial-roc/ code help
    sym = []
    sym.append(symbol)
    dates = pd.date_range(sd, ed)  		  	   		  		 			  		 			     			  	 
    prices_all = get_data(sym, dates)  # automatically adds SPY  	
    prices_all.fillna(method="ffill", inplace=True)
    prices_all.fillna(method="bfill", inplace=True)	
    prices_all = prices_all.dropna()	  		 			     			  	 
    prices = prices_all[sym]  # only portfolio symbols 

    roc_days = 100
    roc = pd.Series((((prices[symbol].diff(roc_days - 1)) / (prices[symbol].shift(roc_days - 1)  )) * 100))  

    orders = pd.DataFrame(index=dates)
    orders[symbol] = 0.0

    currentHolding = 0.0
    for x in prices.index:
        if not np.isnan(roc[x]):
            if roc[x] > 20:
                if currentHolding == 0.0:
                    orders[symbol][x] = 1000.0
                    currentHolding = 1000.0
                elif currentHolding == 1000.0:
                    orders[symbol][x] = 0.0
                    currentHolding = 1000.0
                elif currentHolding == -1000.0:
                    orders[symbol][x] = 2000.0
                    currentHolding = 1000.0
            elif roc[x] < -20:
                if currentHolding == 0.0:
                    orders[symbol][x] = -1000.0
                    currentHolding = -1000.0
                elif currentHolding == 1000.0:
                    orders[symbol][x] = -2000.0
                    currentHolding = -1000.0
                elif currentHolding == -1000.0:
                    orders[symbol][x] = 0.0
                    currentHolding = -1000.0
    
    if currentHolding == 1000.0:
        orders[symbol][prices.last_valid_index()] = -1000.0
    elif currentHolding == -1000.0:
        orders[symbol][prices.last_valid_index()] = 1000.0

    plt.plot(roc)
    plt.axhline(y=0, color = 'r')
    plt.legend(["ROC"])
    plt.title("ROC")
    plt.xlabel("Date")
    plt.ylabel("Momentum")
    plt.savefig("images/figure6.png")

    return(orders)

def TEMA(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31)):
    sym = []
    sym.append(symbol)
    dates = pd.date_range(sd, ed)  		  	   		  		 			  		 			     			  	 
    prices_all = get_data(sym, dates)  # automatically adds SPY  	
    prices_all.fillna(method="ffill", inplace=True)
    prices_all.fillna(method="bfill", inplace=True)	
    prices_all = prices_all.dropna()	  		 			     			  	 
    prices = prices_all[sym]  # only portfolio symbols 

    tema_days = 30
    ema1 = prices[symbol].ewm(span=tema_days, adjust=False).mean()
    ema2 = ema1.ewm(span=tema_days, adjust=False).mean()
    ema3 = ema2.ewm(span=tema_days, adjust=False).mean()

    tema = 3 * (ema1 - ema2) + ema3

    orders = pd.DataFrame(index=dates)
    orders[symbol] = 0.0

    currentHolding = 0.0
    for x in prices.index:
        if not np.isnan(tema[x]):
            if prices[symbol][x] > (tema[x]*1.1):
                if currentHolding == 0.0:
                    orders[symbol][x] = 1000.0
                    currentHolding = 1000.0
                elif currentHolding == 1000.0:
                    orders[symbol][x] = 0.0
                    currentHolding = 1000.0
                elif currentHolding == -1000.0:
                    orders[symbol][x] = 2000.0
                    currentHolding = 1000.0
            elif prices[symbol][x] < (tema[x]*0.9):
                if currentHolding == 0.0:
                    orders[symbol][x] = -1000.0
                    currentHolding = -1000.0
                elif currentHolding == 1000.0:
                    orders[symbol][x] = -2000.0
                    currentHolding = -1000.0
                elif currentHolding == -1000.0:
                    orders[symbol][x] = 0.0
                    currentHolding = -1000.0
    
    if currentHolding == 1000.0:
        orders[symbol][prices.last_valid_index()] = -1000.0
    elif currentHolding == -1000.0:
        orders[symbol][prices.last_valid_index()] = 1000.0

    plt.plot(tema)
    plt.plot(prices)
    plt.legend(["TEMA", "Prices"])
    plt.title("TEMA vs Prices (30 day moving average)")
    plt.xlabel("Date")
    plt.ylabel("Prices")
    plt.savefig("images/figure4.png")

    return(orders)