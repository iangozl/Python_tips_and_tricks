import collections
from collections import deque

d = deque("Welcome!")
d.pop()
d.append('1')
d.append(10)
d.pop()
d.popleft() # Removes an element from the left

d.clear()
d.extend('100hi') # Put it at the end of the list
# No need for a FOR LOOP

d.extend([1,2,3])
d.extendleft('morning') # It adds the element back

d.rotate(-1) # Takes an element from the left and puts it on the other side
print(d)

e = deque("hello", maxlen = 5) # You cannot change maxlen after initiated it

print(e)
e.extend([1,4,5]) # Adds the elements and removes the initial ones and preserves
                    # the max length
print(e)

