# Map function

li = [1,2,4,5,6]

def func(x):
    return x**x

# Long Way:
newList = []

for x in li:
    newList.append(func(x))
print(newList)

# Combining functions and lists with map()
# There's many cases where you have to apply FUNCTIONS to a list.
print(list(map(func, li)))

# Using a loop
print([func(x) for x in li])




