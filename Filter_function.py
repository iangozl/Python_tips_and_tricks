# Filter Function

def add100(x):
    return x + 100

def isOdd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,9,10]

# Filter only works with True or False, that makes it good for verifying values
b = list(filter(isOdd,a))
print(b)

# What map() does is apply that function to each character
c = list(map(add100,b))
print(c)

