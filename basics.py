### SECTION 03 - The Basic Datatypes


## 10. Variables ---------------------------------------

# print('hello world!')

# my-bad-var = 'hello there!'
# print(my-bad-var)

# my_good_var = 'heya buddy!'
# print(my_good_var)

# myCamelVar = 'whassup bud?'
# print(myCamelVar)

# myBadVar02 = 'why does this work?'
# print(myBadVar02)

# 03badVar = `this is bad for so many raisins...`
# print(03badVar)

# import datetime
# today = datetime.datetime.now()
# print("today's datetime = ", today)

# mynumber = 5
# mytext = 'hello again!'
# print(mynumber, mytext)


## 11. Simple Types: Integers, Strings, and Floats ---------------------------------------

# x = 2
# y = '3'
# z = 5.5
# l = [1,2,3]
# m = {1: 2}

# print(type(x), type(y), type(z), type(l), type(m))

# list = [1, 2, 3]
# dict = {1: "cat", 2: "dog"}
# print(type(list), type(dict))

# range = list(range(1, 11))
# print(range)

# badrange = list(range("a", "z"))
# print(range)

# emptylist = list(range(5, 0))
# print(badrange2)

# coolrange = list(range(1, 100, 7))
# print(coolrange)

# listdir = dir(list)
# dirtype = type(listdir)
# print(dirtype)
# print(listdir)

# helpme = help(list.insert)
# print(help)

# allfunctions = dir(__builtins__)
# print(allfunctions)

# l = [1,2,5,3,2,4,6,9,4,3,2]
# length = len(l)
# mysum = sum(l)
# mean = mysum / length
# print(mean)

# student_grades = [9.1, 8.8, 7.5]
# student_grades.sort()
# student_grades.reverse()
# max_value = student_grades[0]
# print(max_value)

# student_grades = [9.1, 8.8, 7.5]
# # max_value = max(student_grades)
# student_grades.sort()
# max_value = student_grades[len(student_grades) - 1]
# print(max_value)

## DID YOU KNOW?

# Python is mainly used for automation purposes, web apps, and data science. 
# Many big companies like Instagram, Facebook, and Amazon use Python in different 
# parts of their products. For example, Facebook uses Python to process images.


# Summary: Integers, Floats, Lists, Dictionaries, Tuples, dir, help ---------------------------------------

# In this section you learned that:

#     Integers are for representing whole numbers:

#     rank = 10
#     eggs = 12
#     people = 3

#     Floats represent continuous values:

#     temperature = 10.2
#     rainfall = 5.98
#     elevation = 1031.88

#     Strings represent any text:

#     message = "Welcome to our online shop!"
#     name = "John"
#     serial = "R001991981SW"

#     Lists represent arrays of values that may change during the course of the program:

#     members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
#     pixel_values = [252, 251, 251, 253, 250, 248, 247]

#     Dictionaries represent pairs of keys and values:

#     phone_numbers = {"John Smith": "+37682929928",
#                      "Marry Simpons": "+423998200919"}
#     volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}

#     Keys of a dictionary can be extracted with:

#     phone_numbers.keys()

#     Values of a dictionary can be extracted with:

#     phone_numbers.values()

#     Tuples represent arrays of values that are not to be changed during the course of the program:

#     vowels = ('a', 'e', 'i', 'o', 'u')
#     one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

#     To find out what attributes a type has:

#     dir(str)
#     dir(list)
#     dir(dict)

#     To find out what Python builtin functions there are:

#     dir(__builtins__)

#     Documentation for a Python command can be found with:

#     help(str)
#     help(str.replace)
#     help(dict.values)


# Summary: Positive/Negative Indexes, Slicing --------------------------------------------------------------------------------

# In this section you learned that:

#     Lists, strings, and tuples have a positive index system:

#     ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#     0      1      2      3      4      5      6

#     And a negative index system:

#     ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#     -7 - 6 - 5 - 4 - 3 - 2 - 1

#     In a list, the 2nd, 3rd, and 4th items can be accessed with:

#     days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#     days[1:4]
#     Output: ['Tue', 'Wed', 'Thu']

#     First three items of a list:

#     days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#     days[:3]
#     Output: ['Mon', 'Tue', 'Wed']

#     Last three items of a list:

