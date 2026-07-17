import streamlit as st
from datetime import date


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


# ============================================================
#  SECCIÓN 3: Calculadora de año de nacimiento
#  Un mini-formulario dentro de una caja con borde que pide
#  la edad al usuario y calcula su año de nacimiento aproximado.
# ============================================================

st.divider()
st.header("3. Calculadora de año de nacimiento")

# Creamos una caja con borde para agrupar el formulario.
with st.container(border=True):
    # Título de la sección dentro de la caja
    st.subheader("¿En qué año naciste aproximadamente?")

    # Pedimos la edad actual con un input numérico.
    # Los parámetros min_value y max_value evitan valores absurdos.
    edad = st.number_input(
        "Ingresa tu edad actual:",
        min_value=0,
        max_value=120,
        value=25,
        step=1,
    )

    # Preguntamos si ya cumplió años este año. Esto afina el cálculo:
    # - Si ya cumplió: año_nacimiento = año_actual - edad
    # - Si aún no cumple: año_nacimiento = año_actual - edad - 1
    ya_cumplio = st.checkbox("¿Ya cumpliste años este año?", value=True)

    # Obtenemos el año actual usando el módulo datetime.
    año_actual = date.today().year

    # Calculamos el año de nacimiento según la respuesta.
    if ya_cumplio:
        año_nacimiento = año_actual - edad
    else:
        año_nacimiento = año_actual - edad - 1

    # Mostramos el resultado en una caja verde.
    st.success(
        f"Naciste en el año **{año_nacimiento}**.",
        icon=":material/calendar_today:",
    )

    # También mostramos el desglose del cálculo para que se entienda.
    st.caption(
        f"Cálculo: {año_actual} (año actual) - {edad} (tu edad)"
        f"{' - 1 (aún no cumples)' if not ya_cumplio else ''}"
        f" = {año_nacimiento}"
    )
