from sympy import *
n=symbols('n')
print(limit((5*n**2+4)*(-7*n**2-7)**2/(3*n**2+6)**3, n, oo))
