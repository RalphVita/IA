from sklearn.cluster import KMeans


import numpy as np
from sklearn.datasets import load_iris, load_wine
from pandas import read_csv

from Cluster import Cluster
from SimulatedAnnealing import SimulatedAnnealing
import time



def Avaliar(cluster, Ks, hParans = hParans, n_vezes = 10):
    #Data frame de Resultados
    dfResult = pd.DataFrame(columns=['Heuristica','Configuração','Média','Desvio Padrão','Tempo médio'])
    print(cluster.SSE())

    for k in Ks:
        print('K:',k)

        values = []
        times = []
        for i in range(n_vezes):
            kmeans = KMeans(n_clusters = k)

            start = time.process_time()

            #Executa
            y_kmeans = kmeans.fit_predict(cluster.X)

            end = time.process_time()
            times.append(end - start)

            #cluster.X = y_kmeans
            cluster.grupos = kmeans.labels_
            cluster.centroides = kmeans.cluster_centers_
            print(cluster.SSE())
            values.append(cluster.SSE())


        result = self.result.append(
        {
            'Heuristica': 'K-means',
            'Configuração': '-',
            'Média': np.mean(values),
            'Desvio Padrão': np.std(values),
            'Tempo médio': np.mean(times)
        },
            ignore_index=True)

        result.result['K'] = k

            
            



        