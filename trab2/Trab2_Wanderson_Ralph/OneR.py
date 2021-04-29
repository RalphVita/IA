import numpy as np
from sklearn.base import BaseEstimator
from sklearn.utils.validation import check_X_y
from sklearn.preprocessing import KBinsDiscretizer
import pandas as pd

class OneR(BaseEstimator):
    
    def fit(self,x_train,y_train):
        x_train,y_train = check_X_y(x_train,y_train)

        self.n_classes = len(np.unique(y_train))
        
        #Discretiza
        est = KBinsDiscretizer(n_bins=2*self.n_classes, encode='ordinal', strategy='kmeans').fit(x_train)
        X_bin = est.transform(x_train)



        n_caracteristica = x_train.shape[1]
        
        self.classes = np.unique(y_train)

        #Pra cada caracteristica gera um matriz da associação [[caracteristica,valor, classe] ]
        datas = [[[caracteristica,valor, classe] for (valor, classe) in zip(X_bin[:,caracteristica],y_train)] for caracteristica in range(n_caracteristica)]

        #Lista de dataframes pivoteados
        dfs = []
        #Lista das dos maiores valores das caracteristicas por classes
        lst = []
        for data in datas:
            data = np.array(data)
            
            #Pivotei as matrizes usando pandas
            df = pd.DataFrame(data=data,columns=['caracteristica','valor', 'classe'])
            pivot = pd.pivot_table (df, values = "caracteristica", 
                                    index = "valor", columns = "classe", 
                                    aggfunc = "count")
            #Zera os valores nulos
            pivot = pivot.fillna(0)

            
            #Adiciona as listas
            lst.append((data[0][0],pivot.max().values))
            dfs.append(pivot)

        
        #Caracteristica que mais se destaca
        self.caracteristica = int(max(lst, key = lambda x: sum(x[1]))[0])


        #Tabela de contigencia da caracteristica que mais se destaca
        self.matriz = dfs[self.caracteristica]

    def predict(self,x_test):
        #Discretiza
        est = KBinsDiscretizer(n_bins=2*self.n_classes, encode='ordinal', strategy='kmeans').fit(x_test)
        X_bin = est.transform(x_test)


        result = []
        
        
        for X in X_bin:
            #As vezes esse valor caricteristica não foi usado no treino, mas existe no teste. Nesse caso a probabilidade é igual pra todas classes
            if X[self.caracteristica] in self.matriz.index:
                array = self.matriz.loc[X[self.caracteristica]]
                result.append(np.random.choice(self.classes,1,p=array/sum(array))[0])
            else:
                result.append(np.random.choice(self.classes,1)[0])
        return result