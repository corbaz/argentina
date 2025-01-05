import streamlit as st
from controllers.main_controller import MainController
from views.page_view import PageView

# Inicializar el controlador y la vista
controller = MainController()
view = PageView()

# Obtener la selección del menú y actualizar la página
choice = controller.render_navigation()
controller.set_page(choice.lower())

# Renderizar la vista actual
view.render_layout()
