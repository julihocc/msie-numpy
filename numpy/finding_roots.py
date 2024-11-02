from scipy.optimize import root

# input 
def f(x): 
    return x**3-x-2 

x0 = 1.5

solution = root(f, x0)
# print(solution)
print(solution.success)
print(solution.x) 
print(solution.fun)