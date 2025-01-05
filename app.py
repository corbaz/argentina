from pathlib import Path
import streamlit as st
from controllers.main_controller import MainController
from views.page_view import PageView

# Estilos personalizados para la barra lateral (sidebar) y opciones.
def style_sidebar():
    st.markdown(
        """
        <style>
            /* Estilo general de la barra lateral */         
           [data-testid="stHeader"] {
                position: absolute !important; 
                top: -9999px !important; 
                left: -9999px !important; 
                visibility: hidden !important; 
            }

            [data-testid="stMainBlockContainer"] {
                margin: 0;
                padding: 0;
                overflow: hidden;
            }

            [data-testid="stVerticalBlock"] {
                gap: 0px; 
                background-color: white; 
            }
            
            /* Estilo de la barra lateral */
            [data-testid="stSidebar"] {
                background-color: #5B9BD5;
                padding: 20px;
                border-radius: 0 10px 10px 0;
                font-family: "Segoe UI", Arial, sans-serif;
                width: 250px;
            }
            [data-testid="stRadio"]{
                background-color: #5B9BD5;
            }

            /* Opciones del menú */
            [data-testid="stMarkdownContainer"] p {
                color: #5B9BD5;
                font-size: 14px;
                font-weight: bold;
                margin: 0;
            }
        
            /* Título del menú (estilo específico) */
            [data-testid="stWidgetLabel"] p {
                color: #4472C4;
                font-size: 18px;
                font-weight: bold;
                margin: 0;
            }
        
            /* Contenedor de botones de radio */
            [role="radiogroup"] {
                background-color: #E7E6E6;
                border-radius: 8px;
                padding: 10px;
                border: 1px solid #D9D9D9;
            }
        
            /* Fondo al pasar el cursor sobre una opción */
            [data-baseweb="radio"]:hover {
                background-color: #DCE6F1;
                border-radius: 5px;
            }
        
            /* Fondo para la opción seleccionada */
            [data-baseweb="radio"] > div:first-child {
                background-color: #9BC2E6;
                border: 2px solid #5B9BD5;
                border-radius: 50%;
                width: 20px;
                height: 20px;
                margin-left: 5px;
                display: flex;
                align-items: center;
                justify-content: center;
            }
        
            /* Texto de la opción seleccionada */
            input[type="radio"]:checked + div > div > p {
                color: #2F5597;
                font-weight: bold;
            }
        
            /* Flecha de la barra lateral */
            [data-testid="stSidebarCollapseButton"] svg {
                fill: #4472C4;
                transition: fill 0.3s ease;
            }
        
            /* Cambiar el color al pasar el cursor sobre la flecha */
            [data-testid="stSidebarCollapseButton"]:hover svg {
                fill: #D9D9D9;
            }
            </style>
        """,
        unsafe_allow_html=True,
    )

# Inicializar el controlador y la vista
controller = MainController()
view = PageView()

# Aplicar estilos
style_sidebar()

# Menú de navegación en el sidebar
menu = ["Alta", "Baja", "Consulta", "Modificación"]
choice = st.sidebar.radio("Menú de Usuarios", menu)

# Actualizar la página actual a través del controlador
controller.set_page(choice.lower())

# Renderizar la vista actual
view.render_layout()
