import pandas as pd
import numpy as np


data_names = [
    #'iris', 
    #'digits', 
     #'wine', 
     'breast_cancer'
]

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
index = 0
pd.options.display.float_format = '{:.2e}'.format

def change_dtype(value):
    global nomes,index
    try:
        return int(value)
    except ValueError:
        try:
            str_e = "{:.2e}".format(float(value))
            str_f = "{:.2f}".format(float(value))
            return str_f if float(value) > 0.05 else '\\textbf{'+str_e+'}'
        except ValueError:
            index+=1
            return '\\textbf{'+nomes[index-1]+'}'

for name in data_names:
    df = pd.read_csv(f'result/{name}_pareada.csv',index_col=0)
    
    # df = df.apply(pd.to_numeric, args=('coerce',))
    # df = df.fillna(0)

    

    for column in df.columns:
        df.loc[:, column] = df[column].apply(change_dtype)

# def negative_bold(val):
#     bold = 'bold' if val < 0.95 else ''
#     return 'font-weight: %s' % bold

# df.style.applymap(negative_bold)

print(df)
print(df.to_latex(index=False,header=False,float_format='{:.2e}'.format).replace("\\\n", "\\ \hline\n").replace('\\textbackslash ','\\').replace('\{','{').replace('\}','}'))