import time
import math
import random

class Annealable:
    def Value(self):
        pass
    def GerarVizinho(self):# -> Annealable:
        pass

class SimulatedAnnealing:
    def __init__(self, state : Annealable,t,alfa,iter_max,max_time):
        self.state = state 
        self.t = t 
        self.alfa = alfa
        self.iter_max = iter_max
        self.max_time = max_time
        self.solution : Annealable = None


    def Run(self):
        self.solution = self.state
        max_value = self.solution.Value()

        start = time.process_time()
        end = 0
        t = self.t
        cont = 0

        while t >= 1:
            for _ in range(self.iter_max):
                vizinho = self.solution.GerarVizinho()
                if vizinho == None:
                    return self.solution
                
                vizinho_v = vizinho.Value()
                solution_v = self.solution.Value()

                if vizinho_v < solution_v or self.change_probability(vizinho_v,solution_v,t):
                    self.solution = vizinho

                cont = cont+1

                end = time.process_time()
                if(end-start > self.max_time):
                    print('Iterações:',cont)
                    return self.solution
            
            t = t*self.alfa
            
        
        print('Iterações:',cont)
        return self.solution
              
  
    # Probabilidade de aceitar mudança para pior estado
    def change_probability(self,value,best_value,t):
        p = 1/(math.exp((best_value-value)/t))
        r = random.uniform(0,1)
        if r < p:
            #print(best_value,value,t)
            return True
        else:
            return False