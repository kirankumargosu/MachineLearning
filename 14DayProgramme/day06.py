# Lesson 6: Prepare For Modeling by Pre-Processing Data Your raw data may not be setup to be in the best shape for
# modeling. Sometimes you need to pre-process your data in order to best present the inherent structure of the
# problem in your data to the modeling algorithms. In today’s lesson, you will use the pre-processing capabilities
# provided by the scikit-learn. The scikit-learn library provides two standard idioms for transforming data. Each are
# useful in different circumstances: Fit and Multiple Transform and Combined Fit-And-Transform. There are many
# techniques that you can use to prepare your data for modeling, for example try out some of the following:
# Standardize numerical data (e.g. mean of 0 and standard deviation of 1) using the scale and center options.
# Normalize numerical data (e.g. to a range of 0-1) using the range option. 􏰀
# Explore more advanced feature engineering such as Binarizing.
# For example, the snippet below loads the Pima Indians onset of diabetes dataset, calculates the parameters needed to
# standardize the data, then creates a standardize copy of the input data.

# Standardize data (0 mean, 1 stdev)
from sklearn.preprocessing import StandardScaler
from pandas import read_csv
import numpy
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://goo.gl/bDdBiA'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8] # pick all the rows; pick columns from 0 to 8
Y = array[:, 8] # pick all rows; pick column 8
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
# summarize transformed data
numpy.set_printoptions(precision=3)
print(rescaledX[0:5, :])
