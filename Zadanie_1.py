from sympy import *
n=symbols('n')
print(limit((-5*n**5+8*n**3-6)/(sqrt(3*n**16+n**7+7)), n, oo))
