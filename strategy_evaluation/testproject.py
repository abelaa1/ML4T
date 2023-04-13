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
    sym = "JPM"
    stv = 100000
    df_tradesBench = tos.benchMark(symbol = sym, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = stv)
    # ind_orders = ms.testPolicy(symbol = sym, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31))
    # portVal = msc.compute_portvals(ind_orders,sym,stv,commission=0.0,impact=0.0)

    # msc.test_code(ind_orders,df_tradesBench,sym,stv)
    df = sl.StrategyLearner(verbose=True)
    ord = df.testPolicy()




if __name__ == "__main__":
    test()