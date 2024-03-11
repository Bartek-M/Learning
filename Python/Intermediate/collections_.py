print("Intermediate things in python\n============================================")

# Imports
import numpy as np
from collections import deque

# Deque
print("\n[DEQUE]")
d = deque([1, 2, 3, 4, 5])
print(d)

d.append(6) # Add to back
d.appendleft(0) # Add to front
print("Adding elements:", d)

d.pop() # Remove last item
d.popleft() # Remove first item
print("Removing elements:", d)

d.clear() # Clear
print("Clear deque:", d)

d.extend("Hello") # Add to back
d.extendleft([1, 2, 3]) # Add to front reversed
print("Extending:", d)

d.rotate(-1) # Rotate deque; - left, + right
print("Rotate deque:", d)

# Max len
d = deque("Hello", maxlen=5)
print(d)
d.append(1)
print(d)


# Matrix - 2D array
print("\n\n[MATRIX - 2D ARRAY]")

a = np.array([
    [1, 2, 3, 4], 
    [4, 55, 1, 2], 
    [8, 3, 20, 19], 
    [11, 2, 22, 21]
])
m = np.reshape(a, (4, 4))
print(m, end="\n\n")

print(a[1]) # Accessing list element
print(a[2][0], end="\n\n") # Accessing specific element
  
# Adding Element
m = np.append(m, [[1, 15, 13, 11]], 0)
print(m, end="\n\n")
  
# Deleting Element
m = np.delete(m, [1], 0)
print(m)