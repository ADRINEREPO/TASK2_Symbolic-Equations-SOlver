from sympy import symbols, Eq, solve
x = symbols('x')
expr = x-4-2


sol = solve(expr)


sol

y = symbols('x')
eq1 = Eq(x**2 -5*x + 6)


sol = solve(eq1)
sol

import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))    
d = (b**2) - (4*a*c)  

sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))

a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
x = symbols('x')
f = a*x**3+b*x**2+c*x

df = diff(f, x)
df2= diff(df,x)

import matplotlib.pyplot as plt
import numpy as np
import sympy as sy


def f(x):
	return x**2


def g(x):
	return x**(1/2)


x = sy.Symbol("x")
print(sy.integrate(f(x)-g(x), (x, 0, 2)))
