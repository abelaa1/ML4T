""""""  		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
Test a learner.  (c) 2015 Tucker Balch  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
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
"""  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import math  		  	   		  		 			  		 			     			  	 
import sys  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import numpy as np  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import LinRegLearner as lrl  
import DTLearner as dt	
import RTLearner as rt	  
import BagLearner as bl 
import InsaneLearner as it  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    if len(sys.argv) != 2:  		  	   		  		 			  		 			     			  	 
        print("Usage: python testlearner.py <filename>")  		  	   		  		 			  		 			     			  	 
        sys.exit(1)  		  	   		  		 			  		 			     			  	 
    inf = open(sys.argv[1])  
    next(inf)		  	   		  		 			  		 			     			  	 
    data = np.array(  		  	   		  		 			  		 			     			  	 
        [list(map(float, s.split(",", 1)[1].strip().split(","))) for s in inf.readlines()]  		  	   		  		 			  		 			     			  	 
    )  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # compute how much of the data is training and testing  		  	   		  		 			  		 			     			  	 
    train_rows = int(0.6 * data.shape[0])  		  	   		  		 			  		 			     			  	 
    test_rows = data.shape[0] - train_rows  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # separate out training and testing data  		  	   		  		 			  		 			     			  	 
    train_x = data[:train_rows, 0:-1]  		  	   		  		 			  		 			     			  	 
    train_y = data[:train_rows, -1]  		  	   		  		 			  		 			     			  	 
    test_x = data[train_rows:, 0:-1]  		  	   		  		 			  		 			     			  	 
    test_y = data[train_rows:, -1]  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    print(f"{test_x.shape}")  		  	   		  		 			  		 			     			  	 
    print(f"{test_y.shape}")  	

    # #dtlearner
    # dtlearner = dt.DTLearner(leaf_size = 1, verbose = False) # constructor  
    # dtlearner.add_evidence(train_x, train_y)  # training step   
    # pred_y = dtlearner.query(train_x) 	  

    # #rtlearner
    # rtlearner = rt.RTLearner(leaf_size = 1, verbose = False) # constructor  
    # rtlearner.add_evidence(train_x, train_y)  # training step   
    # pred_y = rtlearner.query(train_x) 	 		 			  		 			     			  	 

    # #baglearner
    # baglearner = bl.BagLearner(learner = dt.DTLearner, kwargs = {"leaf_size":1}, bags = 20, boost = False, verbose = False) # constructor  
    # baglearner.add_evidence(train_x, train_y)  # training step   
    # pred_y = baglearner.query(train_x)                                    

    # #Insanelearner
    itlearner = it.InsaneLearner(verbose = False) # constructor  
    itlearner.add_evidence(train_x, train_y)  # training step   
    # pred_y = itlearner.query(train_x)  

    # # create a learner and train it  		  	   		  		 			  		 			     			  	 
    # learner = lrl.LinRegLearner(verbose=True)  # create a LinRegLearner  		  	   		  		 			  		 			     			  	 
    # learner.add_evidence(train_x, train_y)  # train it  		  	   		  		 			  		 			     			  	 
    # print(learner.author())  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # evaluate in sample  		  	   		  		 			  		 			     			  	 
    pred_y = itlearner.query(train_x)  # get the predictions  		  	   		  		 			  		 			     			  	 
    rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])  		  	   		  		 			  		 			     			  	 
    print()  		  	   		  		 			  		 			     			  	 
    print("In sample results")  		  	   		  		 			  		 			     			  	 
    print(f"RMSE: {rmse}")  		  	   		  		 			  		 			     			  	 
    c = np.corrcoef(pred_y, y=train_y)  		  	   		  		 			  		 			     			  	 
    print(f"corr: {c[0,1]}")  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # evaluate out of sample  		  	   		  		 			  		 			     			  	 
    pred_y = itlearner.query(test_x)  # get the predictions  		  	   		  		 			  		 			     			  	 
    rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])  		  	   		  		 			  		 			     			  	 
    print()  		  	   		  		 			  		 			     			  	 
    print("Out of sample results")  		  	   		  		 			  		 			     			  	 
    print(f"RMSE: {rmse}")  		  	   		  		 			  		 			     			  	 
    c = np.corrcoef(pred_y, y=test_y)  		  	   		  		 			  		 			     			  	 
    print(f"corr: {c[0,1]}")  		  	   		  		 			  		 			     			  	 
