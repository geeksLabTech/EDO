import streamlit as st 
from numerical_ode_solver import NumericalOdeSolver

st.title("Solucionador de EDOs")

func = st.text_input(
    label="Introduzca la EDO",
    help="Ejemplo: 2xy"
    )

n = st.number_input("n")
h = st.number_input("h")
x0 = st.number_input("Valor Inicial de x")
y0 = st.number_input("Valor Inicial de y")


if st.button("Resolver"):
    solver = NumericalOdeSolver(func, h, n, x0, y0)
    results = solver.solve()
    

