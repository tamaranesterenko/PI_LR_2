import sympy
n = sympy.symbols('n')
print(sympy.limit((n**2-3*n)/(-5*n**3+4*n**2+9), n, sympy.oo))
