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

def RSI(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), rsi_days = 130):
    # https://www.learnpythonwithrune.org/pandas-calculate-the-relative-strength-index-rsi-on-a-stock/ code help
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.clip.html learned to use clip

    sym = []
    sym.append(symbol)
    dates = pd.date_range(sd - pd.DateOffset(days=2*rsi_days), ed)  		  	   		  		 			  		 			     			  	 
    prices_all = get_data(sym, dates)  # automatically adds SPY  	
    prices_all.fillna(method="ffill", inplace=True)
    prices_all.fillna(method="bfill", inplace=True)	
    prices_all = prices_all.dropna()	  		 			     			  	 
    prices = prices_all[sym]  # only portfolio symbols 

    delta = prices.diff()
    up = delta.clip(lower=0)
    down = -1*delta.clip(upper=0)
    up_gain = up.rolling(window=rsi_days).mean()
    down_loss = down.rolling(window=rsi_days).mean()

    rs = up_gain/down_loss
    rsi = 100.0 - (100.0 / (1.0 + rs))

    mask = (rsi.index >= sd) & (rsi.index <= ed)
    filtered_roc = rsi.loc[mask]

    return(filtered_roc[symbol])

def ROC(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), roc_days = 100):
    # http://www.andrewshamlet.net/2017/07/07/python-tutorial-roc/ code help

    sym = []
    sym.append(symbol)
    dates = pd.date_range(sd - pd.DateOffset(days=2*roc_days), ed) 	  	   		  		 			  		 			     			  	 
    prices_all = get_data(sym, dates)  # automatically adds SPY  	
    prices_all.fillna(method="ffill", inplace=True)
    prices_all.fillna(method="bfill", inplace=True)	
    prices_all = prices_all.dropna()	  		 			     			  	 
    prices = prices_all[sym]  # only portfolio symbols 

    roc = pd.Series((((prices[symbol].diff(roc_days - 1)) / (prices[symbol].shift(roc_days - 1)  )) * 100))  

    mask = (roc.index >= sd) & (roc.index <= ed)
    filtered_roc = roc.loc[mask]

    return(filtered_roc)

def TEMA(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), tema_days = 190):
    sym = []
    sym.append(symbol)
    dates = pd.date_range(sd, ed)  		  	   		  		 			  		 			     			  	 
    prices_all = get_data(sym, dates)  # automatically adds SPY  	
    prices_all.fillna(method="ffill", inplace=True)
    prices_all.fillna(method="bfill", inplace=True)	
    prices_all = prices_all.dropna()	  		 			     			  	 
    prices = prices_all[sym]  # only portfolio symbols 

    ema1 = prices[symbol].ewm(span=tema_days, adjust=False).mean()
    ema2 = ema1.ewm(span=tema_days, adjust=False).mean()
    ema3 = ema2.ewm(span=tema_days, adjust=False).mean()

    tema = 3 * (ema1 - ema2) + ema3

    return(tema)