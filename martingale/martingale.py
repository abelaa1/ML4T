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
    arr = getNParrayOne(10,win_prob)
    df = pd.DataFrame(arr).T
    df.plot() 
    plt.xlim([0,300])
    plt.ylim([-256,160])
    plt.show()		 			  		 			     			  	 
    
    #Experiment 1 1000 episodes mean
    arr = getNParrayOne(1000,win_prob)
    df = pd.DataFrame(arr).mean()
    dfstd = pd.DataFrame(arr).std()
    upper_band = df + dfstd
    lower_band = df - dfstd
    upper_band.plot()
    lower_band.plot()
    df.plot() 
    plt.xlim([0,300])
    plt.ylim([-256,160])
    plt.show() 	

    #Experiment 1 1000 episodes median
    arr = getNParrayOne(1000,win_prob)
    df = pd.DataFrame(arr).median()
    dfstd = pd.DataFrame(arr).std()
    upper_band = df + dfstd
    lower_band = df - dfstd
    upper_band.plot()
    lower_band.plot()
    df.plot() 
    plt.xlim([0,300])
    plt.ylim([-256,160])
    plt.show()


    #Experiment 2 1000 episodes mean
    arr = getNParrayTwo(1000,win_prob)
    df = pd.DataFrame(arr).mean()
    dfstd = pd.DataFrame(arr).std()
    upper_band = df + dfstd
    lower_band = df - dfstd
    upper_band.plot()
    lower_band.plot()
    df.plot() 
    plt.xlim([0,300])
    plt.ylim([-256,200])
    plt.show() 	

    #Experiment 2 1000 episodes median
    arr = getNParrayTwo(1000,win_prob)
    df = pd.DataFrame(arr).median()
    dfstd = pd.DataFrame(arr).std()
    upper_band = df + dfstd
    lower_band = df - dfstd
    upper_band.plot()
    lower_band.plot()
    df.plot() 
    plt.xlim([0,300])
    plt.ylim([-256,300])
    plt.show() 	 		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    test_code()  		  	   		  		 			  		 			     			  	 