#     days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#     days[-3:]
#     Output: ['Fri', 'Sat', 'Sun']

#     Everything but the last:

#     days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#     days[:-1]
#     Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

#     Everything but the last two:

#     days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#     days[:-2]
#     Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

#     A single in a dictionary can be accessed using its key:

#     phone_numbers = {"John Smith": "+37682929928",
#                      "Marry Simpons": "+423998200919"}
#     phone_numbers["Marry Simpsons"]
#     Output: '+423998200919'

# import time
# timestamp = int(time.time())
# print(timestamp)

# def foo(temp):
#     if temp > 7:
#         return "Warm"
#     else:
#         return "Cold"

# def foo(temp):
#     if temp > 25:
#         return "Hot"
#     elif temp > 15:
#         return "Warm"
#     else:
#         return "Cold"

# Summary: Functions and Conditionals ---------------------------------------------

# In this section you learned to:

#     Define a function:

#     def cube_volume(a):
#         return a * a * a

#     Write a conditional block:

#     message = "hello there"

#     if "hello" in message:
#         print("hi")
#     else:
#         print("I don't understand")

#     Write a conditional block of multiple conditions:

#     message = "hello there"

#     if "hello" in message:
#         print("hi")
#     elif "hi" in message:
#         print("hi")
#     elif "hey" in message:
#         print("hi")
#     else:
#         print("I don't understand")

#     Use the and operator to check if both conditions are True at the same time:

#     x = 1
#     y = 1

#     if x == 1 and y == 1:
#         print("Yes")
#     else:
#         print("No")

# Output is Yes since both x and y are 1.

# Use the or operator to check if at least one condition is True:

#     x = 1
#     y = 2

#     if x == 1 or y == 2:
#         print("Yes")
#     else:
#         print("No")

# Output is Yes since x is 1.

# Check if a value is of a certain type with:

#     isinstance("abc", str)
#     isinstance([1, 2, 3], list)

# or

# type("abc") == str
# type([1, 2, 3]) == lst


# ----------------------------------------------------------------------

# def foo(name):
#     return "Hi %s" % name

# def foo(name):
#     return "Hi %s" % name.title()


# Summary: Processing User Input ----------------------------------------

# In this section you learned that:

#     A Python program can get user input via the input function:

#     The input function halts the execution of the program and gets text input from the user:

#     name = input("Enter your name: ")

#     The input function converts any input to a string, but you can convert it back to int or float:

#     experience_months = input("Enter your experience in months: ")
#     experience_years = int(experience_months) / 12

#     You can format strings with (works both on Python 2 and 3):

#     name = "Sim"
#     experience_years = 1.5
#     print("Hi %s, you have %s years of experience." % (name, experience_years))

# Output: Hi Sim, you have 1.5 years of experience.

# You can also format strings with (Python 3 only):

#     name = "Sim"
#     experience_years = 1.5
#     print("Hi {}, you have {} years of experience".format(name, experience_years))

# Output: Hi Sim, you have 1.5 years of experience.



# ------------------------------------------------------------------------------------------

# colors = [11, 34, 98, 43, 45, 54, 54]

# for number in colors:
#     print(number)


# colors = [11, 34, 98, 43, 45, 54, 54]

# for num in colors:
#     if num > 50:
#         print(num)


# colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

# for num in colors:
#     if isinstance(num, int):
#         print(num)


# colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

# for ele in colors:
#     if isinstance(ele, int) and ele > 50:
#         print(ele)




# Bonus Code: Dictionary Loop and String Formatting

# You can combine a dictionary for loop with string formatting to create text containing information from the dictionary:

#     phone_numbers = {"John Smith": "+37682929928",
#                      "Marry Simpons": "+423998200919"}

#     for pair in phone_numbers.items():
#         print("{} has as phone number {}".format(pair[0], pair[1]))


# Another (better) way to do it::

#     phone_numbers = {"John Smith": "+37682929928",
#                      "Marry Simpons": "+423998200919"}

#     for key, value in phone_numbers.items():
#         print("{} has as phone number {}".format(key, value))

# In both cases the output is:

# Output:

# John Smith has as phone number + 37682929928

# Marry Simpons has as phone number + 423998200919


# phone_numbers = {"John Smith": "+37682929928",
#                  "Marry Simpons": "+423998200919"}

