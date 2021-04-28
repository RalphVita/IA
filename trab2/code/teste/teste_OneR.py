from sklearn.preprocessing import KBinsDiscretizer
import numpy as np
import pandas as pd
from scipy import stats
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

est = KBinsDiscretizer(n_bins=8, 
                    encode='ordinal', strategy='kmeans').fit(iris_X,iris_y)
X_bin = est.transform(iris_X)
#print(X_bin)

n_caracteristica = iris_X.shape[1]

classes = np.unique(iris_y)

lst = []
#data = [[lst.append([caracteristica,bin_, classe]) for (bin_, classe) in zip(X_bin[:,caracteristica],iris_y)] for caracteristica in range(n_caracteristica)]
datas = [[[caracteristica,bin_, classe] for (bin_, classe) in zip(X_bin[:,caracteristica],iris_y)] for caracteristica in range(n_caracteristica)]

dfs = []
for data in datas:
    data = np.array(data)
    df = pd.DataFrame(data=data,columns=['caracteristica','bin_', 'classe'])
    pivot = pd.pivot_table (df, values = "caracteristica", 
                            index = "bin_", columns = "classe", 
                            aggfunc = "count")
    pivot = pivot.fillna(0)
    
    lst.append((data[0][0],pivot.max().values))
    dfs.append(pivot)


__self_pred = max(lst, key = lambda x: sum(x[1]))
print(__self_pred)

matriz = np.array(dfs[int(__self_pred[0])])

caracteristica = int(__self_pred[0])

result = []
for X in X_bin:
    array = matriz[int(X[caracteristica])]
    result.append(np.random.choice(classes,1,p=array/sum(array))[0])

print(result)
    

