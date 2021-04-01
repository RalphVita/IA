
import time
from Training import Trainable
from Roleta import roulette_construction, roulette_run
from IState import IState

class HillClimbing(Trainable):
    def __init__(self, state : IState, numBest = 15, max_time = 1):
        Trainable.__init__(self, 'Hill Climbing')
        self.state = state 
        self.numBest = numBest
        self.max_time = max_time
        self.solution : IState = None

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

            best = sorted (possible_states, key = lambda x: x.Value())[:self.numBest]
            current_state = roulette_run (1, roulette_construction(best))[0]

            end = time.process_time()
            #Saida na convergencia
            if(self.solution.Equal(current_state)):
                break
        return self.solution

    def GenerateNeighborhood(self, state):
        neighborhood = []
        for i in range(self.numBest):
            new_state = state.ChangeState(i,1)
            neighborhood.append(new_state)
        for i in range(self.numBest):
            new_state = state.ChangeState(i,-1)
            neighborhood.append(new_state)
        return neighborhood
        # neighborhood = []
        # for i in range(2*self.numBest):
        #     neighborhood.append(state.NextState())
        
        # return neighborhood