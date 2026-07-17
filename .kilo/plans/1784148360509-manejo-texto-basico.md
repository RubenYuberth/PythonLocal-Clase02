# Plan: 01-manejo-de-texto-basico.py

## Objetivo

Crear un script pedagógico que demuestre las funciones nativas de Streamlit para mostrar texto con diferentes niveles de importancia, cajas de colores (`st.info`, `st.warning`, `st.error`, `st.success`, `st.container(border=True)`), y un mini-formulario interactivo que calcule el año de nacimiento del usuario.

## Restricciones

- **Sin `st.markdown` ni HTML.** Todo se hará con la API nativa de Streamlit.
- **Sin texto coloreado inline** (no `:red[texto]`). Los colores se muestran mediante las cajas nativas.
- **Comentarios en español**, concisos y pedagógicos.
- **Extremadamente sencillo**, adecuado para una primera clase.

## Estructura del archivo

### 1. Configuración inicial (opcional pero recomendado)

```python
import streamlit as st
from datetime import date
```

### 2. Demostración de jerarquía textual

Mostrar cada nivel de importancia textual con su función correspondiente:
- `st.title("...")` — nivel 1 (más importante)
- `st.header("...")` — nivel 2
- `st.subheader("...")` — nivel 3
- `st.write("...")` — texto genérico (renderiza markdown si lo detecta, pero en este caso solo pasamos strings planos)
- `st.text("...")` — texto sin formato (monospace, sin interpretación)
- `st.caption("...")` — texto secundario, pequeño, baja importancia

Cada uno con un comentario breve explicando su propósito visual.

### 3. Demostración de cajas de colores

Usar las funciones de estado nativas, cada una con un color e ícono distintos:
- `st.info("...", icon=":material/info:")` — caja azul
- `st.warning("...", icon=":material/warning:")` — caja amarilla/naranja
- `st.error("...", icon=":material/error:")` — caja roja
- `st.success("...", icon=":material/check_circle:")` — caja verde

Y un `st.container(border=True)` como caja neutra con borde (sin color de fondo).

Cada uno con un comentario breve.

### 4. Caja interactiva: calculadora de año de nacimiento

Dentro de un `st.container(border=True)`:
- Título de sección con `st.subheader`.
- `st.number_input` para la edad (con min=0, max=120, step=1).
- `st.checkbox` para preguntar "¿Ya cumpliste años este año?".
- Cálculo: `año_actual - edad` si ya cumplió, o `año_actual - edad - 1` si no.
- Mostrar resultado con `st.write` y también dentro de una caja `st.success` o `st.info`.
- Comentarios paso a paso explicando la lógica.

### 5. Separadores

Usar `st.divider()` entre las secciones principales para organizar visualmente el contenido.

## Validación

- Ejecutar `streamlit run 01-manejo-de-texto-basico.py` y verificar que:
  - Todas las funciones de texto se renderizan correctamente con su nivel de importancia visual.
  - Las cajas de colores aparecen con sus íconos y colores correctos.
  - El formulario de edad calcula correctamente el año de nacimiento.
  - No hay errores de consola.
