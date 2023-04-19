from sympy import *
n=symbols('n')
print(limit((6*n**4+8*n**3+6*n**2-6)/(4*n**6-3*n**5-7*n**4+6*n+9), n, oo))
