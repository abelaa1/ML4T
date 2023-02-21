""""""  		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
template for generating data to fool learners (c) 2016 Tucker Balch  		  	   		  		 			  		 			     			  	 
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
  		  	   		  		 			  		 			     			  	 
import math  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import numpy as np  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
# this function should return a dataset (X and Y) that will work  		  	   		  		 			  		 			     			  	 
# better for linear regression than decision trees  		  	   		  		 			  		 			     			  	 
def best_4_lin_reg(seed=1489683273):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Returns data that performs significantly better with LinRegLearner than DTLearner.  		  	   		  		 			  		 			     			  	 
    The data set should include from 2 to 10 columns in X, and one column in Y.  		  	   		  		 			  		 			     			  	 
    The data should contain from 10 (minimum) to 1000 (maximum) rows.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param seed: The random seed for your data generation.  		  	   		  		 			  		 			     			  	 
    :type seed: int  		  	   		  		 			  		 			     			  	 
    :return: Returns data that performs significantly better with LinRegLearner than DTLearner.  		  	   		  		 			  		 			     			  	 
    :rtype: numpy.ndarray  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    np.random.seed(seed)  		  	   		  		 			  		 			     			  	 
    x = np.random.random(size=(100, 7)) * 200 - 100 
    y = np.sum(x,axis=1)		   		  		 			  		 			     			  	 	  	   		  		 			  		 			     			  	 
    return x, y  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def best_4_dt(seed=1489683273):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Returns data that performs significantly better with DTLearner than LinRegLearner.  		  	   		  		 			  		 			     			  	 
    The data set should include from 2 to 10 columns in X, and one column in Y.  		  	   		  		 			  		 			     			  	 
    The data should contain from 10 (minimum) to 1000 (maximum) rows.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param seed: The random seed for your data generation.  		  	   		  		 			  		 			     			  	 
    :type seed: int  		  	   		  		 			  		 			     			  	 
    :return: Returns data that performs significantly better with DTLearner than LinRegLearner.  		  	   		  		 			  		 			     			  	 
    :rtype: numpy.ndarray  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    np.random.seed(seed)  		  	   		  		 			  		 			     			  	 
    x = np.random.random(size=(100, 3)) * 100
    y = np.zeros((100, ), dtype = float)  # https://www.geeksforgeeks.org/numpy-zeros-python/ 
    
    for i in range(len(x)):
        pos = 0
        # https://stackoverflow.com/questions/36759106/number-of-levels-in-binary-tree-given-the-list-of-datas#:~:text=For%20complete%20or%20full%20binary,tree%20depends%20only%20on%20n%20.
        # to determine how many levels in a binaray tree
        for j in range(1 + math.floor(math.log2(len(x[i])))): # https://www.freecodecamp.org/news/how-to-round-numbers-up-or-down-in-python/
            if(pos < len(x[i])):
                if(x[i][pos] >= 80):
                    pos = pos*2 + 1
                else:
                    pos = pos*2 + 2
        y[i] = pos - 3

    return x, y  		

def author():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    :return: The GT username of the student  		  	   		  		 			  		 			     			  	 
    :rtype: str  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    return "aaguilar61"  # Change this to your user ID  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    print("they call me Tim.")  		  	   		  		 			  		 			     			  	 
