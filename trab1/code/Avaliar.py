import numpy as np
from sklearn.datasets import load_iris, load_wine
import pandas as pd

from Cluster import Cluster
from SimulatedAnnealing import SimulatedAnnealing
from Genetic import Genetic
from Grasp import Grasp
from Training import Training
import CombineParameters as hParans

#Itera por quantidade de grupos pra cada problema
def Avaliar(cluster, Ks, hParans = hParans, n_vezes = 10):
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
        training = Training([sa,genetic,grasp], n_vezes)

        #Roda o treino
        training.Run()

        #Seta o número de grupos para as resultados desse treino
        training.result['K'] = k

        #Concatena com resultados anteriores
        dfResult = dfResult.append(training.result)

    return dfResult