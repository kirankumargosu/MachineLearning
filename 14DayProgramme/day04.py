# Lesson 4: Understand Data with Descriptive Statistics
# Once you have loaded your data into Python you need to be able to understand it.
# The better you can understand your data, the better and more accurate the models that you can build.
# The first step to understanding your data is to use descriptive statistics.
# Today your lesson is to learn how to use descriptive statistics to understand your data.
# I recommend using the helper functions provided on the Pandas DataFrame.
# Understand your data using the head() function to look at the first few rows. 􏰀
# Review the dimensions of your data with the shape property.
# Look at the data types for each attribute with the dtypes property.
# Review the distribution of your data with the describe() function.
# Calculate pairwise correlation between your variables using the corr() function.
# The below example loads the Pima Indians onset of diabetes dataset and summarizes the distribution of each attribute.

# Statistical Summary
from pandas import read_csv
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://goo.gl/bDdBiA'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(url, names=names)
description = data.describe()
print(description)
corrPearson = data.corr(method='pearson')
print(corrPearson)
corrKendall = data.corr(method='kendall')
print(corrKendall)
