import collections
from collections import namedtuple

Point = namedtuple('Point', 'x y z') # Name is 'Point'
# It breaks it up by space

newP = Point(3,4,5) # Treat it as an object


Point2 = namedtuple('Point2', {'x':0, 'y':7, 'z':10})
newP2 = Point2(3,5,30)
print(newP2)

# You can print each value individually
print(newP2.x, newP2.y, newP2.z) # You cannot do that with a regular tuple

# Print fiels
print(newP2._fields) # Methods require underscore _

# Replacing method
newP2 = newP2._replace(x=88)
print(newP2)

# Replacing methods
newP2 = Point2._make(['a','b','c']) # Replaces the value
print(newP2)
