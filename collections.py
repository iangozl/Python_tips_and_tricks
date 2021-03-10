from collections import Counter

# It doesn't return error

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a','b','b','c'])

# Intersection
print(c & d)

# subtract
c.subtract(d)
print(c)

# Update <- It's like adding
c.update(d)
print(c)

# Clear() <- Erase everything
c.clear()
print(c)