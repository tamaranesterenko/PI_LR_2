from sympy import *
n=symbols('n')
print(limit((3+6*n**8+7*cos(3*n))/(6+5*n**3-8*sin(3*n)),n,oo))
