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
        length = len(self.X)
        repeat = int(length/self.k) + 1
        #self.grupos = np.random.randint(0,self.k,len(self.X))
        self.grupos =  np.array([_ for _ in range(self.k)]*repeat)[:length]
        #print(self.grupos)
        
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
        return self.Mutation()

    #Compara se os grupos de dois clusters são iguais
    def Equal(self, other):
        return np.array_equal(self.grupos, other.grupos)

    #Mutable methods
    def Crossover(self,other):
        r = random.randint(0, len(self.grupos) - 1)
        son = np.concatenate((self.grupos[:r], other.grupos[r:]), axis=0)
        daug = np.concatenate((other.grupos[:r], self.grupos[r:]), axis=0)
        #son = self.grupos[:r]+other.grupos[r:]
        #daug = other.grupos[:r]+self.grupos[r:]

        son, daug = Cluster(X = self.X, k = self.k, grupos=son), Cluster(X = self.X, k = self.k, grupos=daug)

        #Se o número de grupos for menor que K, força mutar até ter K grupos
        while len(np.unique(son.grupos)) < self.k:
            son.Mutation()

        while len(np.unique(daug.grupos)) < self.k:
            daug.Mutation()

        return son, daug

    def Mutation(self):
        new_grupos = self.grupos.copy()

        index = random.randint(0, len(new_grupos)-1)
        while new_grupos[index] == self.grupos[index] or len(np.unique(new_grupos)) < self.k:
            index = random.randint(0, len(new_grupos)-1)
            new_grupos[index] = random.randint(0, self.k - 1)
        
        return Cluster(
            X = self.X, 
            k = self.k, 
            grupos = new_grupos
        ) 
        # individual = self.grupos
        # rand = random.randint(0, len(individual) - 1)
        # if individual[rand] > 0:
        #     r = random.uniform(0,1)
        #     if r > 0.5 and individual[rand] < self.k - 1:
        #         individual[rand] = individual[rand] + 1
        #     else:
        #         individual[rand] = individual[rand] - 1
        # else:
        #     individual[rand] = individual[rand] + 1
        
        # self.grupos = individual

        # #Se o número de grupos for menor que K, força mutar até ter K grupos
        # while len(np.unique(self.grupos)) < self.k:
        #     self.Mutation()

        # return self
        