import time
from HillClimbing import HillClimbing
from GradientDescent import GradientDescent
from Training import Trainable

class Grasp(Trainable):
    def __init__(self, state, numIter = 500, numBest = 15, max_time = 1):
        Trainable.__init__(self, 'Grasp')
        self.state = state 
        self.numIter = numIter 
        self.numBest = numBest
        self.max_time = max_time
        self.solution : Annealable = None

    def Run(self):
        optimal = self.state
        optimal_value = optimal.Value()
        start = time.process_time()
        end = 0
        iter = 0
        while iter < self.numIter and end-start <= self.max_time:
            iter += 1
            s =  HillClimbing(self.state, numBest=self.numBest, max_time=self.max_time/self.numIter).Run()
            s =  GradientDescent().Run(s, max_time = self.max_time/self.numIter)
            s_value = s.Value()
            if s_value < optimal_value:
                optimal = s
                optimal_value = s_value
            end = time.process_time()
        
        self.solution = optimal
        return self.solution
    
    