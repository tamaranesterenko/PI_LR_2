from sympy import *
n=symbols('n')
print(limit((1-4/(7*n+6))**(-2*n+5), n, oo))
