""""""  		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		  		 			  		 			     			  	 
All Rights Reserved  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Template code for CS 4646/7646  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		  		 			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		  		 			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		  		 			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 			  		 			     			  	 
or edited.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		  		 			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		  		 			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 			  		 			     			  	 
GT honor code violation.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
-----do not edit anything above this line---  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Student Name: Abel Aguilar		  	   		  		 			  		 			     			  	 
GT User ID: aaguilar61  		  	   		  		 			  		 			     			  	 
GT ID: 903861561 		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
import indicators as ind
import RTLearner as rt
import BagLearner as bl

import datetime as dt  		  	   		  		 			  		 			     			  	 
import random  
import numpy as np  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import pandas as pd  		  	   		  		 			  		 			     			  	 
import util as ut  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
class StrategyLearner(object):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  		 			  		 			     			  	 
        If verbose = False your code should not generate ANY output.  		  	   		  		 			  		 			     			  	 
    :type verbose: bool  		  	   		  		 			  		 			     			  	 
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		  		 			  		 			     			  	 
    :type impact: float  		  	   		  		 			  		 			     			  	 
    :param commission: The commission amount charged, defaults to 0.0  		  	   		  		 			  		 			     			  	 
    :type commission: float  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    # constructor  		  	   		  		 			  		 			     			  	 
    def __init__(self, verbose=False, impact=0.0, commission=0.0):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Constructor method  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        self.verbose = verbose  		  	   		  		 			  		 			     			  	 
        self.impact = impact  		  	   		  		 			  		 			     			  	 
        self.commission = commission 
        self.baglearner = bl.BagLearner(learner = rt.RTLearner, kwargs = {"leaf_size":5}, bags = 20, boost = False, verbose = False)

    def author(self):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        :return: The GT username of the student  		  	   		  		 			  		 			     			  	 
        :rtype: str  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        return "aaguilar61"		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # this method should create a QLearner, and train it for trading  		  	   		  		 			  		 			     			  	 
    def add_evidence(  		  	   		  		 			  		 			     			  	 
        self,  		  	   		  		 			  		 			     			  	 
        symbol="IBM",  		  	   		  		 			  		 			     			  	 
        sd=dt.datetime(2008, 1, 1),  		  	   		  		 			  		 			     			  	 
        ed=dt.datetime(2009, 1, 1),  		  	   		  		 			  		 			     			  	 
        sv=10000, 
        N = 8,
        YBUY = 0.02,
        YSELL = -0.01

    ):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Trains your strategy learner over a given time frame.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        :param symbol: The stock symbol to train on  		  	   		  		 			  		 			     			  	 
        :type symbol: str  		  	   		  		 			  		 			     			  	 
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  		 			  		 			     			  	 
        :type sd: datetime  		  	   		  		 			  		 			     			  	 
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  		 			  		 			     			  	 
        :type ed: datetime  		  	   		  		 			  		 			     			  	 
        :param sv: The starting value of the portfolio  		  	   		  		 			  		 			     			  	 
        :type sv: int  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        # add your code to do learning here  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        TEMAorders = ind.TEMA(symbol,sd,ed)
        TEMAorders = TEMAorders.to_numpy()
        min_val = np.min(TEMAorders)
        max_val = np.max(TEMAorders)
        # Normalize the array to be between 0 and 1
        TEMAorders = (2*(TEMAorders - min_val)/(max_val - min_val))

        ROCorders = ind.ROC(symbol,sd,ed)
        ROCorders = ROCorders.to_numpy()
        min_val = np.min(ROCorders)
        max_val = np.max(ROCorders)
        # Normalize the array to be between -1 and 1
        ROCorders = (2*(ROCorders - min_val)/(max_val - min_val)) - 1

        RSIorders = ind.RSI(symbol,sd,ed)	
        RSIorders = RSIorders.to_numpy()
        min_val = np.min(RSIorders)
        max_val = np.max(RSIorders)
        # Normalize the array to be between 0 and 1
        RSIorders = (2*(RSIorders - min_val)/(max_val - min_val))

        # https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html
        orders = np.column_stack((TEMAorders, ROCorders ,RSIorders))

        dates = pd.date_range(sd, ed)  
        sym = []
        sym.append(symbol)
        prices = ut.get_data(sym, dates)[sym]
        prices = prices.reset_index()
        y = []
        for x in prices.index:
            if x + N in prices.index:
                ret = (prices[symbol][x]/prices[symbol][x+N])-1
                if ret > (YBUY * (1.0+self.impact) * (1+(self.commission/prices[symbol][x]))):
                    y.append(-1)
                elif ret < (YSELL * (1.0-self.impact) * (1-(self.commission/prices[symbol][x]))):
                    y.append(1)
                else:
                    y.append(0)
            else:
                y.append(0)
        yVal = np.array(y)

        self.baglearner.add_evidence(orders,yVal)

  		  	   		  		 			  		 			     			  	 
    # this method should use the existing policy and test it against new data  		  	   		  		 			  		 			     			  	 
    def testPolicy(  		  	   		  		 			  		 			     			  	 
        self,  		  	   		  		 			  		 			     			  	 
        symbol="IBM",  		  	   		  		 			  		 			     			  	 
        sd=dt.datetime(2009, 1, 1),  		  	   		  		 			  		 			     			  	 
        ed=dt.datetime(2010, 1, 1),  		  	   		  		 			  		 			     			  	 
        sv=10000,  	   		  		 			  		 			     			  	 
    ):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Tests your learner using data outside of the training data  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        :param symbol: The stock symbol that you trained on on  		  	   		  		 			  		 			     			  	 
        :type symbol: str  		  	   		  		 			  		 			     			  	 
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  		 			  		 			     			  	 
        :type sd: datetime  		  	   		  		 			  		 			     			  	 
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  		 			  		 			     			  	 
        :type ed: datetime  		  	   		  		 			  		 			     			  	 
        :param sv: The starting value of the portfolio  		  	   		  		 			  		 			     			  	 
        :type sv: int  		  	   		  		 			  		 			     			  	 
        :return: A DataFrame with values representing trades for each day. Legal values are +1000.0 indicating  		  	   		  		 			  		 			     			  	 
            a BUY of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING.  		  	   		  		 			  		 			     			  	 
            Values of +2000 and -2000 for trades are also legal when switching from long to short or short to  		  	   		  		 			  		 			     			  	 
            long so long as net holdings are constrained to -1000, 0, and 1000.  		  	   		  		 			  		 			     			  	 
        :rtype: pandas.DataFrame  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        TEMAorders = ind.TEMA(symbol,sd,ed)
        TEMAorders = TEMAorders.to_numpy()
        min_val = np.min(TEMAorders)
        max_val = np.max(TEMAorders)
        # Normalize the array to be between 0 and 1
        TEMAorders = (2*(TEMAorders - min_val)/(max_val - min_val))

        ROCorders = ind.ROC(symbol,sd,ed)
        ROCorders = ROCorders.to_numpy()
        min_val = np.min(ROCorders)
        max_val = np.max(ROCorders)
        # Normalize the array to be between -1 and 1
        ROCorders = (2*(ROCorders - min_val)/(max_val - min_val)) - 1

        RSIorders = ind.RSI(symbol,sd,ed)	
        RSIorders = RSIorders.to_numpy()
        min_val = np.min(RSIorders)
        max_val = np.max(RSIorders)
        # Normalize the array to be between 0 and 1
        RSIorders = (2*(RSIorders - min_val)/(max_val - min_val))

        orders = np.column_stack((TEMAorders, ROCorders ,RSIorders))

        y = self.baglearner.query(orders)
        # here we build a fake set of trades  		  	   		  		 			  		 			     			  	 
        # your code should return the same sort of data  		  	   		  		 			  		 			     			  	 
        dates = pd.date_range(sd, ed)  
        sym = []
        sym.append(symbol)
        prices = ut.get_data(sym, dates)[sym]

        orders = prices.copy()
        orders[symbol] = 0.0

        currentHolding = 0.0
        index = 0
        for x in prices.index:
            if y[index] == 1:
                if currentHolding == 0.0:
                    orders[symbol][x] = 1000.0
                    currentHolding = 1000.0
                elif currentHolding == 1000.0:
                    orders[symbol][x] = 0.0
                    currentHolding = 1000.0
                elif currentHolding == -1000.0:
                    orders[symbol][x] = 2000.0
                    currentHolding = 1000.0
            elif y[index] == -1:
                if currentHolding == 0.0:
                    orders[symbol][x] = -1000.0
                    currentHolding = -1000.0
                elif currentHolding == 1000.0:
                    orders[symbol][x] = -2000.0
                    currentHolding = -1000.0
                elif currentHolding == -1000.0:
                    orders[symbol][x] = 0.0
                    currentHolding = -1000.0
            elif y[index] == 0:
                if currentHolding == 0.0:
                    orders[symbol][x] = 0.0
                    currentHolding = 0.0
                elif currentHolding == 1000.0:
                    orders[symbol][x] = -1000.0
                    currentHolding = 0.0
                elif currentHolding == -1000.0:
                    orders[symbol][x] = 1000
                    currentHolding = 0.0
            index += 1
        
        return orders
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    print("One does not simply think up a strategy")  		  	   		  		 			  		 			     			  	 
