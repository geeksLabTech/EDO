
from numerical_ode_solver import NumericalOdeSolver
import numpy as np
import matplotlib.pyplot as plt
import math

def implicit_euler(f, h=0.1, n=10, x0=0, y0=1): 
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = x0 
    y[0] = y0
    
    for i in np.arange(1, n):
        y[i] = y[i-1] + f(x[i-1], y[i-1]) * h
        x[i] = x[i-1] + h
    
    print(x)
    print(y)


def improved_euler(f, h=0.1, n=10, x0=0, y0=1):
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = x0 
    y[0] = y0
    
    for i in np.arange(1, n):
        y_after = y[i-1] + h * f(x[i-1], y[i-1])
        x[i] = x[i-1] + h
        y[i] = y[i-1] + (f(x[i-1], y[i-1]) + f(x[i], y_after)) * h/2
        
    
    print(x)
    print(y)


def rk4(f, h=0.1, n=10, x0=0, y0=1): 
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = x0 
    y[0] = y0
    
    for i in np.arange(1, n):
        x_before = x[i-1]
        y_before = y[i-1]
        k1 = f(x_before, y_before)
        k2 = f(x_before + 1/2 * h, y_before + 1/2*k1*h)
        k3 = f(x_before + 1/2* h, y_before + 1/2*k2*h)
        k4 = f(x_before + h, y_before + k3*h)
        m = 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        y[i] = y_before + m * h
        x[i] = x[i-1] + h
    
    print(x)
    print(y)


f = lambda x, y: 2*x*y 

solver = NumericalOdeSolver("2xy", h = 0.05, x0=1)
solution = solver.solve()
print(solution)
#implicit_euler(f, x0=1, h=0.05)
#improved_euler(f, x0=1, h=0.05)
#rk4(f, x0=1, h = 0.05)