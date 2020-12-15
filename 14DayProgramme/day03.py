# Lesson 3: Load Data From CSV
# Machine learning algorithms need data. You can load your own data from CSV files but when
# you are getting started with machine learning in Python you should practice on standard
# machine learning datasets. Your task for todays lesson are to get comfortable loading data into
# Python and to find and load standard machine learning datasets. There are many excellent
# standard machine learning datasets in CSV format that you can download and practice with on 5
# 􏰀 Practice loading CSV files into Python using the CSV.reader()6 function in the standard library.
#  Practice loading CSV files using NumPy and the numpy.loadtxt()7 function.
#  Practice loading CSV files using Pandas and the pandas.read csv()8 function.
# To get you started, below is a snippet that will load the Pima Indians onset of diabetes dataset using Pandas
# directly from the UCI Machine Learning Repository.

# Load CSV using Pandas from URL
from pandas import read_csv
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://goo.gl/bDdBiA'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class', 'dummy']  # this is the header columns for the dataset
data = read_csv(url, names=names)

print(data.shape)  # this prints the (rowCount, colCount)
print (data['preg']) # prints the column for preg - which is the first column
print (data['dummy']) # the dataset has only 9 columns. Dummy is an extra column. This will print only NaN.
