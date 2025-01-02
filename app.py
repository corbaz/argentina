from pathlib import Path

import streamlit as st


# Estilos personalizados para la barra lateral (sidebar) y opciones.
def style_sidebar():
    st.markdown(
        """
        <script>
            // Intentar manipular elementos fuera del iframe
            window.addEventListener('DOMContentLoaded', function() {
                try {
                    // Acceder al DOM global usando window.parent
                    const parentDocument = window.parent.document;
    
                    // Ocultar el contenedor del perfil
                    const profileContainer = parentDocument.querySelector('._profileContainer_gzau3_53');
                    if (profileContainer) {
                        profileContainer.style.display = 'none';
                    }
    
                    // Ocultar el botón "Manage app"
                    const manageAppButton = parentDocument.querySelector('[data-testid="manage-app-button"]');
                    if (manageAppButton) {
                        manageAppButton.style.display = 'none';
                    }
                } catch (error) {
                    console.error("No se puede acceder al DOM principal:", error);
                }
            });
        </script>
        
        <style>
        ._terminalButton_rix23_138 {
            display: none !important; /* Ocultar completamente el botón */
        }
        
        ._container_gzau3_1 {
            display: none !important; /* Oculta completamente el elemento */
        }
        
        ._profileContainer_gzau3_53 {
            display: none !important; /* Oculta completamente el elemento */
        }
        
        [data-testid="stHeader"] {
                display: none; /* Oculta el elemento */
        }
        
        /* Ocultar el botón "Manage app" */
        [data-testid="manage-app-button"] {
            display: none; /* Oculta completamente el elemento */
        }
        
        /* Estilo de la barra lateral */
        [data-testid="stSidebar"] {
            background-color: #F4F6F8; /* Fondo gris claro pastel */
            padding: 20px;
            border-radius: 0 10px 10px 0; /* Bordes redondeados solo en el lado derecho */
            font-family: "Segoe UI", Arial, sans-serif; /* Fuente similar a Office */
            width: 250px; /* Ancho fijo */
        }
    
        /* Opciones del menú */
        [data-testid="stMarkdownContainer"] p {
            color: #5B9BD5; /* Azul pastel */
            font-size: 18px; /* Tamaño moderado */
            font-weight: bold; /* Texto en negrita */
            margin: 0; /* Sin margen adicional */
        }
    
        /* Título del menú (estilo específico) */
        [data-testid="stWidgetLabel"] p {
            color: #4472C4; /* Azul oscuro pastel */
            font-size: 24px; /* Tamaño más grande para destacar */
            font-weight: bold; /* Texto en negrita */
            margin: 0;
        }
    
        /* Contenedor de botones de radio */
        [role="radiogroup"] {
            background-color: #E7E6E6; /* Gris claro pastel */
            border-radius: 8px; /* Bordes redondeados */
            padding: 10px;
            border: 1px solid #D9D9D9; /* Borde tenue */
        }
    
        /* Fondo al pasar el cursor sobre una opción */
        [data-baseweb="radio"]:hover {
            background-color: #DCE6F1; /* Azul claro pastel */
            border-radius: 5px;
        }
    
        /* Fondo para la opción seleccionada */
        [data-baseweb="radio"] > div:first-child {
            background-color: #9BC2E6; /* Azul pastel seleccionado */
            border: 2px solid #5B9BD5; /* Borde azul más oscuro */
            border-radius: 50%; /* Mantener circular */
            width: 20px;
            height: 20px;
            margin-left: 5px; /* Espaciado a la izquierda */
            display: flex;
            align-items: center;
            justify-content: center;
        }
    
        /* Texto de la opción seleccionada */
        input[type="radio"]:checked + div > div > p {
            color: #2F5597; /* Azul intenso pastel */
            font-weight: bold;
        }
    
        /* Flecha de la barra lateral */
        [data-testid="stSidebarCollapseButton"] svg {
            fill: #4472C4; /* Azul oscuro pastel */
            transition: fill 0.3s ease; /* Transición suave */
        }
    
        /* Cambiar el color al pasar el cursor sobre la flecha */
        [data-testid="stSidebarCollapseButton"]:hover svg {
            fill: #D9D9D9; /* Gris claro */
        }
        </style>
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
