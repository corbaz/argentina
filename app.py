
import streamlit as st
from pathlib import Path

# Ruta base de los archivos HTML
BASE_DIR = Path(__file__).resolve().parent

# Función para leer archivos HTML
def load_html(file_path):
    with open(file_path, "r") as f:
        return f.read()

# Función para renderizar el menú (Layout)
def render_menu():
    st.markdown(
        '''
        <style>
            .menu-container {
                display: flex;
                justify-content: space-around;
                background-color: #4CAF50;
                padding: 10px;
                border-radius: 8px;
                margin-bottom: 20px;
            }
            .menu-item {
                text-decoration: none;
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 10px;
                border-radius: 4px;
                cursor: pointer;
            }
            .menu-item:hover {
                background-color: #45a049;
                color: white;
            }
        </style>
        ''',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Home"):
            st.session_state["page"] = "home"
    with col2:
        if st.button("About"):
            st.session_state["page"] = "about"
    with col3:
        if st.button("Contact Me"):
            st.session_state["page"] = "contact"

# Inicializar la página por defecto
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Renderizar el layout
render_menu()

# Rutas de cada componente
if st.session_state["page"] == "home":
    html_content = load_html(BASE_DIR / "routes/home.html")
elif st.session_state["page"] == "about":
    html_content = load_html(BASE_DIR / "routes/about.html")
elif st.session_state["page"] == "contact":
    html_content = load_html(BASE_DIR / "routes/contact.html")
else:
    html_content = "<h1>Error: Página no encontrada</h1>"

# Renderizar el layout con el contenido de la ruta
layout_html = load_html(BASE_DIR / "layout/layout.html")
layout_with_content = layout_html.replace("{{ content }}", html_content)
st.markdown(layout_with_content, unsafe_allow_html=True)
