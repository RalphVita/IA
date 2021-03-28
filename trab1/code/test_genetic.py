import numpy as np
from sklearn.datasets import load_iris, load_wine
from pandas import read_csv

from Cluster import Cluster
from Genetic import Genetic

iris = load_iris()

cluster = Cluster(X = iris['data'], k = 3)

cluster.Shuffle()
genetic = Genetic(state =  cluster)
print('Antes',cluster.SSE())
genetic.Run()
print('Antes',genetic.solution.SSE())