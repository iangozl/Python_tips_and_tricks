# Never name a module which already exists in python

# Example:

# If I name this file as math.py, there will be a conflict with the original python math module

# If I create and empty list in an argument of a function:

# Python only executes those default arguments just once when the function is declared
import time
from datetime import datetime

def display_time(time=datetime.now()):
    print(time.strftime('%B %d, %Y %H:%M:%S'))

print ("\nFirst example\n")
display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()

# We see that the time still the same even though we expect it to change each second, this is because python only executes those default 
# arguments once when the function is declared

def display_time(time=None):
    if time is None:
        time = datetime.now()
    print(time.strftime('%B %d, %Y %H:%M:%S'))

print ("\nSecond example\n")
display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()

# How iterators work
# Iterators can be exhausted 

# Don't use * all the time, could be a bad practice.
# It's harder to debug your code, because you won't know where some functions are coming from


