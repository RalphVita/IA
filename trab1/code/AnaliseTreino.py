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

# dfA4 =  dfA3.pivot(index="Configuração", columns=['Base','K'], values="Rank")
# print(dfA4.to_latex())
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



def BocPlotTreino(carac = 'z-score'):
    #5 Melhores por Heuristica

    df_ = df[df['Heuristica'] == 'Grasp']
    



    df_['Heuristica'] = df_['Heuristica'].map(str) + '-' + df['Configuração'].map(str)
    
    sns.set_theme()
    df5MelhoresPorHeuristica = df_.sort_values(['Heuristica','z-score','Rank'], ascending=True)
    #df5MelhoresPorHeuristica = df.sort_values(['Heuristica',('z-score', 'mean'),('Rank', 'mean')], ascending=True)#.groupby('Heuristica').head(5)
    df5MelhoresPorHeuristica = df5MelhoresPorHeuristica.reset_index()
    #df5MelhoresPorHeuristica.columns = ['x','y','Metahurística', 'Configuração', 'Média', 'Desvio padrão','Tempo médio','Rank', 'Base','Z-score médio','Rank médio']
    #print(df5MelhoresPorHeuristica.to_string())
    #plt.xticks(rotation='vertical')
    #df5MelhoresPorHeuristica.to_csv('result/analise/5MelhoresPorHeuristica.csv')

    

    ax = sns.boxplot(x="Heuristica", y=carac, data=df5MelhoresPorHeuristica)
    plt.setp(ax.get_xticklabels(), rotation=45)
    #plt.title('Boxplot das médias de tempo por Metahurística')
    ax.set_xticklabels(['MH-1','MH-2','MH-3','MH-4','MH-5','MH-6','MH-7','MH-8','MH-9','MH-10','MH-1','MH-11','MH-12','MH-13','MH-14','MH-15','MH-16','MH-17','MH-18'])
    #ax.set_xticklabels(['MH-18','MH-19','MH-20','MH-21','MH-22','MH-23','MH-24','MH-25','MH-26','MH-27','MH-28','MH-29','MH-30','MH-31','MH-32','MH-33','MH-34','MH-35','MH-36'])

def Plot5Melhores():
    plt.title('Boxplot das médias de Z-score por Metahurística')    
    BocPlotTreino()

    # plt.title('Boxplot das médias de tempo por Configuração')
    # plt.ylim(1,1.09)
    # BocPlotTreino('Tempo médio')

    plt.show()

Plot5Melhores()

print(dfMelhores.to_latex(index=False)) 