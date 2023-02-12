import numpy as np
from numpy import random as rn

class BagLearner(object):
    def __init__(self, learner, kwargs, bags = 20, boost = False, verbose = False):
        self.learner = learner
        self.kwargs = kwargs
        self.bags = bags
        self.boost = boost
        self.verbose = verbose
        self.learners = []  

    def author(self):
        return "aaguilar61"

    def add_evidence(self, data_x, data_y):
        for i in range(0,self.bags):  
            self.learners.append(self.learner(**self.kwargs)) 
        
        for learn in self.learners:
            traingDataX = np.empty((0, np.shape(data_x)[1]), float)
            traingDataY = np.empty((0, 1), float)
            for i in range(0,np.shape(data_x)[0]):
                rand = rn.randint(0, np.shape(data_x)[0]-1)
                traingDataX = np.vstack((traingDataX, data_x[rand]))
                traingDataY = np.append(traingDataY, data_y[rand])
            learn.add_evidence(traingDataX, traingDataY)

    def query(self, points):
        ansY = np.empty((np.shape(points)[0], 0), int)
        for learn in self.learners:
            pred_y = learn.query(points)
            ansY = np.column_stack((ansY,pred_y))

        return(np.mean(ansY, axis=1))