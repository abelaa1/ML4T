import indicators as ind

import matplotlib.pyplot as plt	
import datetime as dt  
import numpy as np  		  	   		  		 			  		 			     			  	 
import math as m 	   		  		 			  		 			     			  	 
import pandas as pd  		  	   		  		 			  		 			     			  	 
from util import get_data, plot_data

def testPolicy(symbol = "AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000):
    TEMAorders = ind.TEMA(symbol,sd,ed)
    ROCorders = ind.ROC(symbol,sd,ed)
    RSIorders = ind.RSI(symbol,sd,ed)

    dates = pd.date_range(sd, ed)  
    orders = pd.DataFrame(index=dates)
    orders[symbol] = 0.0

    sym = []
    sym.append(symbol)
    prices = get_data(sym, dates)[sym]

    currentHolding = 0.0
    for x in prices.index:
        temp = TEMAorders[symbol][x] + ROCorders[symbol][x] + RSIorders[symbol][x]
        if temp > 2:
            if currentHolding == 0.0:
                orders[symbol][x] = 1000.0
                currentHolding = 1000.0
            elif currentHolding == 1000.0:
                orders[symbol][x] = 0.0
                currentHolding = 1000.0
            elif currentHolding == -1000.0:
                orders[symbol][x] = 2000.0
                currentHolding = 1000.0
        elif temp < -2:
            if currentHolding == 0.0:
                orders[symbol][x] = -1000.0
                currentHolding = -1000.0
            elif currentHolding == 1000.0:
                orders[symbol][x] = -2000.0
                currentHolding = -1000.0
            elif currentHolding == -1000.0:
                orders[symbol][x] = 0.0
                currentHolding = -1000.0
        elif temp == 0:
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