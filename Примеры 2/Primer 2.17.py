from sympy import *
n=symbols('n')
print(limit((4*7**(-n)-5*2**(-n)-5)/(5*2**(-n)+5*7**(-n)-3), n, oo))
