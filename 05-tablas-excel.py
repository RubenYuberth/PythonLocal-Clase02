import pandas as pd
import streamlit as st
import plotly.express as px

# ============================================================
#  SECCIÓN 1: Cargar archivo Excel 
#  Si bien streamlit permite cargar archivos Excel,
#  en este ejemplo se importará directamente con pandas.
# ============================================================

# Cargamos el archivo Excel con pandas.
df = pd.read_excel("ventas_febrero_2026.xlsx")

# Mostramos la tabla con st.dataframe(), que permite ordenar y buscar.
st.header("1. Tabla de ventas en febrero 2026")
st.subheader("Datos de ventas")
st.dataframe(df, use_container_width=True)

# ============================================================
#  SECCIÓN 2: Gráfico de ventas por día
#  Gráfico de líneas con Plotly que muestra las ventas por día.
# ============================================================

st.header("2. Gráfico de ventas por día")

# Gráfico de líneas con Plotly que muestra las ventas por día.
fig = px.line(df, x="Fecha", y="Venta Total", markers=True, labels={"Venta Total": "Venta Total (CLP)"})

fig.update_layout(
    xaxis_title="Fecha",
    yaxis_title="Venta Total (CLP)",
)

st.plotly_chart(fig, use_container_width=True)
