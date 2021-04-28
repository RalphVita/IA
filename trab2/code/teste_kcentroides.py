from KCentroides import KCentroides
import numpy as np
import pandas as pd
from scipy import stats
from sklearn import datasets
from sklearn.cluster import KMeans
from Genetic import Genetic

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

kcent = KCentroides(Genetic)

kcent.k = 1

f = kcent.fit(iris_X,iris_y)

#print('--------------------')

#print(iris_y)

print(f)

print(kcent.predict(iris_X))
