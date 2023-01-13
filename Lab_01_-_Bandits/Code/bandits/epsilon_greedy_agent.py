'''
Created on 14 Jan 2022

@author: ucacsjj
'''

import numpy as np

from .agent import Agent

class EpsilonGreedyAgent(Agent):
    
    def __init__(self, environment, epsilon):
        super().__init__(environment)
        self._epsilon = epsilon

    # Q5a:
    # Change the implementation to use the epsilon greedy algorithm
    def _choose_action(self):
        action = 0
        action_space = self._environment.action_space
        p = np.random.random()
        if p < self._epsilon:
            # explore
            action = action_space.sample()
        else:
            # exploit
            # get the current max
            # NOTE: IDK
            max_action, _ = self._environment.optimal_action()
            action = max_action

        return action
            
        
