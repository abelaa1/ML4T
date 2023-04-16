import StrategyLearner as sl
import ManualStrategy as ms
import marketsimcode as msc

import matplotlib.pyplot as plt	
import datetime as dt  

def experimentTwo():
    sym = "JPM"
    stv = 100000
    startD = dt.datetime(2008, 1, 1) #In
    endD = dt.datetime(2009,12,31) #In

    # In Sample 0 impact
    df = sl.StrategyLearner(impact=0.0,commission=0.0)
    df.add_evidence(sym,startD,endD,stv)
    rantree = df.testPolicy(sym,startD,endD,stv)

    portVal_sta = msc.compute_portvals(rantree,sym,stv,commission=0.0,impact=0.0)
    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = msc.findPortStats(portVal_sta)	

    # print(f"Sharpe Ratio of Fund: {sharpe_ratio}")  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
    # print(f"Cumulative Return of Fund: {cum_ret}")  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
    # print(f"Standard Deviation of Fund: {std_daily_ret}")  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
    # print(f"Average Daily Return of Fund: {avg_daily_ret}")  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
    # print(f"Final Portfolio Value: {portVal_sta[-1]}")

    # In Sample High Impact
    df2 = sl.StrategyLearner(impact=0.015,commission=0.0)
    df2.add_evidence(sym,startD,endD,stv)
    rantree2 = df.testPolicy(sym,startD,endD,stv)

    portVal_sta2 = msc.compute_portvals(rantree2,sym,stv,commission=0.0,impact=0.015)
    cum_ret2, avg_daily_ret2, std_daily_ret2, sharpe_ratio2 = msc.findPortStats(portVal_sta2)

    # print(f"Sharpe Ratio of Fund: {sharpe_ratio2}")  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
    # print(f"Cumulative Return of Fund: {cum_ret2}")  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
    # print(f"Standard Deviation of Fund: {std_daily_ret2}")  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
    # print(f"Average Daily Return of Fund: {avg_daily_ret2}")  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
    # print(f"Final Portfolio Value: {portVal_sta2[-1]}")	

    # In Sample Crazy Impact
    df3 = sl.StrategyLearner(impact=0.03,commission=0.0)
    df3.add_evidence(sym,startD,endD,stv)
    rantree3 = df.testPolicy(sym,startD,endD,stv)

    portVal_sta3 = msc.compute_portvals(rantree3,sym,stv,commission=0.0,impact=0.03)
    cum_ret3, avg_daily_ret3, std_daily_ret3, sharpe_ratio3 = msc.findPortStats(portVal_sta3)	

    # print(f"Sharpe Ratio of Fund: {sharpe_ratio3}")  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
    # print(f"Cumulative Return of Fund: {cum_ret3}")  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
    # print(f"Standard Deviation of Fund: {std_daily_ret3}")  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
    # print(f"Average Daily Return of Fund: {avg_daily_ret3}")  		  	   		  		 			  		 			     			  	  		  	   		  		 			  		 			     			  	 
    # print(f"Final Portfolio Value: {portVal_sta3[-1]}")

    portVal_sta = portVal_sta/portVal_sta[0]
    portVal_sta2 = portVal_sta2/portVal_sta2[0]
    portVal_sta3 = portVal_sta3/portVal_sta3[0]
    portVal_sta.plot(color = 'r')
    portVal_sta2.plot(color = 'purple')
    portVal_sta3.plot(color = 'b')

    plt.legend(["0.0 Impact", "0.015 Impact", "0.03 Impact"])
    plt.title("JPM In Sample: Impact Affect On Trading")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Amount")
    plt.savefig("images/figure5.png")
    plt.clf()