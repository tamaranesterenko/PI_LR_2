from sympy import *
n=symbols('n')
print(limit((sqrt(n**2+5)-n)*atan(5*n**3-1),n,oo))
