import marketsimcode as msc
import indicators as ind
import ManualStrategy as ms
import StrategyLearner as sl
import experiment1 as ex1
import experiment2 as ex2

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
    sym = "JPM"
    stv = 100000
    startD = dt.datetime(2008, 1, 1) #In
    endD = dt.datetime(2009,12,31) #In

    startDO = dt.datetime(2010, 1, 1) #Out
    endDO = dt.datetime(2011,12,31) #Out

    # In Sample
    df_tradesBench = ms.benchMark(symbol = sym, sd=startD, ed=endD, sv = stv)
    ind_orders = ms.testPolicy(symbol = sym, sd=startD, ed=endD)
    portVal_benchmark = msc.compute_portvals(df_tradesBench,sym,stv,commission=9.95,impact=0.005)
    portVal_ind = msc.compute_portvals(ind_orders,sym,stv,commission=9.95,impact=0.005)

    portVal_ind = portVal_ind/portVal_ind[0]
    portVal_benchmark = portVal_benchmark/portVal_benchmark[0]
    portVal_ind.plot(color = 'r')
    portVal_benchmark.plot(color = 'purple')

    current = 0.0
    for date in ind_orders.index:
        if ind_orders[sym][date] == 1000.0:
            if current == 0.0:
                plt.axvline(date, color = 'b')
            current += 1000.0
        elif ind_orders[sym][date] == -1000.0:
            if current == 0.0:
                plt.axvline(date, color = 'k')
            current -= 1000.0

    plt.legend(["Manual Strategy", "Benchmark"])
    plt.title("JPM In Sample: Manual Strategy vs Benchmark portfolio")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Amount")
    plt.savefig("images/figure1.png")
    plt.clf()

    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = msc.findPortStats(portVal_ind)	
    cum_ret_Bench, avg_daily_ret_Bench, std_daily_ret_Bench, sharpe_ratio_Bench = msc.findPortStats(portVal_benchmark)

    # print(f"Sharpe Ratio of Fund: {sharpe_ratio}")  		  	   		  		 			  		 			     			  	 
    # print(f"Sharpe Ratio of Benchmark : {sharpe_ratio_Bench}")  		  	   		  		 			  		 			     			  	 
    # print()  		  	   		  		 			  		 			     			  	 
    # print(f"Cumulative Return of Fund: {cum_ret}")  		  	   		  		 			  		 			     			  	 
    # print(f"Cumulative Return of Benchmark : {cum_ret_Bench}")  		  	   		  		 			  		 			     			  	 
    # print()  		  	   		  		 			  		 			     			  	 
    # print(f"Standard Deviation of Fund: {std_daily_ret}")  		  	   		  		 			  		 			     			  	 
    # print(f"Standard Deviation of Benchmark : {std_daily_ret_Bench}")  		  	   		  		 			  		 			     			  	 
    # print()  		  	   		  		 			  		 			     			  	 
    # print(f"Average Daily Return of Fund: {avg_daily_ret}")  		  	   		  		 			  		 			     			  	 
    # print(f"Average Daily Return of Benchmark : {avg_daily_ret_Bench}")  		  	   		  		 			  		 			     			  	 
    # print()  		  	   		  		 			  		 			     			  	 
    # print(f"Final Portfolio Value: {portVal_ind[-1]}")
    # print(f"Final Portfolio Value: Benchmark : {portVal_benchmark[-1]}")


    # Out of Sample
    df_tradesBenchOut = ms.benchMark(symbol = sym, sd=startDO, ed=endDO, sv = stv)
    ind_ordersOut = ms.testPolicy(symbol = sym, sd=startDO, ed=endDO)
    portVal_benchmarkOut = msc.compute_portvals(df_tradesBenchOut,sym,stv,commission=9.95,impact=0.005)
    portVal_indOut = msc.compute_portvals(ind_ordersOut,sym,stv,commission=9.95,impact=0.005)

    portVal_indOut = portVal_indOut/portVal_indOut[0]
    portVal_benchmarkOut = portVal_benchmarkOut/portVal_benchmarkOut[0]
    portVal_indOut.plot(color = 'r')
    portVal_benchmarkOut.plot(color = 'purple')

    current = 0.0
    for date in ind_ordersOut.index:
        if ind_ordersOut[sym][date] == 1000.0:
            if current == 0.0:
                plt.axvline(date, color = 'b')
            current += 1000.0
        elif ind_ordersOut[sym][date] == -1000.0:
            if current == 0.0:
                plt.axvline(date, color = 'k')
            current -= 1000.0

    plt.legend(["Manual Strategy", "Benchmark"])
    plt.title("JPM Out of Sample: Manual Strategy vs Benchmark portfolio")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Amount")
    plt.savefig("images/figure2.png")
    plt.clf()

    cum_retOut, avg_daily_retOut, std_daily_retOut, sharpe_ratioOut = msc.findPortStats(portVal_ind)	
    cum_ret_BenchOut, avg_daily_ret_BenchOut, std_daily_ret_BenchOut, sharpe_ratio_BenchOut = msc.findPortStats(portVal_benchmark)

    # print(f"Sharpe Ratio of Fund: {sharpe_ratioOut}")  		  	   		  		 			  		 			     			  	 
    # print(f"Sharpe Ratio of Benchmark : {sharpe_ratio_BenchOut}")  		  	   		  		 			  		 			     			  	 
    # print()  		  	   		  		 			  		 			     			  	 
    # print(f"Cumulative Return of Fund: {cum_retOut}")  		  	   		  		 			  		 			     			  	 
    # print(f"Cumulative Return of Benchmark : {cum_ret_BenchOut}")  		  	   		  		 			  		 			     			  	 
    # print()  		  	   		  		 			  		 			     			  	 
    # print(f"Standard Deviation of Fund: {std_daily_retOut}")  		  	   		  		 			  		 			     			  	 
    # print(f"Standard Deviation of Benchmark : {std_daily_ret_BenchOut}")  		  	   		  		 			  		 			     			  	 
    # print()  		  	   		  		 			  		 			     			  	 
    # print(f"Average Daily Return of Fund: {avg_daily_retOut}")  		  	   		  		 			  		 			     			  	 
    # print(f"Average Daily Return of Benchmark : {avg_daily_ret_BenchOut}")  		  	   		  		 			  		 			     			  	 
    # print()  		  	   		  		 			  		 			     			  	 
    # print(f"Final Portfolio Value: {portVal_indOut[-1]}")
    # print(f"Final Portfolio Value: Benchmark : {portVal_benchmarkOut[-1]}")

    # Experiment One
    ex1.experimentOne()

    # Experiment Two
    ex2.experimentTwo()


if __name__ == "__main__":
    test()