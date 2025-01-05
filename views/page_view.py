import streamlit as st
from pathlib import Path

""" Clase que representa la vista de la página dinámica"""
""" Renderizar el layout con contenido dinámico """
class PageView:
    """ Constructor de la clase PageView """
    """ self -> Objeto de la clase PageView. """
    """ El self se utiliza para acceder a las variables y métodos de la propia clase. """
    """ __init__ -> Es el constructor de la clase."""
    """ Y self se utiliza para inicializar los atributos de la clase. """
    def __init__(self):
        self.layout_path = Path("layout/layout.html")
    
    def load_html(self, file_path):
        """Función para leer archivos HTML"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "<h1>Error: Archivo no encontrado</h1>"
    
    def render_layout(self):
        """Renderizar el layout con contenido dinámico"""
        # Obtener la página actual desde el controlador
        current_page = st.session_state.get("page", "alta")
        page_path = Path(f"routes/{current_page}.html")
        
        # Cargar el layout y el contenido
        layout_html = self.load_html(self.layout_path)
        page_content = self.load_html(page_path)
        
        # Combinar layout y contenido
        full_page = layout_html.replace("{{ content }}", page_content)
        
        # Renderizar el HTML completo
        st.components.v1.html(full_page, height=800, scrolling=True)
