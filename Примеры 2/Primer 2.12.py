from sympy import *
n=symbols('n')
print(limit((sqrt(25*n**2+3*n-2)-sqrt(16*n**2+n+4))/(3*n+2), n, oo))
