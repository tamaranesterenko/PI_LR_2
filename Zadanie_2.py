#!/usr/bin/python
# -*- coding: utf-8

from sympy import *
n=symbols('n')
print(limit(((n**3-9*n-2)/(n**3+3*n+9))**(9*n**2+6), n, oo))
