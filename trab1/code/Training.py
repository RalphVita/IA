import time
import pandas as pd
import numpy as np
from scipy.stats import zscore

class Trainable:
    #Recebe varias combinações de hyper parâmetros
    def __init__(self,name):
        self.hyperparameters = []
        self.name = name
        self.result = pd.DataFrame(columns=['Heuristica','Configuração','Média','Desvio Padrão','Tempo médio'])


    def set_hyperparameters(self,hyperparameters):
        self.hyperparameters = hyperparameters

    def Train(self, n = 10):
        print(self.name)
        for parameters in self.hyperparameters:
            values = []
            times = []
            for _ in range(n):
                start = time.process_time()

                #Executa memtaheuristica
                values.append(self.Execute(parameters))

                end = time.process_time()
                times.append(end - start)
            
            self.result = self.result.append(
                {
                    'Heuristica': self.name,
                    'Configuração': str(parameters),
                    'Média': np.mean(values),
                    'Desvio Padrão': np.std(values),
                    'Tempo médio': np.mean(times)
                },
                 ignore_index=True)
        
        return self.result
        

            
    def Execute(self,parameters) -> (float):
        pass


class Training:
    def __init__(self, problems, n_vezes = 10):
        self.problems = problems 
        self.n_vezes = n_vezes
        self.result = pd.DataFrame()
    
    def Run(self):
        for problem in self.problems:
            self.result = self.result.append(problem.Train(self.n_vezes))

        return self.result