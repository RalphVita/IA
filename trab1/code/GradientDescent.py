import time

class GradientDescent:
    def Run(self, solution, max_time):
        start = time.process_time()
        min_value = solution.Value()
        neighborhood = self.generate_neighborhood(solution)
        better = True
        end = 0
        while better  and end-start <= max_time:
            better = False
            for s in neighborhood:
                value = s.Value()
                if value < min_value:
                    solution = s
                    min_value = value
                    better = True
            end = time.process_time()    
        return solution

    def generate_neighborhood(self, state):
        neighborhood = []
        for i in range(state.get_number_states()):
            new_state = state.ChangeState(i,1)
            neighborhood.append(new_state)
        for i in range(state.get_number_states()):
            new_state = state.ChangeState(i,-1)
            neighborhood.append(new_state)
        return neighborhood
