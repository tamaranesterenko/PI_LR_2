from sympy import *
n=symbols('n')
print(limit((-n+2)**2*(-2*n+7)/((n+1)**2*sqrt(n**2+5)), n, oo))
