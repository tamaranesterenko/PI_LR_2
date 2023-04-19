from sympy import *
n=symbols('n')
print(limit((3*4**(-n)-2*6**(-n))/(5*6**(-n)-3*4**(-n)), n, oo))
