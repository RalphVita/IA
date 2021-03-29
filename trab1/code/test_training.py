import numpy as np
from sklearn.datasets import load_iris, load_wine
import pandas as pd

from Cluster import Cluster
from SimulatedAnnealing import SimulatedAnnealing
from Genetic import Genetic
from Grasp import Grasp
from Training import Training
import CombineParameters as hParans
import time

start = time.process_time()

#Itera por quantidade de grupos pra cada problema
def Treinar(cluster, Ks):
    #Data frame de Resultados
    dfResult = pd.DataFrame()

    for k in Ks:#[3,7]:#[3, 7, 10, 13, 22]:
        print('K:',k)

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
        genetic.set_hyperparameters(hParans.pararansGe)

        #Grasp
        grasp = Grasp(state =  cluster)
        grasp.set_hyperparameters(hParans.pararansGr)

        #Cria Treino para as Metaheuristicas
        training = Training([sa,genetic,grasp])

        #Roda o treino
        training.Run()

        #Seta o número de grupos para as resultados desse treino
        training.result['K'] = k

        #Concatena com resultados anteriores
        dfResult = dfResult.append(training.result)

    return dfResult

#Data frame de Resultados
dfResultTotal = pd.DataFrame()

#Iris
print('Iris')
iris = load_iris()
clusterIris = Cluster(X = iris['data'], k = 3)
clusterIris.Shuffle()

dfResultIris = Treinar(clusterIris, [3, 7, 10, 13, 22])
dfResultIris['Problema'] = 'Iris'
dfResultTotal = dfResultTotal.append(dfResultIris)
dfResultIris.to_csv('./result/dfResultIris.csv')


#Wine
print('Wine')
wine = load_wine()
clusterwine = Cluster(X = wine['data'], k = 3)
clusterwine.Shuffle()

dfResultWine = Treinar(clusterwine, [2, 6, 9, 11, 33])
dfResultWine['Problema'] = 'Wine'
dfResultTotal = dfResultTotal.append(dfResultWine)
dfResultWine.to_csv('./result/dfResultWine.csv')

#Relatório de resultados
dfResultTotal.to_csv('./result/result.csv')
print(dfResultTotal)

print(time.process_time() - start)