import pandas as pd
import numpy as np
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./result/result.csv')

#Problema = [Base,K]
#print(df)
#print(df.groupby(['Heuristica','Base','K'])['Média'].transform(lambda x : zscore(x)))
df['z-score'] = df.groupby(['Heuristica','Base','K'])['Média'].transform(lambda x : zscore(x))

df['Rank'] = df.groupby(['Heuristica','Base','K'])['z-score'].rank()#.transform(lambda x : zscore(x))
#df['Rank'] = df['z-score'].rank()

dfA3 = df[df['Heuristica'] == 'Genético']

print(dfA3.to_string())

dfA4 =  dfA3.pivot(index="Configuração", columns=['Base','K'], values="Rank")
print(dfA4.to_latex())
# exit()

#Obter média, desvio padrão e ranqueamento médio da configuração
dfT = df.groupby(['Heuristica','Configuração']).agg(
    {
        'z-score': [np.mean, np.std],
        'Rank': np.mean,
        'Tempo médio': np.mean
    })

#print(dfT.to_string())


#Obter melhor configuração por média e por ranqueamento médio do método
dfMelhores =  dfT.sort_values(['Heuristica',('z-score', 'mean'),('Rank', 'mean')], ascending=True).groupby('Heuristica').head(1)
dfMelhores = dfMelhores.reset_index()
dfMelhores.columns = ['Metahurística', 'Configuração', 'Z-score médio', 'Desvio padrão','Rank médio', 'Tempo médio']
#print(dfMelhores)

#Obter as 5 melhores resultados de médias padronizadas e os
#tempos correspondentes das configurações de cada método
df5Melhores =  dfT.sort_values(['Heuristica',('z-score', 'mean')], ascending=True).groupby('Heuristica').head(5)
#print(df5Melhores)

#Retornar tabela com melhor configuração de cada método por média e
#ranqueamento médio
#print(dfMelhores)



def BocPlotTreino(carac = 'Z-score médio'):
    #5 Melhores por Heuristica
    
    sns.set_theme()
    df5MelhoresPorHeuristica = dfT.sort_values(['Heuristica',('z-score', 'mean'),('Rank', 'mean')], ascending=True).groupby('Heuristica').head(5)
    df5MelhoresPorHeuristica = df5MelhoresPorHeuristica.reset_index()
    df5MelhoresPorHeuristica.columns = ['Metahurística', 'Configuração', 'Z-score médio', 'Desvio padrão','Rank médio', 'Tempo médio']
    print(df5MelhoresPorHeuristica.to_string())
    #plt.xticks(rotation='vertical')
    #df5MelhoresPorHeuristica.to_csv('result/analise/5MelhoresPorHeuristica.csv')
    ax = sns.boxplot(x="Metahurística", y=carac, data=df5MelhoresPorHeuristica)
    #plt.title('Boxplot das médias de tempo por Metahurística')

def Plot5Melhores():
    # plt.title('Boxplot das médias de Z-score por Metahurística')    
    # BocPlotTreino()

    plt.title('Boxplot das médias de tempo por Metahurística')
    plt.ylim(1,1.09)
    BocPlotTreino('Tempo médio')

    plt.show()

Plot5Melhores()

print(dfMelhores.to_latex(index=False)) 