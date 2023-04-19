from sympy import *
n=symbols('n')
print(limit(((n**2+3*n+7)/(n**2+8*n-6))**(3*n-4), n, oo))
