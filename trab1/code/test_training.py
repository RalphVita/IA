import numpy as np
from sklearn.datasets import load_iris, load_wine
import pandas as pd

from Cluster import Cluster
from SimulatedAnnealing import SimulatedAnnealing
from Genetic import Genetic
from Training import Training
import CombineParameters as hParans

iris = load_iris()

#Inicializa problema
cluster = Cluster(X = iris['data'], k = 3)
cluster.Shuffle()

#Data frame de Resultados
dfResult = pd.DataFrame()

#Itera por quantidade de grupos pra cada problema
for k in [3, 7, 10, 13, 22]:

    #Seta quantidade de grupos
    cluster.set_k(k)

    #Gera um estado inicial, para nova quantidade de grupos
    cluster.GerarGrupos()

    print('Antes',cluster.SSE())

    #Simulated Annealing
    sa = SimulatedAnnealing(state =  cluster)
    sa.set_hyperparameters(hParans.pararansSA)

    #Genético
    genetic = Genetic(state =  cluster)
    genetic.set_hyperparameters(hParans.pararansG)

    #Cria Treino para as Metaheuristicas
    training = Training([sa])

    #Roda o treino
    training.Run()

    #Seta o número de grupos para as resultados desse treino
    training.result['K'] = k

    #Concatena com resultados anteriores
    dfResult = dfResult.append(training.result)

#Relatório de resultados
dfResult.to_csv('result.csv')
print(dfResult)