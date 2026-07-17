import streamlit as st


# ============================================================
#  SECCIÓN 1: Jerarquía de texto
#  Streamlit ofrece funciones con distinto peso visual.
# ============================================================

# st.title — El texto más grande y llamativo. Ideal para el título principal.
st.title("Demostración de manejo de texto en Streamlit")

# st.header — Segundo nivel de importancia. Para secciones principales.
st.header("1. Jerarquía de texto")

# st.subheader — Tercer nivel. Para subsecciones dentro de un header.
st.subheader("Cada función tiene un peso visual distinto")

# st.write — Texto genérico. Es la función más versátil: acepta strings,
# números, dataframes, gráficos, etc. Para texto simple funciona igual que
# un párrafo normal.
st.write(
    "Este texto fue escrito con st.write(), la función multiuso de Streamlit. "
    "Sirve para mostrar casi cualquier cosa."
)

# st.text — Texto sin formato. Se muestra en fuente monoespaciada
# y no interpreta ningún tipo de marcado. Ideal para mostrar código o logs.
st.text("Este texto fue escrito con st.text(), que usa fuente monoespaciada.")

# st.caption — Texto pequeño y de bajo contraste. Se usa para notas al pie,
# metadatos, aclaraciones o información secundaria.
st.caption("Este es un caption: texto pequeño para notas o aclaraciones.")

# ----------------------------------------------------------
#  Resumen visual de la jerarquía
# ----------------------------------------------------------
st.subheader("Resumen de la jerarquía (de mayor a menor importancia)")

st.write("1. st.title → el más grande")
st.write("2. st.header → segundo nivel")
st.write("3. st.subheader → tercer nivel")
st.write("4. st.write → texto de cuerpo")
st.write("5. st.text → monoespaciado")
st.write("6. st.caption → nota al pie")


# ============================================================
#  SECCIÓN 2: Cajas de colores
#  Streamlit incluye funciones para mostrar mensajes con
#  distintos colores e íconos según su propósito.
# ============================================================

st.divider()
st.header("2. Cajas de colores")

# st.info — Caja azul. Para información general o instrucciones.
st.info(
    "Esto es st.info(): una caja azul para información general.",
    icon=":material/info:",
)

# st.warning — Caja amarilla/naranja. Para advertencias o precauciones.
st.warning(
    "Esto es st.warning(): una caja amarilla para advertencias.",
    icon=":material/warning:",
)

# st.error — Caja roja. Para errores o problemas que bloquean el flujo.
st.error(
    "Esto es st.error(): una caja roja para errores.",
    icon=":material/error:",
)

# st.success — Caja verde. Para confirmar que una acción se completó bien.
st.success(
    "Esto es st.success(): una caja verde para confirmaciones.",
    icon=":material/check_circle:",
)

# st.container(border=True) — Caja neutra con borde, sin color de fondo.
# Útil para agrupar visualmente contenido relacionado.
with st.container(border=True):
    st.write("Esto es st.container(border=True): una caja neutra con borde.")
    st.caption("Ideal para agrupar contenido sin un significado de estado.")

