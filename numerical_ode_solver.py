

from typing import Optional
import numpy as np
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

class NumericalOdeSolver:
    def __init__(self, function:str, exact_solution:Optional[str]=None, h=0.1, n:int=10, x0=0.0, y0=1.0):
      self.f = function
      self.exact_solution = exact_solution
      self.h = h
      self.n = n 
      self.x0 = x0
      self.y0 = y0


    def create_arrays_with_the_initial_value(self):
        x = np.zeros(self.n)
        y = np.zeros(self.n)
        x[0] = self.x0 
        y[0] = self.y0
        return x, y


    def absolute_error(self, y1, y2):
        error = np.zeros(self.n)
        for i in range(self.n):
            error[i] = np.abs(y1[i] - y2[i])

        return error


    def eval_expr(self, x, y):
        return parse_expr(
            self.f, 
            local_dict={'x': x, 'y': y},
            transformations=(standard_transformations + (implicit_multiplication_application,)))


    def implicit_euler(self): 
        x, y = self.create_arrays_with_the_initial_value()

        for i in np.arange(1, self.n):
            y[i] = y[i-1] + self.eval_expr(x[i-1], y[i-1]) * self.h
            x[i] = x[i-1] + self.h
        
        return x, y


    def improved_euler(self):
        x, y = self.create_arrays_with_the_initial_value()
        
        for i in np.arange(1, self.n):
            y_after = y[i-1] + self.h * self.eval_expr(x[i-1], y[i-1])
            x[i] = x[i-1] + self.h
            y[i] = y[i-1] + (self.eval_expr(x[i-1], y[i-1]) + self.eval_expr(x[i], y_after)) * self.h/2
            
        return x, y


    def rk4(self): 
        x, y = self.create_arrays_with_the_initial_value()
        
        for i in np.arange(1, self.n):
            x_before = x[i-1]
            y_before = y[i-1]
            k1 = self.eval_expr(x_before, y_before)
            k2 = self.eval_expr(x_before + 1/2 * self.h, y_before + 1/2 * k1 * self.h)
            k3 = self.eval_expr(x_before + 1/2* self.h, y_before + 1/2 * k2* self.h)
            k4 = self.eval_expr(x_before + self.h, y_before + k3 * self.h)
            m = 1/6 * (k1 + 2*k2 + 2*k3 + k4)
            y[i] = y_before + m * self.h
            x[i] = x[i-1] + self.h
        
        return x, y


    def solve_with_exact_solution(self):
        x, y = self.create_arrays_with_the_initial_value()
        
        for i in np.arange(1, self.n):
            y[i] = self.eval_expr(x[i-1], y[i-1])
            x[i] = x[i-1]

        return x, y
    
    
    def solve(self):
        s1 = self.implicit_euler()
        s2 = self.improved_euler()
        s3 = self.rk4()
        solutions = {"Xn": s1[0], "Euler": s1[1], "Euler Mejorado": s2[1], "RK4": s3[1]}
        if self.exact_solution is not None:
            s4 = self.solve_with_exact_solution()
            solutions["Valor Real"] = s4[1]
            solutions["Error Absoluto Euler"] = self.absolute_error(s1[1], s4[1])
            solutions["Error Absoluto Euler Mejorado"] = self.absolute_error(s1[1], s4[1])
            solutions["Error Absoluto RK4"] = self.absolute_error(s1[1], s4[1])

        return solutions
    
    
