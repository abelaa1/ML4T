""""""  		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
Template for implementing QLearner  (c) 2015 Tucker Balch  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
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
  		  	   		  		 			  		 			     			  	 
import random as rand  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import numpy as np  

def author():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    :return: The GT username of the student  		  	   		  		 			  		 			     			  	 
    :rtype: str  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    return "aaguilar61"
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
class QLearner(object):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    This is a Q learner object.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param num_states: The number of states to consider.  		  	   		  		 			  		 			     			  	 
    :type num_states: int  		  	   		  		 			  		 			     			  	 
    :param num_actions: The number of actions available..  		  	   		  		 			  		 			     			  	 
    :type num_actions: int  		  	   		  		 			  		 			     			  	 
    :param alpha: The learning rate used in the update rule. Should range between 0.0 and 1.0 with 0.2 as a typical value.  		  	   		  		 			  		 			     			  	 
    :type alpha: float  		  	   		  		 			  		 			     			  	 
    :param gamma: The discount rate used in the update rule. Should range between 0.0 and 1.0 with 0.9 as a typical value.  		  	   		  		 			  		 			     			  	 
    :type gamma: float  		  	   		  		 			  		 			     			  	 
    :param rar: Random action rate: the probability of selecting a random action at each step. Should range between 0.0 (no random actions) to 1.0 (always random action) with 0.5 as a typical value.  		  	   		  		 			  		 			     			  	 
    :type rar: float  		  	   		  		 			  		 			     			  	 
    :param radr: Random action decay rate, after each update, rar = rar * radr. Ranges between 0.0 (immediate decay to 0) and 1.0 (no decay). Typically 0.99.  		  	   		  		 			  		 			     			  	 
    :type radr: float  		  	   		  		 			  		 			     			  	 
    :param dyna: The number of dyna updates for each regular update. When Dyna is used, 200 is a typical value.  		  	   		  		 			  		 			     			  	 
    :type dyna: int  		  	   		  		 			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  		 			  		 			     			  	 
    :type verbose: bool  		  	   		  		 			  		 			     			  	 
    """  
    def author(self):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        :return: The GT username of the student  		  	   		  		 			  		 			     			  	 
        :rtype: str  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        return "aaguilar61"
		  	   		  		 			  		 			     			  	 
    def __init__(  		  	   		  		 			  		 			     			  	 
        self,  		  	   		  		 			  		 			     			  	 
        num_states=100,  		  	   		  		 			  		 			     			  	 
        num_actions=4,  		  	   		  		 			  		 			     			  	 
        alpha=0.2,  		  	   		  		 			  		 			     			  	 
        gamma=0.9,  		  	   		  		 			  		 			     			  	 
        rar=0.5,  		  	   		  		 			  		 			     			  	 
        radr=0.99,  		  	   		  		 			  		 			     			  	 
        dyna=0,  		  	   		  		 			  		 			     			  	 
        verbose=False,  		  	   		  		 			  		 			     			  	 
    ):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Constructor method  		  	   		  		 			  		 			     			  	 
        """  	
        self.visited = []  	
        self.visited_act = {}   		  		 			  		 			     			  	 
        self.verbose = verbose  		  	   		  		 			  		 			     			  	 
        self.num_actions = num_actions  
        self.num_states = num_states	  	   		  		 			  		 			     			  	 
        self.s = 0  		  	   		  		 			  		 			     			  	 
        self.a = 0  
        self.alpha = alpha
        self.gamma = gamma
        self.rar = rar
        self.radr = radr
        self.dyna = dyna
        self.Q_table = np.zeros((num_states, num_actions))

        if self.dyna != 0:
            self.T = np.zeros((num_states, num_actions, num_states))
            self.T_c = np.zeros((num_states, num_actions, num_states))
            self.T_c.fill(0.0001)
            self.R = np.zeros((num_states, num_actions))
        
    def querysetstate(self, s):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Update the state without updating the Q-table  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        :param s: The new state  		  	   		  		 			  		 			     			  	 
        :type s: int  		  	   		  		 			  		 			     			  	 
        :return: The selected action  		  	   		  		 			  		 			     			  	 
        :rtype: int  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        self.s = s  		  	   		  		 			  		 			     			  	 
        action = rand.randint(0, self.num_actions - 1)  		  	   		  		 			  		 			     			  	 
        if self.verbose:  		  	   		  		 			  		 			     			  	 
            print(f"s = {s}, a = {action}")  		  	   		  		 			  		 			     			  	 
        return action  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    def query(self, s_prime, r):  		  	   		  		 			  		 			     			  	 
        """  		  	   		  		 			  		 			     			  	 
        Update the Q table and return an action  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
        :param s_prime: The new state  		  	   		  		 			  		 			     			  	 
        :type s_prime: int  		  	   		  		 			  		 			     			  	 
        :param r: The immediate reward  		  	   		  		 			  		 			     			  	 
        :type r: float  		  	   		  		 			  		 			     			  	 
        :return: The selected action  		  	   		  		 			  		 			     			  	 
        :rtype: int  		  	   		  		 			  		 			     			  	 
        """  	
            
        self.Q_table[self.s][self.a] = (((1-self.alpha) * self.Q_table[self.s][self.a]) + self.alpha*(r + self.gamma * self.Q_table[s_prime][np.argmax(self.Q_table[s_prime])]))

        if np.random.uniform(0.0, 1.0) < self.rar:
            action = rand.randint(0, self.num_actions - 1)
        else:
            action = np.argmax(self.Q_table[s_prime,:])
        self.rar *= self.radr

        if self.dyna != 0:
            # creating dicts https://www.geeksforgeeks.org/python-ways-to-create-a-dictionary-of-lists/
            if self.s not in self.visited:
                self.visited.append(self.s)
                self.visited_act[self.s] = []
                self.visited_act[self.s].append(self.a)
            else:
                self.visited_act[self.s].append(self.a)

            self.T_c[self.s][self.a][s_prime] += 1
            self.T[self.s][self.a][s_prime] = self.T_c[self.s][self.a][s_prime]/np.sum(self.T_c[self.s][self.a])
            self.R[self.s][self.a] = (1-self.alpha) * self.R[self.s][self.a] + (self.alpha * r)

            for i in range(self.dyna):
                # random choice https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
                s_d = rand.choice(self.visited)
                a_d = rand.choice(self.visited_act[s_d])
                s_prime_d = np.argmax(self.T[s_d][a_d])
                r_d = self.R[s_d][a_d]

                self.Q_table[s_d][a_d] = (((1-self.alpha) * self.Q_table[s_d][a_d]) + self.alpha*(r_d + self.gamma * self.Q_table[s_prime_d][np.argmax(self.Q_table[s_prime_d])]))

        self.s = s_prime
        self.a = action
 		  	   		  		 			  		 			     			  	 
        if self.verbose:  		  	   		  		 			  		 			     			  	 
            print(f"s = {s_prime}, a = {action}, r={r}")  		  	   		  		 			  		 			     			  	 
        return action  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    print("Remember Q from Star Trek? Well, this isn't him")  		 

    # notes used https://www.omscs-notes.com/machine-learning-trading/q-learning/ 	   		  		 			  		 			     			  	 