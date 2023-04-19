from sympy import *
n=symbols('n')
print(limit(sqrt(5*n**14-3*n**8+2*n-1)/(2*n**7-8*n**4+1), n, oo))
