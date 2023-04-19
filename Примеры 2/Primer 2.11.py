from sympy import *
n=symbols('n')
print(limit(sqrt(3*n**18+2)/sqrt(5*n**16-5*n**9+8), n, oo))
