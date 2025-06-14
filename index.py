
from datetime import datetime
from datetime import timedelta
import time

current_time = time.time()
print(f"Поточний час: {current_time}")

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")


# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)


# now = datetime.now()

# print(now)
# print(datetime.now().day)


# ######################## conditions

# name = "Andrii"

# if name == "Andrii":
#     print(f"Hello {name}")
# elif name == "Husky":
#     print(f"Hello dog {name}")
# else:
#     print("Hello no name!") 

# ######################## ternary
# name = ""
# print(name if name else "No name")

# ######################## match ...case
# name = "Andrii"

# match name:
#     case "Andrii":
#         print(f"Hello {name}")

#     case "Husky":
#          print(f"Hello dog {name}")

#     case _:
#         print("Hello no name!")

# ######################## try...except
# val = 'a'

# try:
#     val = int(val)
# except ValueError:
#     print(f"val {val} is not a number")
# else:
#     print(val > 0)
# finally:
#     print("This will be printed anyway")

# #######################loops
# for i in range(5):
#     print(i)

# for i in range(2, 10):
#     print(i)

# some_list = ["apple", "banana", "cherry"]

# for index, value in enumerate(some_list):
#     print(index, value)


# list1 = ["зелене", "стигла", "червоний"]
# list2 = ["яблуко", "вишня", "томат"]

# for number, letter in zip(list1, list2):
#     print(number, letter)

######################## functions
# def say_hello(name): 
#     return f"Hello {name}"

# print(sayHello('Andrii'))

# def say_hello_to_args(*args):
#     for arg in args:
#         print(arg)

# def check_all_args(*args, **kwargs):
#     for arg, kwarg in zip(args, kwargs):
#         print(arg, kwarg)

# check_all_args('a',"b","c", d="d1", e="e1", f="f1")


######################## unpucking

# my_list = [1, 2, 3]
# a, b, c = my_list

# aa, *rest = my_list

# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# person_info = {"name": "Alice", "age": 25}
# greet(**person_info)








