import pandas as pd
import numpy as np
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

data_names = [
    #'iris', 
    'digits', 
    # 'wine', 
    # 'breast_cancer'
]

for name in data_names:
    df = pd.read_csv(f'result/{name}_scores.csv')
    ax = sns.boxplot(x="Classificador", y='Acurácia', data=df)

plt.show()