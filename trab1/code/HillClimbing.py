
import time

class Scalable:
    def Value(self):
        pass
    def GenerateStates(self):
        pass

class HillClimbing(Trainable):
    def __init__(self, state : Scalable,t = 500,alfa=0.95,iter_max = 500, max_time = 1):
        Trainable.__init__(self, 'Simulated Annealing')
        self.state = state 
        self.t = t 
        self.alfa = alfa
        self.iter_max = iter_max
        self.max_time = max_time
        self.solution : Annealable = None

def Run(self):#max_size, items, max_time):
    start = time.process_time()
    current_state = self.state
    self.solution = current_state
    optimal_value = self.solution.Value()
    end = 0

    while end-start <= max_time:
        possible_states = current_state.GenerateStates()

        for state in possible_states:
            aux_val = state.Value()
            if aux_val < optimal_value:
                optimal_value = aux_val
                optimal_state = state
                current_state = state

        end = time.process_time()
        #TODO saida na convergencia
        #if(optimal_value == )

    return optimal_state, optimal_size, optimal_value
