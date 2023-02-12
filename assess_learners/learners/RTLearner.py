import numpy as np
from numpy import random as rn

class RTLearner(object):
    def __init__(self, leaf_size = 1, verbose=False):
        self.leaf_size = leaf_size
        self.verbose = verbose

    def author(self):
        return "aaguilar61"

    def train(self,data_x, data_y):
        if data_x.shape[0] <= self.leaf_size:
            leafOne = np.array([[100, np.mean(data_y), 100, 100]])
            return(leafOne)
        elif np.all(data_y == data_y[0]):
            leafTwo = np.array([[100, data_y[0], 100, 100]])
            return(leafTwo)
        
        rand = rn.randint(0, np.shape(data_x)[1]-1)
        splitVal = np.median(data_x.T[rand])
        data = np.column_stack((data_x,data_y))
        left = data[data[:,rand]<=splitVal]
        right = data[data[:,rand]>splitVal]
        flagL = np.any(left)
        flagR = np.any(right)
        if flagL == False:
            return np.array([[100, np.mean(right[:, -1]), 100, 100]])
        elif flagR == False:
            return np.array([[100, np.mean(left[:, -1]), 100, 100]])
        lefttree = self.train(left[:, 0:-1],left[:, -1])
        righttree = self.train(right[:, 0:-1],right[:, -1])
        root = np.array([[rand, splitVal, 1, lefttree.shape[0] + 1]])
        temp1 = np.append(root, lefttree, axis=0)
        temp2 = np.append(temp1, righttree, axis=0)
        return (temp2)

    def add_evidence(self, data_x, data_y):
        self.rtModel = self.train(data_x,data_y)

    def query(self, points):
        ans = np.empty((0, 1), float)
        for row in points:
            factor = int(self.rtModel[0][0])
            current = 0
            while factor != 100:
                disVal = row[factor]
                if disVal <= self.rtModel[current][1]:
                    current = current + int(self.rtModel[current][2])
                elif disVal > self.rtModel[current][1]:
                    current = current + int(self.rtModel[current][3])
                factor = int(self.rtModel[current][0])
            new = self.rtModel[current][1]
            ans = np.append(ans, [new])
        return ans