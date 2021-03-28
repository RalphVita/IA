import time
import pandas as pd
import numpy as np
from scipy.stats import zscore

class Trainable:
    #Recebe varias combinações de hyper parâmetros
    def __init__(self,name):
        self.hyperparameters = []
        self.n = 10
        self.name = name
        self.result = pd.DataFrame(columns=['Heuristica','Configuração','Média','Desvio Padrão','Tempo médio'])


    def set_hyperparameters(self,hyperparameters):
        self.hyperparameters = hyperparameters

    def Train(self):
        for parameters in self.hyperparameters:
            values = []
            times = []
            for _ in range(self.n):
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
    def __init__(self, problems):
        self.problems = problems 
        self.result = pd.DataFrame()
    
    def Run(self):
        for problem in self.problems:
            self.result = self.result.append(problem.Train())
        #self.result['z-score'] = self.result.groupby(['Heuristica'])['Média'].transform(lambda x : zscore(x))

        return self.result