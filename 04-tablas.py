import pandas as pd
import plotly.express as px
import streamlit as st

# ============================================================
#  SECCIÓN 1: Tabla de temperaturas semanales
#  DataFrame con temperaturas máximas y mínimas de lun a dom,
#  tabla interactiva y gráfico de líneas con Plotly.
# ============================================================

# Creamos el DataFrame con todos los días de la semana.
df = pd.DataFrame({
    "Día": ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
    "Temp. Máx.": [18, 20, 17, 22, 19, 24, 21],
    "Temp. Mín.": [8, 10, 7, 11, 9, 14, 12],
})

st.header("1. Tabla de temperaturas")

# Mostramos la tabla con st.dataframe(), que permite ordenar y buscar.
st.subheader("Datos de la semana")
st.dataframe(df, use_container_width=True)

# Gráfico de líneas con Plotly que muestra ambas temperaturas.
st.subheader("Gráfico de temperaturas")
fig = px.line(
    df,
    x="Día",
    y=["Temp. Máx.", "Temp. Mín."],
    markers=True,
    labels={"value": "Temperatura (°C)", "variable": "Tipo"},
)
fig.update_layout(
    xaxis_title="Día",
    yaxis_title="Temperatura (°C)",
    legend_title=None,
)
st.plotly_chart(fig, use_container_width=True)

# Gráfico de barras con temperaturas máximas ordenadas de mayor a menor.
st.subheader("Temperaturas máximas (ordenadas)")

# Ordenamos el DataFrame por temperatura máxima descendente.
df_ordenado = df.sort_values("Temp. Máx.", ascending=False)

fig_barras = px.bar(
    df_ordenado,
    x="Día",
    y="Temp. Máx.",
    labels={"Temp. Máx.": "Temperatura (°C)"},
    category_orders={"Día": df_ordenado["Día"].tolist()},
    text_auto=True,
)
fig_barras.update_layout(
    xaxis_title="Día",
    yaxis_title="Temperatura (°C)",
)
st.plotly_chart(fig_barras, use_container_width=True)