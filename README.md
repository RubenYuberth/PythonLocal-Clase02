# Tutoriales de Streamlit con Python

Bienvenido/a a este proyecto de aprendizaje. Acá vas a encontrar una serie de tutoriales prácticos para aprender a usar **Streamlit**, una librería de Python que te permite crear aplicaciones web interactivas con poquísimo código.

Estos ejercicios están pensados para que aprendas paso a paso, sin necesidad de saber nada de desarrollo web. Solo con conocimientos básicos de Python ya estás listo/a para partir.

---

## ¿Qué necesitas?

- **Python 3.14 o superior** (revisa con `python --version`).
- **uv** como gestor de dependencias y entornos virtuales. Si aún no lo tenés, instalalo desde [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/).

---

## ¿Qué tecnologías usamos?

| Herramienta | Para qué sirve |
|-------------|----------------|
| **uv** | Gestiona el entorno virtual y las dependencias de forma rápida y sencilla. |
| **Streamlit** | Crea la interfaz web interactiva con puro Python. |
| **Pandas** | Maneja tablas y datos de forma ordenada (DataFrames). |
| **Plotly** | Genera gráficos interactivos y modernos. |

---

## Cómo empezar

### 1. Clona o descarga este proyecto

Descarga este proyecto y pega su contenido dentro de una carpeta vacía.
Luego, abre esa carpeta con Visual Studio Code.

### 2. Instala las dependencias

Con `uv` se instala todo automáticamente leyendo el archivo `pyproject.toml`:

```bash
uv sync
```

Esto crea el entorno virtual y descarga **Streamlit**, **Pandas** y **Plotly**.

### 4. Ejecuta los tutoriales

Cada archivo `.py` es una app independiente. Para correrla, usa el comando `uv run streamlit run` seguido del nombre del archivo.

Por ejemplo, para el primer tutorial:

```bash
uv run streamlit run 01-manejo-de-texto-basico.py
```

Se va a abrir tu navegador automáticamente mostrando la app. Si no se abre, copia la URL que aparece en la terminal (generalmente `http://localhost:8501`).

---

## ¿Qué aprendes en cada tutorial?

### `01-manejo-de-texto-basico.py`
Aprende a mostrar texto con distinto peso visual y cajas de colores:
- Títulos, subtítulos, párrafos, textos monoespaciados y notas al pie.
- Cajas de información, advertencia, error, éxito y contenedores con borde.

### `02-inputs-basicos.py`
Aprende a recibir datos de la persona que usa la app:
- Cajas de texto (`st.text_input`).
- Números con límites (`st.number_input`).
- Casillas de verificación (`st.checkbox`).
- Paneles expandibles (`st.expander`).
- Ejercicio práctico: calculadora de año de nacimiento.

### `03-mas-inputs.py`
Amplía los widgets interactivos con un formulario más completo:
- Selector de fecha (`st.date_input`).
- Selector de hora (`st.time_input`).
- Deslizador numérico (`st.slider`).
- Listas desplegables simples y múltiples (`st.selectbox`, `st.multiselect`).
- Acceso a la cámara (`st.camera_input`).
- Botones de acción (`st.button`).

### `04-tablas.py`
Trabajá con datos y gráficos:
- Creación de tablas con **Pandas** (`st.dataframe`).
- Gráficos de líneas interactivos con **Plotly**.
- Gráficos de barras ordenados.

---

## Estructura del proyecto

```
80-clase-02/
├── .venv/                           # Entorno virtual (se crea al ejecutar uv sync)
├── 01-manejo-de-texto-basico.py     # Tutorial 1: texto y cajas
├── 02-inputs-basicos.py             # Tutorial 2: inputs básicos
├── 03-mas-inputs.py                 # Tutorial 3: más widgets
├── 04-tablas.py                     # Tutorial 4: tablas y gráficos
├── pyproject.toml                   # Dependencias y configuración del proyecto
└── README.md                        # Este archivo
```

---

## Tips para seguir aprendiendo

- **Experimenta**: modificá los valores, cambiá los textos, agrega nuevos widgets y mira qué pasa.
- **Consulta la documentación oficial de Streamlit**: [https://docs.streamlit.io](https://docs.streamlit.io)

---

¡Éxito con el aprendizaje! Cualquier duda, revisa los comentarios dentro de cada archivo `.py`, que están escritos para guiarte paso a paso.
