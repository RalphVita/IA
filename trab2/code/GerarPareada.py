import pandas as pd
import numpy as np
from scipy.stats import ttest_rel, wilcoxon


name = 'breast_cancer'
df = pd.read_csv(f'result/{name}_scores.csv')

df = df.groupby('Classificador')['Acurácia'].apply(list)
print([[x,y] for (x,y) in zip(df.loc['Knn'],df.loc['DistKnn'])])
print(ttest_rel(df.loc['Knn'],df.loc['DistKnn']))