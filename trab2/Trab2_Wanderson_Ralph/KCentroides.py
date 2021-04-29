import numpy as np
from sklearn.base import BaseEstimator
from sklearn.utils.validation import check_X_y
from sklearn.cluster import KMeans
from Genetic import Genetic

class KCentroides(BaseEstimator):
    def __init__(self,algoritimo = 'KMeans', k=None):
        super().__init__()
        self.k = k
        self.algoritimo = algoritimo
    
    def fit(self,x_train,y_train):
        x_train,y_train = check_X_y(x_train,y_train)

        alg = KMeans(n_clusters = self.k) if self.algoritimo == 'KMeans' else Genetic(k= self.k)
        #print(self.k)

        self.__self_pred = []
        for classe in np.unique(y_train):
            alg.fit(x_train[y_train == classe])
            for centroide in  alg.cluster_centers_:
                self.__self_pred.append((centroide, classe))
        return self.__self_pred

    def predict(self,x_test):
        
        distancia = lambda a,b : np.linalg.norm(a-b)


        #Varre todos pontos e retorna a classe do centroide mais próximo a cada um
        return np.array([
            #Retorna a classe do centróide que está mais próximo do ponto
            min(
                [(distancia(ponto,centroide),classe) for (centroide,classe) in self.__self_pred], #Distancia do ponto e cada centroide calculado
                key = lambda dist_class: dist_class[0]#Compara pela distância
                )[1]# Retorna a classe
                    for ponto in x_test #Varre por todos pontos da matriz x_test
        ])
