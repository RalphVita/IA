
import time
from Training import Trainable

class Scalable:
    def Value(self):
        pass
    def GerarVizinho(self):
        pass
    def get_number_states(self):
        pass

class HillClimbing(Trainable):
    def __init__(self, state : Scalable, numBest = 15, max_time = 1):
        Trainable.__init__(self, 'Hill Climbing')
        self.state = state 
        self.numBest = numBest
        self.max_time = max_time
        self.solution : Annealable = None

    def Run(self):#max_size, items, max_time):
        start = time.process_time()
        current_state = self.state
        self.solution = current_state
        optimal_value = self.solution.Value()
        end = 0

        while end-start <= self.max_time:
            possible_states = self.GenerateNeighborhood(current_state)

            for state in possible_states:
                aux_val = state.Value()
                if aux_val < optimal_value:
                    optimal_value = aux_val
                    self.solution = state
                    current_state = state

            end = time.process_time()
            #Saida na convergencia
            #if(optimal_state.Equal())
        #self.solution = optimal_state
        return self.solution

    def GenerateNeighborhood(self, state):
        neighborhood = []
        for i in range(2*state.get_number_states()):
            neighborhood.append(state.GerarVizinho())
        
        return neighborhood