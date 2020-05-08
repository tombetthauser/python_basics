#remember you have to 'pip3 install pandas' and pip3 install ipython before working with these
#
# ipython is just an enhanced interface for working with data in python
#
# pandas is a library that allows us to easily work with a lot of different database formats like json etc
#
# when you enter into ipython you have to manually import pandas



# test
# PANDAS iPYTHON EXAMPLE
# creating a 'dataframe'
# creating a 'dataframe' --> df1=pandas.DataFrame([1,2,3],[4,5,6],columns=['a','b','c'],index=['one','two'])
# you can also create these dataframes with objects and use panda methods to access specific rows / columns etc (called pandas series) and get things like the mean or highest value etc
# in jupyter press esc and dd (d two times) to delete
# lookup more keyboard shortcuts under the help dropdown under keyboard shortcuts
# once youre done with a session just close the browser tabs and to reopen just relocate to directory with a notebook and command line $ jupyter notebook



# Solution

# The code for loading the supermarkets.json file in Python with pandas would be this:

#     import pandas
#     df2 = pandas.read_json("supermarkets.json")

# The df2 dataframe should contain this data:






# Exercise: Loading JSON Files

# In  the previous lecture you learned that you can load a CSV file with this code:

#     import pandas
#     df1 = pandas.read_csv("supermarkets.csv")

# Try loading the supermarkets.json file for this exercise using read_json instead of read_csv.

# The supermarkets.json file can be found inside the supermarkets.zip file attached in the previous lecture.


import numpy
import pandas
import cv2
Note on Loading Excel Files

In the next lecture you're also going to learn how to load Excel (.xlsx) files in Python with pandas. Pandas may require the xlrd library as a dependency. If you get an error such as ModuleNotFoundError: No module named 'xlrd', you can fix the error by installing xlrd:

pip install xlrd
or

pip3 install xlrd



# Installing OpenCV

# In the next lecture and in Section 17 we will use the OpenCV image processing library. Let us first make sure you have installed the OpenCV library. OpenCV is also referred to as cv2 in Python.


# Install OpenCV:

# 1. Open the command line and type:

# pip install opencv-python

# 2. Open a Python session and try:


#
# 
# 
#  FROM JUPYTER SESSION

# dt1 = pandas.read_csv("sota.csv")

# len(dt1.columns)

# 104

# len(dt1.index)

# 99

# dt1.to_numpy()[0:2, 0:4]

# array([['2019/08/06 5:24:58 PM PDT', 'M', 'W', 'Prefer not to say'],
#        ['2019/08/09 2:38:06 PM PDT', 'Female', 'White', 'No']],
#       dtype=object)

# ​


# n = numpy.arange(27)

# n.reshape(3, 3, 3)

# array([[[0,  1,  2],
#         [3,  4,  5],
#         [6,  7,  8]],

#        [[9, 10, 11],
#         [12, 13, 14],
#         [15, 16, 17]],

#        [[18, 19, 20],
#         [21, 22, 23],
#         [24, 25, 26]]])

# m = numpy.asarray([[123, 12, 123, 12, 33], [], []])

# type(m)

# numpy.ndarray


# dt1

# pandas.core.frame.DataFrame
