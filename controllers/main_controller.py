import streamlit as st

""" Clase que representa el controlador principal de la aplicación"""
""" Su función es mantener el estado de la sesión y gestionar la navegación entre las páginas"""
class MainController:
    """ Constructor de la clase"""
    """ Inicializa el estado de la sesión con la página de Alta de Usuarios"""
    def __init__(self):
        if "page" not in st.session_state:
            st.session_state["page"] = "alta"
        self.menu = ["Alta", "Baja", "Consulta", "Modificación"]
    
    """ Actualiza la página actual en el estado de la sesión"""
    """ La función recibe el nombre de la página a la cual se desea navegar"""
    def set_page(self, page_name):
        st.session_state["page"] = page_name
    
    """ Obtiene la página actual del estado de la sesión"""
    """ La función devuelve el nombre de la página actual"""
    def get_current_page(self):
        return st.session_state.get("page", "alta")
    
    """ Renderiza el menú de navegación en la barra lateral"""
    """ Retorna la opción seleccionada por el usuario"""
    def render_navigation(self):
        return st.sidebar.radio("Menú de Usuarios", self.menu)
