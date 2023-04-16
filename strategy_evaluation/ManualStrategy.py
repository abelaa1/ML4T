import indicators as ind

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

def benchMark(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000):
    sym = []
    sym.append(symbol)
    dates = pd.date_range(sd, ed)  		  	   		  		 			  		 			     			  	 
    prices_all = get_data(sym, dates)  # automatically adds SPY  	
    prices_all.fillna(method="ffill", inplace=True)
    prices_all.fillna(method="bfill", inplace=True)	
    prices_all = prices_all.dropna()	  		 			     			  	 
    prices = prices_all[sym]  # only portfolio symbols 

    orders = pd.DataFrame(index=dates)
    orders[symbol] = 0.0

    orders[symbol][prices.first_valid_index()] = 1000
    orders[symbol][prices.last_valid_index()] = -1000

    return orders

def testPolicy(symbol = "AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000):
    dates = pd.date_range(sd, ed)  
    sym = []
    sym.append(symbol)
    prices = get_data(sym, dates)[sym]


    tema = ind.TEMA(symbol,sd,ed)
    TEMAorders = prices.copy()
    TEMAorders[symbol] = 0

    current = 0
    for x in prices.index:
        if not np.isnan(tema[x]):
            if prices[symbol][x] > (tema[x]*1.1):
                TEMAorders[symbol][x] = 1
                current = 1
            elif prices[symbol][x] < (tema[x]*0.9):
                TEMAorders[symbol][x] = -1
                current = -1
            else:
                TEMAorders[symbol][x] = current
    
    TEMAorders[symbol][prices.last_valid_index()] = 0


    roc = ind.ROC(symbol,sd,ed)
    ROCorders = prices.copy()
    ROCorders[symbol] = 0

    current = 0
    for x in prices.index:
        if not np.isnan(roc[x]):
            if roc[x] > 20:
                ROCorders[symbol][x] = 1
                current = 1
            elif roc[x] < -20:
                ROCorders[symbol][x] = -1
                current = -1
            else:
                ROCorders[symbol][x] = current
    
    ROCorders[symbol][prices.last_valid_index()] = 0


    rsi = ind.RSI(symbol,sd,ed)
    RSIorders = prices.copy()
    RSIorders[symbol] = 0

    current = 0
    upperflag = 0
    lowerflag = 0
    for x in prices.index:
        if not np.isnan(rsi[x]):
            if rsi[x] > 70:
                upperflag = 1
            elif rsi[x] < 30:
                lowerflag = 1
            if upperflag == 1 and rsi[x] < 70:
                upperflag = 0
                RSIorders[symbol][x] = -1
                current = -1
            elif lowerflag ==1 and rsi[x] > 30:
                lowerflag = 0
                RSIorders[symbol][x] = 1
                current = 1
            else:
                RSIorders[symbol][x] = current
    
    RSIorders[symbol][prices.last_valid_index()] = 0

    orders = prices.copy()
    orders[symbol] = 0.0

    currentHolding = 0.0
    for x in prices.index:
        temp = TEMAorders[symbol][x] + ROCorders[symbol][x] + RSIorders[symbol][x]
        if temp >= 2:
            if currentHolding == 0.0:
                orders[symbol][x] = 1000.0
                currentHolding = 1000.0
            elif currentHolding == 1000.0:
                orders[symbol][x] = 0.0
                currentHolding = 1000.0
            elif currentHolding == -1000.0:
                orders[symbol][x] = 2000.0
                currentHolding = 1000.0
        elif temp <= -2:
            if currentHolding == 0.0:
                orders[symbol][x] = -1000.0
                currentHolding = -1000.0
            elif currentHolding == 1000.0:
                orders[symbol][x] = -2000.0
                currentHolding = -1000.0
            elif currentHolding == -1000.0:
                orders[symbol][x] = 0.0
                currentHolding = -1000.0
        else:
            if currentHolding == 0.0:
                orders[symbol][x] = 0.0
                currentHolding = 0.0
            elif currentHolding == 1000.0:
                orders[symbol][x] = -1000.0
                currentHolding = 0.0
            elif currentHolding == -1000.0:
                orders[symbol][x] = 1000
                currentHolding = 0.0
    
    if currentHolding == 1000.0:
        orders[symbol][orders.last_valid_index()] = -1000.0
    elif currentHolding == -1000.0:
        orders[symbol][orders.last_valid_index()] = 1000.0

    return orders