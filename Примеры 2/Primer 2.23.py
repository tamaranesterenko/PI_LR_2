from sympy import *
n=symbols('n')
print(limit(sqrt(5*n**2)-sqrt(5*n**2-4), n, oo))
