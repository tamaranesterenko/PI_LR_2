from sympy import *
n=symbols('n')
print(limit(3/ (sqrt(9*n**2-5*n+4 ) -sqrt(9*n**2-2*n+5)) ,n, oo))
