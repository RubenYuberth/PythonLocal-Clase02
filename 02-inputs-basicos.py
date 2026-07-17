import streamlit as st
from datetime import date

# ============================================================
#  SECCIÓN 1: st.text_input() — Entrada de texto básica
#  El widget más simple para que la persona escriba texto.
#  Cada vez que se escribe, la app se re-ejecuta y la variable
#  se actualiza automáticamente.
# ============================================================

st.header("1. Entrada de texto con st.text_input()")

# st.text_input() — Una caja de texto de una sola línea.
# El primer argumento es la etiqueta (label) que aparece arriba.
# El valor devuelto es un string con lo que la persona escribió.
nombre = st.text_input("¿Cómo te llamas?")

# Si el input está vacío, mostramos un mensaje pidiendo que escriba.
# Si ya escribió algo, lo saludamos con el nombre ingresado.
if nombre:
    st.success(f"¡Hola, {nombre}! Bienvenido/a.", icon=":material/waving_hand:")
else:
    st.info("Escribe tu nombre en la caja de arriba.", icon=":material/edit:")

# También se puede usar el parámetro `placeholder` para mostrar
# un texto de ejemplo dentro de la caja (desaparece al escribir).
apellido = st.text_input("¿Y tu apellido?", placeholder="Escribe tu apellido acá...")

if apellido:
    nombre_completo = f"{nombre} {apellido}" if nombre else apellido
    st.caption(f"Nombre completo: **{nombre_completo}**")

# ----------------------------------------------------------
#  Resumen de parámetros útiles de st.text_input()
# ----------------------------------------------------------
with st.expander("Ver parámetros de st.text_input()"):
    st.write("**st.text_input(label, value, placeholder, disabled, label_visibility)**")
    st.write("- **label**: texto que aparece arriba del input.")
    st.write("- **value**: valor inicial del input.")
    st.write("- **placeholder**: texto de ejemplo dentro del input.")
    st.write("- **disabled**: si es True, el input no se puede editar.")
    st.write("- **label_visibility**: 'visible', 'hidden' o 'collapsed'.")

# ============================================================
#  SECCIÓN 2: Calculadora de año de nacimiento
#  Un mini-formulario dentro de una caja con borde que pide
#  la edad al usuario y calcula su año de nacimiento aproximado.
# ============================================================

st.divider()
st.header("2. Calculadora de año de nacimiento")

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
