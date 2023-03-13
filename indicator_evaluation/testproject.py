import TheoreticallyOptimalStrategy as tos
import marketsimcode as ms
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

def test():
    sym = "JPM"
    stv = 100000
    df_trades = tos.testPolicy(symbol = sym, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = stv)
    df_tradesBench = tos.benchMark(symbol = sym, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = stv)

    ms.test_code(df_trades,df_tradesBench,sym,stv)

    portValBest = ms.compute_portvals(df_trades,sym,stv,commission=0.0,impact=0.0)
    portValBench = ms.compute_portvals(df_tradesBench,sym,stv,commission=0.0,impact=0.0)

    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = ms.findPortStats(portValBest)	

    cum_ret_Bench, avg_daily_ret_Bench, std_daily_ret_Bench, sharpe_ratio_Bench = ms.findPortStats(portValBench)

    portValBest = portValBest/portValBest[0]
    portValBench = portValBench/portValBench[0]
    portValBest.plot(color = 'r')
    portValBench.plot(color = 'purple')

    plt.legend(["Theoretically optimal portfolio", "Benchmark portfolio"])
    plt.title("Theoretically optimal portfolio vs Benchmark portfolio")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Amount")
    plt.savefig("images/figure1.png")
    plt.clf()

    sma_orders = ind.SMA(symbol = sym, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31))
    portValSMA = ms.compute_portvals(sma_orders,sym,stv,commission=0.0,impact=0.0)
    plt.clf()

    ema_orders = ind.EMA(symbol = sym, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31))
    portValEMA = ms.compute_portvals(ema_orders,sym,stv,commission=0.0,impact=0.0)
    plt.clf()

    rsi_orders = ind.RSI(symbol = sym, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31))
    portValRSI = ms.compute_portvals(rsi_orders,sym,stv,commission=0.0,impact=0.0)
    plt.clf()

    roc_orders = ind.ROC(symbol = sym, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31))
    portValROC = ms.compute_portvals(roc_orders,sym,stv,commission=0.0,impact=0.0)
    plt.clf()

    tema_orders = ind.TEMA(symbol = sym, sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31))
    portValTEMA = ms.compute_portvals(tema_orders,sym,stv,commission=0.0,impact=0.0)
    plt.clf()

if __name__ == "__main__":
    test()