# for key, val in phone_numbers.items():
#     print("{}: {}".format(key, val))


# phone_numbers = {"John Smith": "+37682929928",
#                  "Marry Simpons": "+423998200919"}

# for val in phone_numbers.values():
#     print("00{}".format(val[1:]))


# Summary: Loops

# In this section you learned that:

#     For loops are useful for executing a command over a large number of items.

#     You can create a for loop like so:

#     for letter in 'abc':
#         print(letter.upper())

# Output:

# A
# B
# C

#    The name after for (e.g. letter) is just a variable name

#     You can loop over dictionary keys:

#     phone_numbers = {"John Smith": "+37682929928",
#         "Marry Simpons": "+423998200919"}
#     for value in phone_numbers.keys():
#         print(value)

# Output:

# John Smith
# Marry Simpsons

#    You can loop over dictionary values:

#     phone_numbers = {"John Smith": "+37682929928",
#         "Marry Simpons": "+423998200919"}
#     for value in phone_numbers.values():
#         print(value)

# Output:

# +37682929928
# +423998200919

#    You can loop over dictionary items:

#         phone_numbers = {"John Smith": "+37682929928",
#             "Marry Simpons": "+423998200919"}
#         for key, value in phone_numbers.items():
#             print(key, value)

#     Output:

#     ('John Smith', '+37682929928')

#     ('Marry Simpons', '+423998200919')

#     While loops will run as long as a condition is true:

#         while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
#             print("It's not yet 19:30:20 of 2090.8.20")

#     The loop above will print out the string inside print() over and over again until the 20th of August, 2090.


### LIST COMPREHENSION ONE-LINERS ---------------------------------------------------------------------------------------------

# def foo(mylist):
#     return [ele for ele in mylist if isinstance(ele, (int, float))]

# def foo(mylist):
# #     return [ele for ele in mylist if ele > 0]


# def foo(mylist):
#     return [ele if isinstance(ele, (int, float)) else 0 for ele in mylist]


# def foo(mylist):
#     return sum([float(ele) for ele in mylist])


# # Summary: List Comprehensions - -----------------------------------------------------------------------------------------------

# In this section you learned that:

#     A list comprehension is an expression that creates a list by iterating over another container.

#     A basic list comprehension:

#         [i*2 for i in [1, 5, 10]]

#     Output: [2, 10, 20]

#     List comprehension with if condition:

#         [i*2 for i in [1, -2, 10] if i > 0]

#     Output: [2, 20]

#     List comprehension with an if and else condition:

#         [i*2 if i > 0 else 0 for i in [1, -2, 10]]

#     Output: [2, 0, 20]


# Summary: More on Functions

# In this section you learned that:

#     Functions can have more than one parameter:

#     def volume(a, b, c):
#         return a * b * c

#     Functions can have default parameters(e.g. coefficient):

#     def converter(feet, coefficient=3.2808):
#         meters = feet / coefficient
#         return meters

#     print(converter(10))

# Output: 3.0480370641306997

# Arguments can be passed as non-keyword(positional) arguments(e.g. a) or keyword arguments(e.g. b=2 and c=10):

#     def volume(a, b, c):
#         return a * b * c

#     print(volume(1, b=2, c=10))

#     An * args parameter allows the  function to be called with an arbitrary number of non-keyword arguments:

#     def find_max(*args):
#         return max(args)
#     print(find_max(3, 99, 1001, 2, 8))

# Output: 1001

# An ** kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:

#     def find_winner(**kwargs):
#         return max(kwargs, key=kwargs.get)

#     print(find_winner(Andy=17, Marry=19, Sim=45, Kae=34))

# Output: Sim


# file = open("data.txt")
# content = file.read()
# content = content.split("\n")
# for ele in content:
#   print(ele)

# Summary: File Processing

# In this section you learned that:

#     You can read an existing file with Python:

#     with open("file.txt") as file:
#         content = file.read()

#     You can create a new file with Python and write some text on it:

#     with open("file.txt", "w") as file:
#         content = file.write("Sample text")

#     You can append text to an existing file without overwriting it:

#     with open("file.txt", "a") as file:
#         content = file.write("More sample text")

#     You can both append and read a file with:

#     with open("file.txt", "a+") as file:
#         content = file.write("Even more sample text")
#         file.seek(0)
#         content = file.read()

