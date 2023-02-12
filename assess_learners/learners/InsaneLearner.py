import BagLearner as bl 
import LinRegLearner as lrl  
class InsaneLearner(object):
    def __init__(self, verbose=False): self.verbose = verbose
    def author(self): return "aaguilar61"
    def add_evidence(self, data_x, data_y): 
        self.insaneLearn = bl.BagLearner(learner = bl.BagLearner, kwargs = {"learner":lrl.LinRegLearner, "kwargs":{}, "bags":20, "boost":False, "verbose":self.verbose}, bags = 20, boost = False, verbose = self.verbose) 
        self.insaneLearn.add_evidence(data_x,data_y)
    def query(self, points): return(self.insaneLearn.query(points))