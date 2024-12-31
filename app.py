from pathlib import Path

import streamlit as st


# Aplicar estilos personalizados a la sidebar
def style_sidebar():
    st.markdown(
        """
        <style>
        /* Estilo de la barra lateral */
        [data-testid="stSidebar"] {
            background-color: cyan;
            padding: 10px;
            border-radius: 0 10px 10px 0;
            font-family: Arial, sans-serif;
            width: 244px;
        }
        
        /* Opciones */
        [data-testid="stMarkdownContainer"] p {
            color: blue;           /* Cambiar el color del texto */
            font-size: 20px;       /* Cambiar el tamaño del texto */
            font-weight: bold;     /* Poner el texto en negrita */
            margin: 0;             /* Quitar márgenes adicionales */
        }
        
        /* Titulo Menu (cascada para que no tome css de las opciones) */
        [data-testid="stWidgetLabel"] p {
            color: red;             /* Cambiar el color del texto */
            font-size: 38px;        /* Cambiar el tamaño del texto */
            font-weight: bold;      /* Poner el texto en negrita */
            margin: 0;              /* Quitar márgenes */
        }

        /* Estilo para cada botón de radio (input[type="radio"]) */
        [role="radiogroup"] {
            background-color: transparent; /* Fondo del grupo */
            border-radius: 0px; /* Bordes redondeados */
            padding: 5px;
            border: 0px solid #ddd; /* Borde del contenedor */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        /* Fondo al pasar el cursor sobre una opción */
        [data-baseweb="radio"]:hover {
            background-color: yellow;
            border-radius: 10px;
            width: 100%;
        }

        /* Fondo para la opción seleccionada */
        [data-baseweb="radio"] > div:first-child {
            background-color: green; /* Cambiar el fondo */
            border: 2px solid pink; /* Cambiar el borde */
            border-radius: 50%; /* Mantener circular */
            width: 20px;
            height: 20px;
            margin-left: 5px; /* Espaciado a la izquierda del radio button */
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        /* Estilo para la opción activa */
        input[type="radio"]:checked + div > div > p {
            color: #2E7D32; /* Cambiar color del texto seleccionado */
        }
        
        /* Cambiar el color de la flecha usando el atributo fill */
        [data-testid="stSidebarCollapseButton"] svg {
            fill: yellow; /* Cambiar a amarillo */
            transition: fill 0.3s ease; /* Transición suave */
        }

        /* Cambiar el color al pasar el cursor */
        [data-testid="stSidebarCollapseButton"]:hover svg {
            fill: red; /* Cambiar a rojo al hacer hover */
        }
        """,
        unsafe_allow_html=True,
    )


# Inicializar la página por defecto
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Aplicar estilos personalizados
style_sidebar()

# Menú de navegación en el sidebar
menu = ["Home", "About", "Contact"]
choice = st.sidebar.radio("Menu", menu)

# Actualizar la página actual
if choice.lower() != st.session_state["page"]:
    st.session_state["page"] = choice.lower()

# Ruta del archivo de la página actual
page_path = Path(f"routes/{st.session_state['page']}.html")

# Ruta del archivo de layout
layout_path = Path("layout/layout.html")


# Función para leer archivos HTML
def load_html(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Error: Archivo no encontrado</h1>"


# Renderizar el layout con contenido dinámico
def render_layout():
    layout_html = load_html(layout_path)  # Cargar la plantilla del layout
    page_content = load_html(page_path)  # Cargar el contenido de la página seleccionada
    full_page = layout_html.replace("{{ content }}", page_content)  # Reemplazar {{ content }}
    st.components.v1.html(full_page, height=800, scrolling=True)  # Renderizar el HTML completo


# Renderizar el diseño completo
render_layout()
