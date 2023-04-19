from sympy import *
x = symbols('x')
func = sin(x)
x0 = 0
print(func.series(x, x0, 10))
