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


# all citiation for code used can be found in report

import math  		  	   		  		 			  		 			     			  	 
import sys  
import time		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import numpy as np
import matplotlib.pyplot as plt	  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import LinRegLearner as lrl  
import DTLearner as dt	
import RTLearner as rt	  
import BagLearner as bl 
import InsaneLearner as it  

def gtid():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    :return: The GT ID of the student  		  	   		  		 			  		 			     			  	 
    :rtype: int  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    return 903861561
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    if len(sys.argv) != 2:  		  	   		  		 			  		 			     			  	 
        print("Usage: python testlearner.py <filename>")  		  	   		  		 			  		 			     			  	 
        sys.exit(1)  		  	   		  		 			  		 			     			  	 
    inf = open(sys.argv[1])  
    next(inf)		  	   		  		 			  		 			     			  	 
    data = np.array(  		  	   		  		 			  		 			     			  	 
        [list(map(float, s.split(",", 1)[1].strip().split(","))) for s in inf.readlines()]  		  	   		  		 			  		 			     			  	 
    )  		  	   		  		 			  		 			     			  	 

    # data = np.array(  		  	   		  		 			  		 			     			  	 
    #     [list(map(float, s.strip().split(","))) for s in inf.readlines()]  		  	   		  		 			  		 			     			  	 
    # ) 

    # compute how much of the data is training and testing  		  	   		  		 			  		 			     			  	 
    # train_rows = int(0.6 * data.shape[0])  		  	   		  		 			  		 			     			  	 
    # test_rows = data.shape[0] - train_rows  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # separate out training and testing data  		  	   		  		 			  		 			     			  	 
    # train_x = data[:train_rows, 0:-1]  		  	   		  		 			  		 			     			  	 
    # train_y = data[:train_rows, -1]  		  	   		  		 			  		 			     			  	 
    # test_x = data[train_rows:, 0:-1]  		  	   		  		 			  		 			     			  	 
    # test_y = data[train_rows:, -1]  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    # print(f"{test_x.shape}")  		  	   		  		 			  		 			     			  	 
    # print(f"{train_x.shape}")  	

    #test leanrers

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
    # itlearner = it.InsaneLearner(verbose = False) # constructor  
    # itlearner.add_evidence(train_x, train_y)  # training step   
    # pred_y = itlearner.query(train_x)  

    # # create a learner and train it  		  	   		  		 			  		 			     			  	 
    # learner = lrl.LinRegLearner(verbose=True)  # create a LinRegLearner  		  	   		  		 			  		 			     			  	 
    # learner.add_evidence(train_x, train_y)  # train it  		  	   		  		 			  		 			     			  	 
    # print(learner.author())    
    
    np.random.seed(gtid())
    # Experiment One

    rmsePointsIn = np.empty((0, 2), float)
    rmsePointsOut = np.empty((0, 2), float)

    corPointsIn = np.empty((0, 2), float)
    corPointsOut = np.empty((0, 2), float)

    for i in range(1, 51):
        num = data.shape[0]
        random_indices = np.random.choice(num, size=num, replace=False)
        random_rows = data[random_indices, :]

        train_rows = int(0.6 * random_rows.shape[0])  		  	   		  		 			  		 			     			  	 
        test_rows = random_rows.shape[0] - train_rows  		  	   		  		 			  		 			     			  	 
                                                                                    		  	   		  		 			  		 			     			  	 
        train_x = random_rows[:train_rows, 0:-1]  		  	   		  		 			  		 			     			  	 
        train_y = random_rows[:train_rows, -1]  		  	   		  		 			  		 			     			  	 
        test_x = random_rows[train_rows:, 0:-1]  		  	   		  		 			  		 			     			  	 
        test_y = random_rows[train_rows:, -1]  


        dtlearner = dt.DTLearner(leaf_size = i, verbose = False) # constructor  
        dtlearner.add_evidence(train_x, train_y)  # training step  

        pred_y = dtlearner.query(train_x)  # get the predictions  		  	   		  		 			  		 			     			  	 
        rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
        rmsePointsIn = np.vstack((rmsePointsIn, [i,rmse]))
        c = np.corrcoef(pred_y, y=train_y)
        corPointsIn = np.vstack((corPointsIn, [i,c[0, 1]]))

        pred_y = dtlearner.query(test_x)  # get the predictions
        rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
        rmsePointsOut = np.vstack((rmsePointsOut, [i,rmse]))
        c = np.corrcoef(pred_y, y=test_y)
        corPointsOut = np.vstack((corPointsOut, [i,c[0, 1]]))

    x1, y1 = rmsePointsIn.T
    x2, y2 = rmsePointsOut.T

    plt.clf()
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.legend(["RMSE In Sample", "RMSE Out Sample"])
    plt.title("DTLearner: RMSE In Sample vs Out Sample")
    plt.xlabel("Leaf Size")
    plt.ylabel("RMSE")
    plt.savefig("images/figure1.png")

    x3, y3 = corPointsIn.T
    x4, y4 = corPointsOut.T

    plt.clf()
    plt.plot(x3,y3)
    plt.plot(x4,y4)
    plt.legend(["Correlation In Sample", "Correlation Out Sample"])
    plt.title("DTLearner: Correlation In Sample vs Out Sample")
    plt.xlabel("Leaf Size")
    plt.ylabel("Correlation")
    plt.savefig("images/figure2.png")


    # Experiment Two

    rmsePointsIn2 = np.empty((0, 2), float)
    rmsePointsOut2 = np.empty((0, 2), float)

    corPointsIn2 = np.empty((0, 2), float)
    corPointsOut2 = np.empty((0, 2), float)

    for i in range(1, 51):
        num = data.shape[0]
        random_indices = np.random.choice(num, size=num, replace=False)
        random_rows = data[random_indices, :]

        train_rows = int(0.6 * random_rows.shape[0])  		  	   		  		 			  		 			     			  	 
        test_rows = random_rows.shape[0] - train_rows  		  	   		  		 			  		 			     			  	 
                                                                                    		  	   		  		 			  		 			     			  	 
        train_x = random_rows[:train_rows, 0:-1]  		  	   		  		 			  		 			     			  	 
        train_y = random_rows[:train_rows, -1]  		  	   		  		 			  		 			     			  	 
        test_x = random_rows[train_rows:, 0:-1]  		  	   		  		 			  		 			     			  	 
        test_y = random_rows[train_rows:, -1]  


        baglearner = bl.BagLearner(learner = dt.DTLearner, kwargs = {"leaf_size":i}, bags = 20, boost = False, verbose = False) # constructor  
        baglearner.add_evidence(train_x, train_y)  # training step   

        pred_y = baglearner.query(train_x)  # get the predictions  		  	   		  		 			  		 			     			  	 
        rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
        rmsePointsIn2 = np.vstack((rmsePointsIn2, [i,rmse]))
        c = np.corrcoef(pred_y, y=train_y)
        corPointsIn2 = np.vstack((corPointsIn2, [i,c[0, 1]]))

        pred_y = baglearner.query(test_x)  # get the predictions
        rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
        rmsePointsOut2 = np.vstack((rmsePointsOut2, [i,rmse]))
        c = np.corrcoef(pred_y, y=test_y)
        corPointsOut2 = np.vstack((corPointsOut2, [i,c[0, 1]]))

    x5, y5 = rmsePointsIn2.T
    x6, y6 = rmsePointsOut2.T

    plt.clf()
    plt.plot(x5,y5)
    plt.plot(x6,y6)
    plt.legend(["RMSE In Sample", "RMSE Out Sample"])
    plt.title("BagLearner: RMSE In Sample vs Out Sample")
    plt.xlabel("Leaf Size")
    plt.ylabel("RMSE")
    plt.savefig("images/figure3.png")

    x7, y7 = corPointsIn2.T
    x8, y8 = corPointsOut2.T

    plt.clf()
    plt.plot(x7,y7)
    plt.plot(x8,y8)
    plt.legend(["Correlation In Sample", "Correlation Out Sample"])
    plt.title("BagLearner: Correlation In Sample vs Out Sample")
    plt.xlabel("Leaf Size")
    plt.ylabel("Correlation")
    plt.savefig("images/figure4.png")


    # Experiment Three

    maePointsInDT = np.empty((0, 2), float)
    maePointsOutDT = np.empty((0, 2), float)

    maePointsInRT = np.empty((0, 2), float)
    maePointsOutRT = np.empty((0, 2), float)

    DTtimeTrain = np.empty((0, 2), float)
    RTtimeTrain = np.empty((0, 2), float)

    DTtimeQuery = np.empty((0, 2), float)
    RTtimeQuery = np.empty((0, 2), float)

    for i in range(1, 51):
        num = data.shape[0]
        random_indices = np.random.choice(num, size=num, replace=False)
        random_rows = data[random_indices, :]

        train_rows = int(0.6 * random_rows.shape[0])  		  	   		  		 			  		 			     			  	 
        test_rows = random_rows.shape[0] - train_rows  		  	   		  		 			  		 			     			  	 
                                                                                    		  	   		  		 			  		 			     			  	 
        train_x = random_rows[:train_rows, 0:-1]  		  	   		  		 			  		 			     			  	 
        train_y = random_rows[:train_rows, -1]  		  	   		  		 			  		 			     			  	 
        test_x = random_rows[train_rows:, 0:-1]  		  	   		  		 			  		 			     			  	 
        test_y = random_rows[train_rows:, -1]  

        startDTT = time.time()
        dtlearner = dt.DTLearner(leaf_size = i, verbose = False) # constructor  
        dtlearner.add_evidence(train_x, train_y)  # training step  
        endDTT = time.time()
        DTtimeTrain = np.vstack((DTtimeTrain, [i,startDTT-endDTT]))

        startRTT = time.time()
        rtlearner = rt.RTLearner(leaf_size = i, verbose = False) # constructor  
        rtlearner.add_evidence(train_x, train_y)  # training step 
        endRTT = time.time()
        RTtimeTrain = np.vstack((RTtimeTrain, [i,startRTT-endRTT]))

        pred_y = dtlearner.query(train_x)  # get the predictions 	  	   		  		 			  		 			     			  	 
        mae = (abs(train_y - pred_y).sum()) / train_y.shape[0]
        maePointsInDT = np.vstack((maePointsInDT, [i,mae]))

        startDTQ = time.time()
        pred_y = dtlearner.query(test_x)  # get the predictions 
        endDTQ = time.time()	
        DTtimeQuery = np.vstack((DTtimeQuery, [i,startDTQ-endDTQ]))  	   		  		 			  		 			     			  	 
        mae = (abs(test_y - pred_y).sum()) / test_y.shape[0]
        maePointsOutDT = np.vstack((maePointsOutDT, [i,mae]))

        pred_y = rtlearner.query(train_x)  # get the predictions  		  	   		  		 			  		 			     			  	 
        mae = (abs(train_y - pred_y).sum()) / train_y.shape[0]
        maePointsInRT = np.vstack((maePointsInRT, [i,mae]))

        startRTQ = time.time()
        pred_y = rtlearner.query(test_x)  # get the predictions 
        endRTQ = time.time()	
        RTtimeQuery = np.vstack((RTtimeQuery, [i,startRTQ-endRTQ]))   		  	   		  		 			  		 			     			  	 
        mae = (abs(test_y - pred_y).sum()) / test_y.shape[0]
        maePointsOutRT = np.vstack((maePointsOutRT, [i,mae]))

    x9, y9 = maePointsInDT.T
    x10, y10 = maePointsOutDT.T

    plt.clf()
    plt.plot(x9,y9)
    plt.plot(x10,y10)
    plt.legend(["MAE In Sample", "MAE Out Sample"])
    plt.title("DTLearner: MAE In Sample vs Out Sample")
    plt.xlabel("Leaf Size")
    plt.ylabel("MAE")
    plt.savefig("images/figure5.png")

    x11, y11 = maePointsInRT.T
    x12, y12 = maePointsOutRT.T

    plt.clf()
    plt.plot(x11,y11)
    plt.plot(x12,y12)
    plt.legend(["MAE In Sample", "MAE Out Sample"])
    plt.title("RTLearner: MAE In Sample vs Out Sample")
    plt.xlabel("Leaf Size")
    plt.ylabel("MAE")
    plt.savefig("images/figure6.png")

    x13, y13 = DTtimeTrain.T
    x14, y14 = RTtimeTrain.T

    plt.clf()
    plt.plot(x13,y13)
    plt.plot(x14,y14)
    plt.legend(["DT Time to Train", "RT Time to Train"])
    plt.title("DT vs RT Time to Train")
    plt.xlabel("Leaf Size")
    plt.ylabel("Train Time")
    plt.savefig("images/figure7.png")

    x15, y15 = DTtimeQuery.T
    x16, y16 = RTtimeQuery.T

    plt.clf()
    plt.plot(x15,y15)
    plt.plot(x16,y16)
    plt.legend(["DT Time to Query", "RT Time to Query"])
    plt.title("DT vs RT Time to Query")
    plt.xlabel("Leaf Size")
    plt.ylabel("Query Time")
    plt.savefig("images/figure8.png")