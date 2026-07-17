import streamlit as st

# ============================================================
#  SECCIÓN 1: Formulario con widgets variados
#  Demostración de st.date_input, st.time_input, st.slider,
#  st.selectbox, st.multiselect y st.camera_input.
# ============================================================

st.header("1. Formulario para solicitar cita médica")

# Agrupamos todos los widgets en una caja con borde.
with st.container(border=True):
    st.subheader("Completa los siguientes datos")

    # st.date_input — Selector de fecha con calendario desplegable.
    fecha = st.date_input("Ingresa tu fecha de nacimiento.")

    # st.time_input — Selector de hora con reloj desplegable.
    hora = st.time_input("Ingresa la hora de tu cita médica (aprox.)")

    # st.slider — Deslizador numérico.
    # min_value y max_value definen el rango. step define el incremento.
    nivel = st.slider(
        "Del 1 al 10, ¿cuánto le duele?",
        min_value=0,
        max_value=10,
        value=5,
        step=1,
    )

    # st.selectbox — Lista desplegable para elegir una sola opción.
    pais = st.selectbox(
        "País",
        ["Argentina", "Chile", "Uruguay", "Paraguay", "Bolivia"],
    )

    # st.multiselect — Lista desplegable para elegir varias opciones.
    # Devuelve una lista con las opciones seleccionadas.
    intereses = st.multiselect(
        "Dolencias o síntomas que presenta (puede elegir varias):",
        ["Fiebre", "Dolor de cabeza", "Náuseas", "Fatiga", "Tos", "Dolor muscular o articular"],
    )

    # st.camera_input — Accede a la cámara del dispositivo.
    # Devuelve los bytes de la imagen o None si no se tomó ninguna.
    selfie = st.camera_input("Tomate una selfie")

    # Botón para mostrar el resumen de lo completado.
    if st.button("Enviar", type="primary"):
        st.success("Formulario enviado correctamente.", icon=":material/check_circle:")

        st.write(f"**Fecha:** {fecha}")
        st.write(f"**Hora:** {hora}")
        st.write(f"**Nivel de energía:** {nivel}%")
        st.write(f"**País:** {pais}")
        st.write(
            f"**Intereses:** {', '.join(intereses) if intereses else 'Ninguno'}"
        )

        if selfie:
            st.image(selfie, caption="Tu selfie", width=300)
