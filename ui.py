import streamlit as st 
from numerical_ode_solver import NumericalOdeSolver

st.title("Solucionador de EDOs")

func = st.text_input(
    label="Introduzca la EDO",
    help="Ejemplo: 2xy"
    )

n = int(st.number_input("n"))
h = st.number_input("h")
x0 = st.number_input("Valor Inicial de x")
y0 = st.number_input("Valor Inicial de y")
exact_solution = st.text_input("Solución exacta")

if st.button("Resolver"):
    solver = NumericalOdeSolver(func, exact_solution=exact_solution, h=h, n=n, x0=x0, y0=y0)
    results = solver.solve()
    

