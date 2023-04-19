from sympy import *
n=symbols('n')
print(limit((3*n+9)*(ln(2*n-3)-ln(2*n-1)), n, oo))
