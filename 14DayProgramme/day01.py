# Lesson 1: Download and Install Python and SciPy Ecosystem You cannot get started with machine learning in Python
# until you have access to the platform. Todays lesson is easy, you must download and install the Python 3.6 platform
# on your computer. Visit the Python homepage2 and download Python for your operating system (Linux, OSX or Windows).
# Install Python on your computer. You may need to use a platform specific package manager such as macports on OS X
# or yum on RedHat Linux. You also need to install the SciPy platform3 and the scikit-learn library. I recommend
# using the same approach that you used to install Python. You can install everything at once (much easier) with
# Anaconda. Anaconda is recommended for beginners. Start Python for the first time from command line by typing python
# at the command line. Check the versions of everything you are going to need using the code below:

# Python version
import sys

print('Python: {}'.format(sys.version))
# scipy
import scipy

print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy

print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib

print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas

print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn

print('sklearn: {}'.format(sklearn.__version__))
