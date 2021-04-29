import numpy as np
import random
from IState import IState
from sklearn.utils import shuffle

class Cluster(IState):
    def __init__(self, X, k, grupos = None,centroides = None):
        self.X = X
        self.grupos = grupos
        self.centroides = centroides
        self.k = k
        self.sse = 0
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
    
    def set_grupos(self, grupos):
        self.grupos =  grupos
        self.GerarCentroide()
    
    def GerarGrupos(self):
        length = len(self.X)
        repeat = int(length/self.k) + 1
        #self.grupos = np.random.randint(0,self.k,len(self.X))
        self.grupos =  np.array([_ for _ in range(self.k)]*repeat)[:length]
        #print(self.grupos)
        
        self.GerarCentroide()

    def GerarCentroide(self):
        self.centroides = np.array([sum(self.X[self.grupos == g])/len(self.X[self.grupos == g]) for g in self.get_grupos()])
        self.SSE()

    
    ####### Distancia Euclidia ##########
    def SomaDistanciaEuclidia(self, X, centroide):
        return sum([np.linalg.norm(x-centroide) for x in X])

    def SSE(self):
        self.sse = sum([self.SomaDistanciaEuclidia(self.X[self.grupos == g],self.centroides[g]) for g in self.get_grupos()])
        return self.sse

    def Show(self):
        print('Grupos:', self.grupos)
        print('Centroides:', self.centroides)
        print('Pontos:', self.X)

    ##### IState ######
    def Value(self):
        return self.sse

    def NextState(self):
        return self.Mutation()

    #Compara se os grupos de dois clusters são iguais
    def Equal(self, other):
        return np.array_equal(self.grupos, other.grupos)

    #IMutable methods
    def Crossover(self,other):
        r = random.randint(0, len(self.grupos) - 1)
        son = np.concatenate((self.grupos[:r], other.grupos[r:]), axis=0)
        daug = np.concatenate((other.grupos[:r], self.grupos[r:]), axis=0)


        #Se o número de grupos for menor que K cancela esse cruzamento
        if(len(np.unique(son)) < self.k):
            son = self.grupos
        if(len(np.unique(daug)) < self.k):
            daug = other.grupos
        son, daug = Cluster(X = self.X, k = self.k, grupos=son), Cluster(X = self.X, k = self.k, grupos=daug)



        return son, daug
    
    def get_number_states(self):
        return self.k
    
    def ChangeState(self, index, value):
        new_grupos = self.grupos.copy()

        old_value = new_grupos[index]
        new_value = old_value + value

        if(new_value < 0):
            new_grupos[index] = self.k-1
        elif new_value >= self.k:
            new_grupos[index] =  0
        else:
            new_grupos[index] = new_value
        
        #Verifica se continua com K grupos
        if len(np.unique(new_grupos)) < self.k:
            new_grupos[index] = old_value #Volta so estado anterior, mantendo K grupos

        return Cluster(
            X = self.X, 
            k = self.k, 
            grupos = new_grupos
        )


    def Mutation(self):
        new_grupos = self.grupos.copy()

        if(self.k > 1):#Se tiver só um grupo, não precisa fazer mutação
            index = random.randint(0, len(new_grupos)-1)
            while new_grupos[index] == self.grupos[index] or len(np.unique(new_grupos)) < self.k:
                index = random.randint(0, len(new_grupos)-1)
                new_grupos[index] = random.randint(0, self.k - 1)
        
        return Cluster(
            X = self.X, 
            k = self.k, 
            grupos = new_grupos
        ) 
