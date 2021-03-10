#5 Lambda

def func(x):
    return x+5

# It's used when you have one expression in your function

func2 = lambda x: x+5
print(func(2))
print(func2(10))

# Useful because you want to create a function inside another function

# lambda + filter()

a = [1,2,3,4,5,10,12]

newList = list(filter(lambda x: x%2 == 0, a))

print(newList)

# lambda + map()

second_list = list(map(lambda x: x + 10 , a))

print(second_list)