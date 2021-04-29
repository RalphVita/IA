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
from sklearn.pipeline import make_pipeline

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

rskf = RepeatedStratifiedKFold(n_splits=10, n_repeats=3,random_state=36851234)

#clf = make_pipeline(StandardScaler(), DummyClassifier('most_frequent'))
scalar = StandardScaler()
pipeline = Pipeline([('transformer', scalar), ('estimator', dKNN)])

scores = cross_val_score(clf, iris_X, iris_y, cv=rskf)

print(scores)