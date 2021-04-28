import numpy as np
import pandas as pd
from scipy import stats
from sklearn import datasets
from sklearn.model_selection import cross_val_predict 
from sklearn.dummy import DummyClassifier
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score, GridSearchCV, RepeatedStratifiedKFold
from scipy.stats import ttest_rel, wilcoxon
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from KCentroides import KCentroides
from OneR import OneR


'''
ZeroR, 
Aleatório, 
Aleatório Estratificado, 
*OneR Probabilístico, 
Naive Bayes Gaussiano, 

KmeansCentroides,
KGACentroides, 
Knn, 
DistKnn, 
Árvore de Decisão
Florestas de Árvores
'''

nomes = [
            'ZeroR', 
            'Aleatório', 
            'Aleatório Estratificado', 
            'OneR Probabilístico', 
            'Naive Bayes Gaussiano', 

            'KmeansCentroides',
            'KGACentroides',
            'Knn',
            'DistKnn',
            'Árvore de Decisão',
            'Florestas de Árvores'
        ]

#iris, digits, wine e breast cancer
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

param_kmeans = {'estimator__k': [1, 3, 5, 7]}
param_kga = {'estimator__k': [1, 3, 5, 7]}
param_knn = {'estimator__n_neighbors': [1, 3, 5, 7]}
param_DistKnn = {'estimator__n_neighbors': [1, 3, 5, 7]}
param_Arvore = {'estimator__max_depth': [None,3, 5, 10]}
param_Floresta = {'estimator__n_estimators': [10, 20, 50, 100]}

scalar = StandardScaler()

def get_pipeline(classificador):
    return Pipeline([('transformer', scalar), ('estimator', classificador)])

def get_gridSearchCV(classificador, parans):
    return GridSearchCV(estimator=get_pipeline(classificador), param_grid = parans, scoring='accuracy', cv = 4)

rskf = RepeatedStratifiedKFold(n_splits=10, n_repeats=3,random_state=36851234)
classificadores =   [ 
                        get_pipeline(DummyClassifier('most_frequent')), 
                        get_pipeline(DummyClassifier(strategy='uniform')),
                        get_pipeline(DummyClassifier(strategy='stratified')),
                        get_pipeline(OneR()),
                        get_pipeline(GaussianNB()),

                        get_gridSearchCV(KCentroides(algoritimo = 'KMeans'),param_kmeans),
                        get_gridSearchCV(KCentroides(algoritimo = 'Genetic'),param_kga),

                        get_gridSearchCV(KNeighborsClassifier(),param_knn),
                        get_gridSearchCV(KNeighborsClassifier(weights = 'distance'),param_DistKnn),
                        get_gridSearchCV(DecisionTreeClassifier(),param_Arvore),
                        get_gridSearchCV(RandomForestClassifier(),param_Floresta)
                    ]


lstScores =     [
                    cross_val_score(classificador, iris_X, iris_y, scoring='accuracy', cv = rskf,n_jobs=-1)
                    for classificador in classificadores
                ]
#print(lstScores)
tabela =    [
                {
                    'Média': scores.mean(),
                    'Desvio Padrão': scores.std(),
                    'Limite': stats.norm.interval(0.95, loc=scores.mean(), scale=scores.std()/np.sqrt(len(scores)))
                }
                for scores in lstScores
            ]

df = pd.DataFrame(tabela)

df['Limite Inferior'], df['Limite Superior'] = zip(*df.Limite)


print(df)

 
tabela_pareada =    [
                        [nome1 if i1 == i2 else ttest_rel(scores1,scores2)[1] if i1 < i2 else wilcoxon (scores1,scores2)[1]
                            for i2, (nome2, scores2) in enumerate(zip(nomes, lstScores))] 
                                for i1,(nome1, scores1) in enumerate(zip(nomes, lstScores))
                    ]
print(pd.DataFrame(tabela_pareada))


