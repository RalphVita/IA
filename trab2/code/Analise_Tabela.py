import pandas as pd
import numpy as np


data_names = [
    #'iris', 
    #'digits', 
    # 'wine', 
     'breast_cancer'
]
pd.options.display.float_format = '{:.2f}'.format

for name in data_names:
    df = pd.read_csv(f'result/{name}_media.csv',index_col=None)

print(df)
print(df[['Método','Média','Desvio Padrão','Limite Inferior','Limite Superior']].to_latex(index=False).replace("\\\n", "\\ \hline\n"))