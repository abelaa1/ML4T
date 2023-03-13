import TheoreticallyOptimalStrategy as tos
import marketsimcode as ms

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
    df_trades = tos.testPolicy(symbol = sym, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = stv)
    df_tradesBench = tos.benchMark(symbol = sym, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = stv)

    # ms.test_code(df_trades,df_tradesBench,sym,stv)

    portValBest = ms.compute_portvals(df_trades,sym,stv,commission=0.0,impact=0.0)
    portValBench = ms.compute_portvals(df_tradesBench,sym,stv,commission=0.0,impact=0.0)

    portValBest = portValBest/portValBest[0]
    portValBench = portValBench/portValBench[0]
    portValBest.plot(color = 'r')
    portValBench.plot(color = 'purple')

    plt.legend(["Theoretically optimal portfolio", "Benchmark portfolio"])
    plt.title("Theoretically optimal portfolio vs Benchmark portfolio")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Amount")
    plt.savefig("images/figure1.png")


if __name__ == "__main__":
    test()