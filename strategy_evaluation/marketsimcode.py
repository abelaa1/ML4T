""""""  		  	   		  		 			  		 			     			  	 
"""MC2-P1: Market simulator.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
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

def findPortStats(portval):
    sf = 252
    rfr = 0.0

    port_val = portval		  	   		  		 			  		 			     			  	 

    daily_returns = port_val.copy()
    daily_returns = (port_val / port_val.shift(1)) - 1           

    daily_returns = daily_returns[1:]
    cum_ret = (port_val[-1]/port_val[0] - 1)
    avg_daily_ret = daily_returns.mean()
    std_daily_ret = daily_returns.std() 

    SR = m.sqrt(sf) * (avg_daily_ret - rfr) / std_daily_ret 

    cr, adr, sddr, sr = [  		  	   		  		 			  		 			     			  	 
        cum_ret,  		  	   		  		 			  		 			     			  	 
        avg_daily_ret,  		  	   		  		 			  		 			     			  	 
        std_daily_ret,  		  	   		  		 			  		 			     			  	 
        SR,  		  	   		  		 			  		 			     			  	 
    ] 

    return cr, adr, sddr, sr

def compute_portvals(  		  	   		  		 			  		 			     			  	 
    orders_file, 
    symbol, 		  	   		  		 			  		 			     			  	 
    start_val=1000000,  		  	   		  		 			  		 			     			  	 
    commission=9.95,  		  	   		  		 			  		 			     			  	 
    impact=0.005,  		  	   		  		 			  		 			     			  	 
):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Computes the portfolio values.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param orders_file: Path of the order file or the file object  		  	   		  		 			  		 			     			  	 
    :type orders_file: str or file object  		  	   		  		 			  		 			     			  	 
    :param start_val: The starting value of the portfolio  		  	   		  		 			  		 			     			  	 
    :type start_val: int  		  	   		  		 			  		 			     			  	 
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		  		 			  		 			     			  	 
    :type commission: float  		  	   		  		 			  		 			     			  	 
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		  		 			  		 			     			  	 
    :type impact: float  		  	   		  		 			  		 			     			  	 
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.
    :rtype: pandas.DataFrame  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 		
    sym = []
    sym.append(symbol)
    dates = pd.date_range(orders_file.first_valid_index(), orders_file.last_valid_index())  		  	   		  		 			  		 			     			  	 
    prices_all = get_data(sym, dates)  # automatically adds SPY  	
    prices_all.fillna(method="ffill", inplace=True)
    prices_all.fillna(method="bfill", inplace=True)	
    prices_all = prices_all.dropna()	  		 			     			  	 
    prices = prices_all[sym]  # only portfolio symbols 
    # https://www.interviewqs.com/ddi-code-snippets/add-new-col-df-default-value
    # setting a new default value for cash
    prices['Cash'] = 1.0

    # https://www.w3schools.com/python/pandas/ref_df_copy.asp
    # coping dataframe
    trades = prices.copy()
    trades[symbol] = 0.0
    trades['Cash'] = 0.0

    # https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
    # iterate over prices dataframe
    for x in trades.index:
        # https://www.geeksforgeeks.org/check-if-a-value-exists-in-a-dataframe-using-in-not-in-operator-in-python-pandas/
        # check if index exists in orders
        if orders_file[symbol][x] < 0:
            trades[symbol][x] = orders_file[symbol][x]
            trades['Cash'][x] = trades['Cash'][x] - (float(trades[symbol][x]) * (prices[symbol][x] * (1.0-impact))) - float(commission)
        elif orders_file[symbol][x] > 0:
            trades[symbol][x] = orders_file[symbol][x]
            trades['Cash'][x] = trades['Cash'][x] - (float(trades[symbol][x]) * (prices[symbol][x] * (1.0+impact))) - float(commission)

    yest = {}
    for s in sym:
        yest[s] = 0.0
    yest['Cash'] = float(start_val)

    holding = trades.copy()
    for x in holding:
        holding[x] = 0.0

    for i in holding.index:
        for s in sym:
            holding[s][i] = trades[s][i] + yest[s]
            yest[s] = trades[s][i] + yest[s]
        holding['Cash'][i] = trades['Cash'][i] + yest['Cash']
        yest['Cash'] = trades['Cash'][i] + yest['Cash']
    
    values = prices * holding
    portvals = np.sum(values, axis=1)
		 			  		 			     			  	 
    return portvals  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def test_code(  		  	   		  		 			  		 			     			  	 
    ordersBest,
    ordersBench, 
    symbol, 		  	   		  		 			  		 			     			  	 
    start_val=1000000,		  	   		  		 			  		 			     			  	 
):   		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Helper function to test code  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    # this is a helper function you can use to test your code  		  	   		  		 			  		 			     			  	 
    # note that during autograding his function will not be called.  		  	   		  		 			  		 			     			  	 
    # Define input parameters  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    of = ordersBest 		  	
    ofb = ordersBench   		  		 			  		 			     			  	 
    sv = start_val		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # Process orders  		  	   		  		 			  		 			     			  	 
    portvals = compute_portvals(orders_file=of, symbol=symbol, start_val=sv, commission=0.0, impact=0.0)  		  	   		  		 			  		 			     			  	 
    if isinstance(portvals, pd.DataFrame):  		  	   		  		 			  		 			     			  	 
        portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		  		 			  		 			     			  	 
    else:  		  	   		  		 			  		 			     			  	 
        "warning, code did not return a DataFrame"  


    portvalsBench = compute_portvals(orders_file=ofb, symbol=symbol, start_val=sv, commission=0.0, impact=0.0)  		  	   		  		 			  		 			     			  	 
    if isinstance(portvalsBench, pd.DataFrame):  		  	   		  		 			  		 			     			  	 
        portvalsBench = portvalsBench[portvalsBench.columns[0]]  # just get the first column  		  	   		  		 			  		 			     			  	 
    else:  		  	   		  		 			  		 			     			  	 
        "warning, code did not return a DataFrame"  	  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # Get portfolio stats
    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = findPortStats(portvals)	

    cum_ret_Bench, avg_daily_ret_Bench, std_daily_ret_Bench, sharpe_ratio_Bench = findPortStats(portvalsBench)


    # Compare portfolio against $SPX  		  	   		  		 			  		 			     			  	 
    print(f"Date Range: {portvals.first_valid_index()} to {portvals.last_valid_index()}")  		  	   		  		 			  		 			     			  	 
    print()  		  	   		  		 			  		 			     			  	 
    print(f"Sharpe Ratio of Fund: {sharpe_ratio}")  		  	   		  		 			  		 			     			  	 
    print(f"Sharpe Ratio of Benchmark : {sharpe_ratio_Bench}")  		  	   		  		 			  		 			     			  	 
    print()  		  	   		  		 			  		 			     			  	 
    print(f"Cumulative Return of Fund: {cum_ret}")  		  	   		  		 			  		 			     			  	 
    print(f"Cumulative Return of Benchmark : {cum_ret_Bench}")  		  	   		  		 			  		 			     			  	 
    print()  		  	   		  		 			  		 			     			  	 
    print(f"Standard Deviation of Fund: {std_daily_ret}")  		  	   		  		 			  		 			     			  	 
    print(f"Standard Deviation of Benchmark : {std_daily_ret_Bench}")  		  	   		  		 			  		 			     			  	 
    print()  		  	   		  		 			  		 			     			  	 
    print(f"Average Daily Return of Fund: {avg_daily_ret}")  		  	   		  		 			  		 			     			  	 
    print(f"Average Daily Return of Benchmark : {avg_daily_ret_Bench}")  		  	   		  		 			  		 			     			  	 
    print()  		  	   		  		 			  		 			     			  	 
    print(f"Final Portfolio Value: {portvals[-1]}")
    print(f"Final Portfolio Value: Benchmark : {portvalsBench[-1]}")