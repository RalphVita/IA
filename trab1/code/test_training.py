import numpy as np
from sklearn.datasets import load_iris, load_wine
import pandas as pd

from Cluster import Cluster
from SimulatedAnnealing import SimulatedAnnealing
from Training import Training

iris = load_iris()

pararans = []
for t in [500, 100, 50]:
    for alfa in [0.95, 0.85, 0.7]:
        for iter_max in [350, 500]:
            pararans.append({
                't': t, 
                'alfa': alfa,
                'iter_max': iter_max,
                'max_time': 1
            })

cluster = Cluster(X = iris['data'], k = 3)
cluster.Shuffle()

dfResult = pd.DataFrame()
for k in [3, 7, 10, 13, 22]:
    cluster.set_k(k)
    print('Antes',cluster.SSE())
    sa = SimulatedAnnealing(state =  cluster)

    sa.set_hyperparameters(pararans)

    training = Training([sa])

    training.Run()
    training.result['K'] = k
    dfResult = dfResult.append(training.result)

dfResult.to_csv('result.csv')
print(dfResult)