import TheoreticallyOptimalStrategy as tos
import marketsimcode as msc
import indicators as ind
import ManualStrategy as ms
import StrategyLearner as sl

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

def test():
    np.random.seed(16)
    # sym = "SINE_FAST_NOISE"
    # sym = "AAPL"
    sym = "JPM"
    stv = 100000
    startD = dt.datetime(2008, 1, 1) #In
    endD = dt.datetime(2009,12,31) #In
    dates = pd.date_range(startD, endD) 

    # plot_data(get_data([sym],dates))

    startDO = dt.datetime(2010, 1, 1) #Out
    endDO = dt.datetime(2011,12,31) #Out

    df_tradesBench = tos.benchMark(symbol = sym, sd=startD, ed=endD, sv = stv)
    ind_orders = ms.testPolicy(symbol = sym, sd=startD, ed=endD)
    # portVal = msc.compute_portvals(ind_orders,sym,stv,commission=0.0,impact=0.0)

    msc.test_code(ind_orders,df_tradesBench,sym,stv)

    df = sl.StrategyLearner()
    df.add_evidence(sym,startD,endD,stv)
    rantree = df.testPolicy(sym,startD,endD,stv)
    msc.test_code(rantree,df_tradesBench,sym,stv)




if __name__ == "__main__":
    test()