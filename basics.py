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
