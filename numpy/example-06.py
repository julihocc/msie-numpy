import numpy as np 

np.random.seed(0)

u = np.random.randint(100, size=10)
print(u)

v = np.random.randint(100, size=10) 
print(v) 

print(u+v)
print(u-v)
print(u*v)
print(np.sum(u*v))
print(np.dot(u,v))