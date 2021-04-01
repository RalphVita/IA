import time
import math
import random
from Training import Trainable
from IState import IState
from Metaheuristica import Metaheuristica

class SimulatedAnnealing(Metaheuristica,Trainable):
    def __init__(self, state : IState,t = 500,alfa=0.95,iter_max = 500, max_time = 1):
        Trainable.__init__(self, 'Simulated Annealing')
        Metaheuristica.__init__(self,state)
        self.t = t 
        self.alfa = alfa
        self.iter_max = iter_max
        self.max_time = max_time
        self.solution : IState = None


    def Run(self):
        #Solução temporaria = Melhor solução geral até agora = estado inicial
        solution = self.solution = self.state
        max_value = solution.Value()

        start = time.process_time()
        end = 0
        t = self.t
        cont = 0

        while t >= 1:
            for _ in range(self.iter_max):
                vizinho = solution.NextState()
                if vizinho == None:
                    return self.solution
                
                vizinho_v = vizinho.Value()
                solution_v = solution.Value()

                if vizinho_v < solution_v or self.change_probability(vizinho_v,solution_v,t):
                    solution = vizinho
                    #Se melhor que a melhor solução geral até agora
                    if vizinho_v < self.solution.Value():
                        self.solution = vizinho

                cont = cont+1

                end = time.process_time()
                if(end-start > self.max_time):
                    print('Iterações:',cont)
                    return self.solution
            
            t = t*self.alfa
            
        
        print('Iterações:',cont)
        return self.solution

    def Execute(self, parameters):# -> (float):
        self.t = parameters['t'] 
        self.alfa = parameters['alfa']
        self.iter_max = parameters['iter_max']
        self.max_time = parameters['max_time']
        
        return self.Run().Value()
  
    # Probabilidade de aceitar mudança para pior estado
    def change_probability(self,value,best_value,t):
        p = 1/(math.exp((best_value-value)/t))
        r = random.uniform(0,1)
        if r < p:
            #print(best_value,value,t)
            return True
        else:
            return False