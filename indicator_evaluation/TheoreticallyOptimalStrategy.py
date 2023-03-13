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

def testPolicy(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000):

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
    
    yest = sd
    yest_price = 0.0
    dayB4share = 0.0
    for x in prices.index:
        if x != prices.first_valid_index():
            if yest_price > prices[symbol][x]:
                if dayB4share == 1000.0:
                    orders[symbol][yest] = - 2000.0
                    dayB4share = -1000.0
                elif dayB4share == 0.0:
                    orders[symbol][yest] = -1000.0
                    dayB4share = -1000.0
                elif dayB4share == -1000.0:
                    orders[symbol][yest] = 0.0
                    dayB4share = -1000.0
            elif yest_price < prices[symbol][x]:
                if dayB4share == 1000.0:
                    orders[symbol][yest] = 0
                    dayB4share = 1000.0
                elif dayB4share == 0.0:
                    orders[symbol][yest] = 1000.0
                    dayB4share = 1000.0
                elif dayB4share == -1000.0:
                    orders[symbol][yest] = 2000.0
                    dayB4share = 1000.0
            elif yest_price == prices[symbol][x]:
                if dayB4share == 1000.0:
                    orders[symbol][yest] = 0.0
                    dayB4share = 1000.0
                elif dayB4share == 0.0:
                    orders[symbol][yest] = 0.0
                    dayB4share = 0.0
                elif dayB4share == -1000.0:
                    orders[symbol][yest] = 0.0
                    dayB4share = -1000.0
        yest_price = prices[symbol][x]
        yest = x

    if dayB4share == 1000.0:
        orders[symbol][prices.last_valid_index()] = -1000.0
    elif dayB4share == -1000.0:
        orders[symbol][prices.last_valid_index()] = 1000.0

    return orders