import matplotlib.pyplot as plt 
import numpy as np 

# input 
def f(x): 
    return x**3-x-2 

a = 1.4
b = 1.6
tol = 0.001 
nmax = 1000 

x_range = np.linspace(a,b,num=101) 
# print(x_range)
# print(len(x_range))
y_range = f(x_range)
# x_axis = np.zeros_like(x_range)
x_axis = 0*x_range
plt.plot(x_range,y_range)
plt.plot(x_range,x_axis,c="red")
plt.show()

cond1 = a < b 
# cond2 = (f(a)<0 and f(b)>0) or (f(a)>0 and f(b)<0)
cond2 = f(a)*f(b) < 0 

if not cond1 or not cond2:
    raise("Conditions are not meet")

n = 1 

output = None 

while n <= nmax:
    c = (a+b)/2 
    
    if f(c) == 0 or (b-a)/2 < tol:
        output = c
        break  

    n+=1 
    
    if f(c)*f(a) > 0: 
        a = c  
    else: 
        b = c 

print(output) 
if output:
    print(np.abs(f(output)))

 
