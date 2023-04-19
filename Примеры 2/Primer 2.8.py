from sympy import *
n=symbols('n')
print(limit((8+5*n+cos(6*n))/(3*n-8*sin(5*n)-8),n,oo))
