import DistanciaEuclidiana as de
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

import numpy as np
from sklearn.datasets import load_iris, load_wine
from pandas import read_csv

from Cluster import Cluster
from SimulatedAnnealing import SimulatedAnnealing

iris = load_iris()

cluster = Cluster(X = iris['data'], k = 3, grupos = iris['target'])

cluster.GerarCentroide()

print(cluster.SSE())

cluster.GerarGrupos()
cluster.GerarCentroide()
print(cluster.SSE())

#exit()

data = iris['data']

k = 3

kmeans = KMeans(n_clusters = k, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(data)

#cluster.X = y_kmeans
cluster.grupos = kmeans.labels_
cluster.centroides = kmeans.cluster_centers_
print(cluster.SSE())


cluster = Cluster(X = iris['data'], k = 3)
cluster.GerarGrupos()
cluster.Shuffle()
sa = SimulatedAnnealing(
    state =  cluster, 
    t = 500, 
    alfa = 0.95,
    iter_max=500,
    max_time = 1)
print('Antes',cluster.SSE())
sa.Run()
print('Antes',cluster.SSE())
print('Depois',sa.solution.SSE())
#cluster.Show()
#sa.solution.Show()

#cluster.Show()

# plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'yellow', label = 'Centroids')

# plt.show()

# groups = {}
# for group in range(0,k):
#     groups[group] = { 
#         'centroide' : kmeans.cluster_centers_[group],
#         'X' : data[y_kmeans == group]
#     }

# print(de.SSE(groups))
# print(kmeans.inertia_)