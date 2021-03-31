import numpy as np
from sklearn.datasets import load_iris, load_wine
import pandas as pd

from Cluster import Cluster
from SimulatedAnnealing import SimulatedAnnealing
from Genetic import Genetic
from Grasp import Grasp
from Training import Training
import CombineParameters as hParans

from Avaliar import Avaliar

import time

start = time.process_time()

#Data frame de Resultados
dfResultTotal = pd.DataFrame()

#Iris
print('Iris')
iris = load_iris()
clusterIris = Cluster(X = iris['data'], k = 3)
clusterIris.Shuffle()

dfResultIris = Avaliar(clusterIris, [3, 7, 10, 13, 22])
dfResultIris['Problema'] = 'Iris'
dfResultTotal = dfResultTotal.append(dfResultIris)
dfResultIris.to_csv('./result/dfResultIris.csv')


#Wine
print('Wine')
wine = load_wine()
clusterwine = Cluster(X = wine['data'], k = 3)
clusterwine.Shuffle()

dfResultWine = Avaliar(clusterwine, [2, 6, 9, 11, 33])
dfResultWine['Problema'] = 'Wine'
dfResultTotal = dfResultTotal.append(dfResultWine)
dfResultWine.to_csv('./result/dfResultWine.csv')

#Relatório de resultados
dfResultTotal.to_csv('./result/result.csv')
print(dfResultTotal)

print(time.process_time() - start)