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


Note on Loading Excel Files

In the next lecture you're also going to learn how to load Excel (.xlsx) files in Python with pandas. Pandas may require the xlrd library as a dependency. If you get an error such as ModuleNotFoundError: No module named 'xlrd', you can fix the error by installing xlrd:

pip install xlrd
or

pip3 install xlrd
