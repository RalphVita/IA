import numpy as np
import random
from SimulatedAnnealing import Annealable
from sklearn.utils import shuffle

class Cluster(Annealable):
    def __init__(self, X, k, grupos = None,centroides = None):
        self.X = X
        self.grupos = grupos
        self.centroides = centroides
        self.k = k
        if grupos is not None:
            self.GerarCentroide()
        else:
            self.GerarGrupos()

    def Shuffle(self):
        self.X, self.grupos = shuffle(self.X, self.grupos)
        self.GerarCentroide()

    def set_k(self,k):
        self.k = k

    def get_grupos(self):
        return np.arange(0,self.k)
    
    def GerarGrupos(self):
        self.grupos = np.random.randint(0,self.k,len(self.X))
        self.GerarCentroide()

    def GerarCentroide(self):
        self.centroides = np.array([sum(self.X[self.grupos == g])/len(self.X[self.grupos == g]) for g in self.get_grupos()])

    
    ####### Distancia Euclidia ##########
    def SomaDistanciaEuclidia(self, X, centroide):
        return sum([np.linalg.norm(x-centroide) for x in X])

    def SSE(self):
        return sum([self.SomaDistanciaEuclidia(self.X[self.grupos == g],self.centroides[g]) for g in self.get_grupos()])

    def Show(self):
        print('Grupos:', self.grupos)
        print('Centroides:', self.centroides)
        print('Pontos:', self.X)

    ##### Annealable ######
    def Value(self):
        return self.SSE()

    def GerarVizinho(self):
        new_grupos = self.grupos.copy()

        index = random.randint(0, len(new_grupos)-1)
        while new_grupos[index] == self.grupos[index] or len(np.unique(new_grupos)) < self.k:
            new_grupos[index] = random.randint(0, self.k - 1)

        #print(index,self.grupos[index],new_grupos[index])
        return Cluster(
            X = self.X, 
            k = self.k, 
            grupos = new_grupos
        )
        