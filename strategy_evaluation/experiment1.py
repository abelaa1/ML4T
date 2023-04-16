import StrategyLearner as sl
import ManualStrategy as ms
import marketsimcode as msc

import matplotlib.pyplot as plt	
import datetime as dt  

def experimentOne():
    sym = "JPM"
    stv = 100000
    startD = dt.datetime(2008, 1, 1) #In
    endD = dt.datetime(2009,12,31) #In

    startDO = dt.datetime(2010, 1, 1) #Out
    endDO = dt.datetime(2011,12,31) #Out
    
    # In Sample
    df = sl.StrategyLearner(impact=0.005,commission=9.95)
    df.add_evidence(sym,startD,endD,stv)
    rantree = df.testPolicy(sym,startD,endD,stv)
    df_tradesBench = ms.benchMark(symbol = sym, sd=startD, ed=endD, sv = stv)
    ind_orders = ms.testPolicy(symbol = sym, sd=startD, ed=endD)

    portVal_benchmark = msc.compute_portvals(df_tradesBench,sym,stv,commission=9.95,impact=0.005)
    portVal_ind = msc.compute_portvals(ind_orders,sym,stv,commission=9.95,impact=0.005)
    portVal_sta = msc.compute_portvals(rantree,sym,stv,commission=9.95,impact=0.005)

    portVal_ind = portVal_ind/portVal_ind[0]
    portVal_benchmark = portVal_benchmark/portVal_benchmark[0]
    portVal_sta = portVal_sta/portVal_sta[0]
    portVal_ind.plot(color = 'r')
    portVal_benchmark.plot(color = 'purple')
    portVal_sta.plot(color = 'b')

    plt.legend(["Manual Strategy", "Benchmark", "Strategy Learner"])
    plt.title("JPM In Sample: Manual vs Benchmark portfolio vs Strategy Learner")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Amount")
    plt.savefig("images/figure3.png")
    plt.clf()

    # Out of Sample
    dfOut = sl.StrategyLearner(impact=0.005,commission=9.95)
    dfOut.add_evidence(sym,startD,endD,stv)
    rantreeOut = df.testPolicy(sym,startDO,endDO,stv)
    df_tradesBenchOut = ms.benchMark(symbol = sym, sd=startDO, ed=endDO, sv = stv)
    ind_ordersOut = ms.testPolicy(symbol = sym, sd=startDO, ed=endDO)

    portVal_benchmarkOut = msc.compute_portvals(df_tradesBenchOut,sym,stv,commission=9.95,impact=0.005)
    portVal_indOut = msc.compute_portvals(ind_ordersOut,sym,stv,commission=9.95,impact=0.005)
    portVal_staOut = msc.compute_portvals(rantreeOut,sym,stv,commission=9.95,impact=0.005)

    portVal_indOut = portVal_indOut/portVal_indOut[0]
    portVal_benchmarkOut = portVal_benchmarkOut/portVal_benchmarkOut[0]
    portVal_staOut = portVal_staOut/portVal_staOut[0]
    portVal_indOut.plot(color = 'r')
    portVal_benchmarkOut.plot(color = 'purple')
    portVal_staOut.plot(color = 'b')

    plt.legend(["Manual Strategy", "Benchmark", "Strategy Learner"])
    plt.title("JPM Out of Sample: Manual vs Benchmark portfolio vs Strategy Learner")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Amount")
    plt.savefig("images/figure4.png")
    plt.clf()