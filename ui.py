import streamlit as st 
from numerical_ode_solver import NumericalOdeSolver
import matplotlib.pyplot as plt
import pandas as pd

st.title("Solucionador de EDOs")

func = st.text_input(
    label="Introduzca la EDO")

n = st.number_input("n", format="%d", value=1, min_value=1)
h = st.number_input("h", format='%.3f', min_value=0.0)
x0 = st.number_input("Valor Inicial de x", format='%.4f')
y0 = st.number_input("Valor Inicial de y", format='%.4f')
exact_solution = st.text_input("Solución exacta")

exact_solution = exact_solution.replace('^', '**')
exact_solution = exact_solution.replace('t', 'x')
func = func.replace('^', '**')
func = func.replace('t', 'x')

if exact_solution == '':
    exact_solution = None 

if st.button("Resolver"):
    solver = NumericalOdeSolver(func, exact_solution=exact_solution, h=h, n=n, x0=x0, y0=y0)
    results,performance = solver.solve()
    
    fig, ax = plt.subplots(1,1) 
    # if st.checkbox("Euler", value=True):
    ax.plot(results['Xn'], results['Euler'], label='Euler')
    
    # if st.checkbox("Euler Mejorado"):
    ax.plot(results['Xn'], results['Euler Mejorado'], label='Euler Mejorado')
    
    # if st.checkbox("RK4"):
    ax.plot(results['Xn'], results['RK4'], label='Runge-Kutta')

    # if exact_solution != None and exact_solution != '' and st.checkbox("Solución Exacta"):
    ax.plot(results['Xn'], results['Valor Real'], label='Valor Real')
        
    ax.legend()
    st.pyplot(fig)

    df = pd.DataFrame(results)
    st.dataframe(df)
    
    df2 = pd.DataFrame(performance)
    st.dataframe(df2)