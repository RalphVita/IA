
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
import TestarKmeans

start = time.process_time()


#Data frame de Resultados
dfResultTotal = pd.DataFrame()


### Melhores configurações ###
#Simulated Annealing 
hParans.pararansSA = [{'t': 100, 'alfa': 0.85, 'iter_max': 500, 'max_time': 1}]
#Genetic Algorithm
hParans.pararansGe = [{'pop_size': 10, 'cross_ratio': 0.75, 'mut_ratio': 0.2, 'max_time': 1}]
#Grasp
hParans.pararansGr = [{'numIter': 20, 'numBest': 5, 'max_time': 1}, {'numIter': 20, 'numBest': 15, 'max_time': 1}]


### Carrega  dados de teste
#Iris
print('Iris')
iris = load_iris()
clusterIris = Cluster(X = iris['data'], k = 3)
clusterIris.Shuffle()
k_iris = [2, 4, 8, 11, 15, 17, 23, 28, 32, 50]


#Wine
print('Wine')
wine = load_wine()
clusterwine = Cluster(X = wine['data'], k = 3)
clusterwine.Shuffle()
k_wine = [3, 5, 13, 15, 20, 23, 25, 30, 41, 45]


#Ionosphere
print('Ionosphere')
ionos = pd.read_csv('ionosphere.data',header=None)
ionosphere = np.asarray([i[:34] for i in ionos.values])
clusterionos = Cluster(X = ionosphere, k = 3)
clusterionos.Shuffle()
k_ionos = [2, 3, 5, 10, 15, 20, 25, 30, 40, 50]

##################################################
### TESTAR ###

dfResultIris = Avaliar(clusterIris, k_iris, hParans, 20)
dfResultIris['Base'] = 'Iris'
dfResultTotal = dfResultTotal.append(dfResultIris)
dfResultIris.to_csv('./result/dfTestartIris.csv')

dfResultWine = Avaliar(clusterwine, k_wine,hParans, 20)
dfResultWine['Base'] = 'Wine'
dfResultTotal = dfResultTotal.append(dfResultWine)
dfResultWine.to_csv('./result/dfTestarWine.csv')

dfResultIonos = Avaliar(clusterionos, k_ionos,hParans, 20)
dfResultIonos['Base'] = 'Ionosphere'
dfResultTotal = dfResultTotal.append(dfResultIonos)
dfResultIonos.to_csv('./result/dfTestarIonos.csv')

##################################################
## Testa o K-means ##

dfResultIris =TestarKmeans.Avaliar(clusterIris, k_iris, 20)
dfResultIris['Base'] = 'Iris'
dfResultTotal = dfResultTotal.append(dfResultIris)
#dfResultIris.to_csv('./result/dfTestartKmeansIris.csv')

dfResultWine = TestarKmeans.Avaliar(clusterwine, k_wine, 20)
dfResultWine['Base'] = 'Wine'
dfResultTotal = dfResultTotal.append(dfResultWine)
#dfResultWine.to_csv('./result/dfTestarKmeansWine.csv')

dfResultIonos = TestarKmeans.Avaliar(clusterionos, k_ionos, 20)
dfResultIonos['Base'] = 'Ionosphere'
dfResultTotal = dfResultTotal.append(dfResultIonos)
#dfResultIonos.to_csv('./result/dfTestarKmeansIonos.csv')

dfResultTotal.to_csv('./result/resultKmeansTeste.csv')
##################################################



#Relatório de resultados
dfResultTotal.to_csv('./result/resultTeste.csv')






# hParans.pararansGr = [{'numIter': 20, 'numBest': 15, 'max_time': 1}]

# dfResultIris = Avaliar(clusterIris, k_iris, hParans, 20)
# dfResultIris['Base'] = 'Iris'
# dfResultTotal = dfResultTotal.append(dfResultIris)
# dfResultIris.to_csv('./result/dfTestartIris_Grasp.csv')

# dfResultWine = Avaliar(clusterwine, k_wine,hParans, 20)
# dfResultWine['Base'] = 'Wine'
# dfResultTotal = dfResultTotal.append(dfResultWine)
# dfResultWine.to_csv('./result/dfTestarWine_Grasp.csv')

# dfResultIonos = Avaliar(clusterionos, k_ionos,hParans, 20)
# dfResultIonos['Base'] = 'Ionosphere'
# dfResultTotal = dfResultTotal.append(dfResultIonos)
# dfResultIonos.to_csv('./result/dfTestarIonos_Grasp.csv')

# dfResultTotal.to_csv('./result/resultTeste_Grasp.csv')

print(time.process_time() - start)