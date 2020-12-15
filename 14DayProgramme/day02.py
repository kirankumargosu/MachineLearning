# Lesson 2: Get Around In Python, NumPy, Matplotlib and Pandas You need to be able to read and write basic Python
# scripts. As a developer you can pick-up new programming languages pretty quickly. Python is case sensitive,
# uses hash (#) for comments and uses white space to indicate code blocks (white space matters). Todays task is to
# practice the basic syntax of the Python programming language and important SciPy data structures in the Python
# interactive environment.
# 1. Practice assignment, working with lists and flow control in Python.
# 2. Practice working with NumPy arrays.
# 3. Practice creating simple plots in Matplotlib.
# 4. Practice working with Pandas Series and DataFrame.
# For example, below is a simple example of creating a Pandas DataFrame.

# DataFrame
import numpy
import pandas

myArray = numpy.array([[1, 2, 3], [4, 5, 6]])
rowNames = ['a', 'b']
colNames = ['one', 'two', 'three']
myDataFrame = pandas.DataFrame(myArray, index=rowNames, columns=colNames)
print(myDataFrame)
