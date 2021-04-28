import pandas as pd
import numpy as np
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt

nomes = [
            'ZeroR', 
            'Aleatório', 
            'A. Est', 
            'OneR', 
            'NBayes G.', 

            'Kmeans',
            'KGA',
            'Knn',
            'DistKnn',
            'Árv. D.',
            'Florestas'
        ]

sns.set_theme()

data_names = [
    #'iris', 
    'digits', 
    # 'wine', 
    # 'breast_cancer'
]

for name in data_names:
    df = pd.read_csv(f'result/{name}_scores.csv')
    #df['Classificador'] = nomes
    ax = sns.boxplot(x="Classificador", y='Acurácia', data=df)
    ax.set_xticklabels(nomes)
plt.show()