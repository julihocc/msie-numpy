import numpy as np 

n = np.array(range(25), dtype=np.float32)
print(n)
print(n.shape)

# n.shape = (5,5)
# print(n)
# print(n.shape)

# n.shape = (25,1)
# print(n)
# print(n.shape)

# n.shape = (1,25)
# print(n)
# print(n.shape)

n.shape = (5,-1)
print(n)
print(n.shape)