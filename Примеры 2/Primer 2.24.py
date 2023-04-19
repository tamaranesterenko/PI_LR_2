from sympy import *
n=symbols('n')
print(limit((1-3/n)**(-8*n), n, oo))
