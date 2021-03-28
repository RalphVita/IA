import numpy as np
from sklearn.datasets import load_iris, load_wine
from pandas import read_csv

from Cluster import Cluster
from Grasp import Grasp

iris = load_iris()

cluster = Cluster(X = iris['data'], k = 3)
cluster.Shuffle()

grasp = Grasp(state =  cluster)

print('Antes',cluster.SSE())
#for _ in range(10):
 
grasp.Run()
print('Antes',grasp.solution.SSE())