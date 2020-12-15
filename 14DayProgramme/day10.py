# Lesson 10: Model Comparison and Selection
# Now that you know how to spot-check machine learning algorithms on your dataset, you need to know how to compare the
# estimated performance of different algorithms and select the best model. In todays lesson you will practice comparing
# the accuracy of machine learning algorithms in Python with scikit-learn.
# Compare linear algorithms to each other on a dataset.
# Compare nonlinear algorithms to each other on a dataset. 􏰀 Create plots of the results comparing algorithms.
# The example below compares Logistic Regression and Linear Discriminant Analysis to each other on the Pima Indians
# onset of diabetes dataset.

# Compare Algorithms
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# load dataset
url = 'https://goo.gl/bDdBiA'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
# prepare models
models = []
models.append(('LR', LogisticRegression(solver='liblinear')))
models.append(('LDA', LinearDiscriminantAnalysis()))
# evaluate each model in turn
results = []
names = []
scoring = 'accuracy'
for name, model in models:
    kfold = KFold(n_splits=10, random_state=7)
    cv_results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))