import streamlit as st 
from numerical_ode_solver import NumericalOdeSolver
import matplotlib.pyplot as plt

st.title("Solucionador de EDOs")

func = st.text_input(
    label="Introduzca la EDO")

n = int(st.number_input("n"))
h = st.number_input("h")
x0 = st.number_input("Valor Inicial de x")
y0 = st.number_input("Valor Inicial de y")
exact_solution = st.text_input("Solución exacta")
if exact_solution == '':
    exact_solution = None 
print(exact_solution)
if st.button("Resolver"):
    solver = NumericalOdeSolver(func, exact_solution=exact_solution, h=h, n=n, x0=x0, y0=y0)
    results = solver.solve()
    
    fig, ax = plt.subplots(1,1) 
    ax.plot(results['Xn'], results['Euler'], label='Euler')
    ax.plot(results['Xn'], results['Euler Mejorado'], label='Euler Mejorado')
    ax.plot(results['Xn'], results['RK4'], label='Runge-Kutta')
    if exact_solution != None and exact_solution != '':
        ax.plot(results['Xn'], results['Valor Real'], label='Valor Real')
    ax.legend()
    st.pyplot(fig)
    
    results['RK4']