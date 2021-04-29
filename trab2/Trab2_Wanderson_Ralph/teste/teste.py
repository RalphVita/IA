import numpy as np
from scipy import stats
from sklearn import datasets
from sklearn.model_selection import cross_val_predict 
from sklearn.dummy import DummyClassifier
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score, GridSearchCV, RepeatedStratifiedKFold

'''
ZeroR, 
Aleatório, 
Aleatório Estratificado, 
*OneR Probabilístico, 
Naive Bayes Gaussiano, 

*KmeansCentroides,
*KGACentroides, 
Knn, 
DistKnn, 
Árvore de Decisão
Florestas de Árvores
'''
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

rskf = RepeatedStratifiedKFold(n_splits=10, n_repeats=3,random_state=36851234)

##### ZeroR #####

zR = DummyClassifier()

scores = cross_val_score(zR, iris_X, iris_y, scoring='accuracy', 
                         cv = rskf)

print(scores)

mean = scores.mean()
std = scores.std()
inf, sup = stats.norm.interval(0.95, loc=mean, 
                               scale=std/np.sqrt(len(scores)))

print("\nMean Accuracy: %0.2f Standard Deviation: %0.2f" % (mean, std))
print ("Accuracy Confidence Interval (95%%): (%0.2f, %0.2f)\n" % 
       (inf, sup)) 



# y_pred = cross_val_predict(zR, iris_X, iris_y, cv=5)
# conf_mat = confusion_matrix(iris_y, y_pred)

# print(conf_mat)

# plt.matshow(conf_mat, cmap=plt.cm.Blues)
# for i in range(len(conf_mat)):
#     for j in range(len(conf_mat)):
#         plt.text(i, j, conf_mat[i][j], va="center", ha="center")

# #plt.show()


# ###### Aleatório #######

# aU = DummyClassifier(strategy='uniform')

# y_pred = cross_val_predict(aU, iris_X, iris_y, cv=5)
# conf_mat = confusion_matrix(iris_y, y_pred)

# print(conf_mat)

# plt.matshow(conf_mat, cmap=plt.cm.Blues)
# for i in range(len(conf_mat)):
#     for j in range(len(conf_mat)):
#         plt.text(i, j, conf_mat[i][j], va="center", ha="center")

# #plt.show()

# ####### Aleatório Estratificado #######

# aS = DummyClassifier(strategy='stratified')

# y_pred = cross_val_predict(aS, iris_X, iris_y, cv=5)
# conf_mat = confusion_matrix(iris_y, y_pred)

# print(conf_mat)

# plt.matshow(conf_mat, cmap=plt.cm.Blues)
# for i in range(len(conf_mat)):
#     for j in range(len(conf_mat)):
#         plt.text(i, j, conf_mat[i][j], va="center", ha="center")

# #plt.show()

# ####### Naive Bayes Gaussiano #######

# gNB = GaussianNB()

# y_pred = cross_val_predict(gNB, iris_X, iris_y, cv=5)
# conf_mat = confusion_matrix(iris_y, y_pred)

# print(conf_mat)

# plt.matshow(conf_mat, cmap=plt.cm.Blues)
# for i in range(len(conf_mat)):
#     for j in range(len(conf_mat)):
#         plt.text(i, j, conf_mat[i][j], va="center", ha="center")

# plt.show()