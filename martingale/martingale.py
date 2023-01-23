""""""  		  	   		  		 			  		 			     			  	 
"""Assess a betting strategy.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
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
  		  	   		  		 			  		 			     			  	 
import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt	
from scipy.stats import binom	  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def author():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    :return: The GT username of the student  		  	   		  		 			  		 			     			  	 
    :rtype: str  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    return "aaguilar61"  # replace tb34 with your Georgia Tech username.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def gtid():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    :return: The GT ID of the student  		  	   		  		 			  		 			     			  	 
    :rtype: int  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    return 903861561  # replace with your GT ID number  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def get_spin_result(win_prob):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param win_prob: The probability of winning  		  	   		  		 			  		 			     			  	 
    :type win_prob: float  		  	   		  		 			  		 			     			  	 
    :return: The result of the spin.  		  	   		  		 			  		 			     			  	 
    :rtype: bool  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    result = False  		  	   		  		 			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		  		 			  		 			     			  	 
        result = True  		  	   		  		 			  		 			     			  	 
    return result  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 

def getNParrayOne(episodeNum, prob):
    arr = np.empty([episodeNum,1001], dtype=int)
    for x in range(episodeNum):
        episode_winning = 0
        bet_amount = 1
        for y in range(1001):
            arr[x][y] = episode_winning
            if episode_winning < 80:
                won = get_spin_result(prob)
                if won:
                    episode_winning += bet_amount
                    bet_amount = 1
                else:
                    episode_winning -= bet_amount
                    bet_amount *= 2
    return arr

def getNParrayTwo(episodeNum, prob):
    arr = np.empty([episodeNum,1001], dtype=int)
    for x in range(episodeNum):
        episode_winning = 0
        bet_amount = 1
        for y in range(1001):
            arr[x][y] = episode_winning
            if episode_winning < 80 and episode_winning > -256:
                won = get_spin_result(prob)
                if won:
                    episode_winning += bet_amount
                    bet_amount = 1
                else:
                    episode_winning -= bet_amount
                    bet_amount *= 2
                    if bet_amount > (episode_winning+256):
                        bet_amount = episode_winning+256
    return arr

def test_code():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Method to test your code  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    win_prob = 0.474  # set appropriately to the probability of a win  		  	   		  		 			  		 			     			  	 
    np.random.seed(gtid())  # do this only once  		  	   		  		 			  		 			     			  	 
    # Experiment 1 10 episodes
    plt.clf()
    arr = getNParrayOne(10,win_prob)
    df = pd.DataFrame(arr).T
    df.plot() 
    plt.legend(["Episode 1", "Episode 2", "Episode 3", "Episode 4", "Episode 5", "Episode 6", "Episode 7", "Episode 8", "Episode 9", "Episode 10"])
    plt.title("Figure#1 10 Episodes Unlimted Bank Roll")
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.xlim([0,300])
    plt.ylim([-256,250])
    plt.savefig("images/figure1.png")	#code was taken from https://www.geeksforgeeks.org/matplotlib-pyplot-savefig-in-python/  proper citaion in p1_martingale_report.pdf		  		 			     			  	 
    
    #Experiment 1 1000 episodes mean
    plt.clf()
    arr = getNParrayOne(1000,win_prob)
    df = pd.DataFrame(arr).mean()
    dfstd = pd.DataFrame(arr).std()
    upper_band = df + dfstd
    lower_band = df - dfstd
    upper_band.plot()
    lower_band.plot()
    df.plot() 
    plt.legend(["Mean Plus STD", "Mean Minus STD", "Mean"])
    plt.title("Figure#2 1000 Episodes Unlimted Bank Roll - Mean")
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.xlim([0,300])
    plt.ylim([-256,250])
    plt.savefig("images/figure2.png")	 
    #used to find STD maxs and mins
    max1 = np.max(upper_band)
    min1 = np.min(lower_band)
    # print(min1)
    # print(max1)
    #used to find if all episodes ended in 80
    # print(arr[:, -1])

    #code was taken from https://www.geeksforgeeks.org/python-binomial-distribution/  proper citaion in p1_martingale_report.pdf
    plt.clf()
    n = 1000
    p = 0.474
    r_values = list(range(n + 1))
    dist = [binom.pmf(r, n, p) for r in r_values ]
    # used to find probabilty of at least 80 wins happen
    tot_prob = 0
    for i in range(80 + 1):
        tot_prob += dist[i]
    # print(tot_prob)
    plt.title("Figure BD Probability of winning X spins")
    plt.xlabel("Spins")
    plt.ylabel("Probability")
    plt.fill_between(r_values[81:1001], dist[81:1001] ,color='blue',alpha=0.2)
    plt.plot(r_values, dist)
    plt.savefig("images/BinomialDistributionUnlimitedBank.png")

    #Experiment 1 1000 episodes median
    plt.clf()
    arr = getNParrayOne(1000,win_prob)
    df = pd.DataFrame(arr).median()
    dfstd = pd.DataFrame(arr).std()
    upper_band = df + dfstd
    lower_band = df - dfstd
    upper_band.plot()
    lower_band.plot()
    df.plot() 
    plt.legend(["Median Plus STD", "Median Minus STD", "Median"])
    plt.title("Figure#3 1000 Episodes Unlimted Bank Roll - Median")
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.xlim([0,300])
    plt.ylim([-256,250])
    plt.savefig("images/figure3.png")	 


    #Experiment 2 1000 episodes mean
    plt.clf()
    arr = getNParrayTwo(1000,win_prob)
    df = pd.DataFrame(arr).mean()
    dfstd = pd.DataFrame(arr).std()
    upper_band = df + dfstd
    lower_band = df - dfstd
    upper_band.plot()
    lower_band.plot()
    df.plot() 
    plt.legend(["Mean Plus STD", "Mean Minus STD", "Mean"])
    plt.title("Figure#4 1000 Episodes $256 Bank Roll - Mean")
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.xlim([0,300])
    plt.ylim([-256,250])
    plt.savefig("images/figure4.png")	

    # used to find experiemental odds of winning 80 or losing 256
    count = 0
    fail = 0
    for x in arr[:, -1]:
        if x == 80:
            count += 1
        elif x == -256:
            fail += 1
    # print(count) 
    # print(fail)
    # used to find expected menan
    # arr1 = np.mean(arr[:, -1])
    #used to find STD maxs and mins
    max1 = np.max(upper_band)
    min1 = np.min(lower_band)
    # print(max1)
    # print(min1)

    #Experiment 2 1000 episodes median
    plt.clf()
    arr = getNParrayTwo(1000,win_prob)
    df = pd.DataFrame(arr).median()
    dfstd = pd.DataFrame(arr).std()
    upper_band = df + dfstd
    lower_band = df - dfstd
    upper_band.plot()
    lower_band.plot()
    df.plot() 
    plt.legend(["Median Plus STD", "Median Minus STD", "Median"])
    plt.title("Figure#5 1000 Episodes $256 Bank Roll - Median")
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.xlim([0,300])
    plt.ylim([-256,250])
    plt.savefig("images/figure5.png")	 		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    test_code()  		  	   		  		 			  		 			     			  	 
