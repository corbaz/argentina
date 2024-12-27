import streamlit as st

# Tailwind CDN
TAILWIND_CDN = '<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">'

# Función para renderizar el menú
def render_menu():
    st.markdown(
        """
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
        """,
        unsafe_allow_html=True,
    )

    # Menú con botones de navegación
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

# HTML para cada página
def render_html_page(title, content):
    st.markdown(
        f"""
        {TAILWIND_CDN}
        <!DOCTYPE html>
        <html>
        <head>
            <title>{title}</title>
        </head>
        <body class="bg-gray-100 flex items-center justify-center h-screen">
            <div class="bg-black shadow-md rounded-lg p-8">
                <h1 class="text-2xl font-bold text-center text-blue-500">{title}</h1>
                <p class="text-red-700 mt-4">{content}</p>
            </div>
        </body>
        </html>
        """,
        unsafe_allow_html=True,
    )

# Inicializar el estado de la página
if "page" not in st.session_state:
    st.session_state["page"] = "home"  # Página predeterminada

# Renderizar el menú
render_menu()

# Mostrar la página correspondiente con HTML y Tailwind
if st.session_state["page"] == "home":
    render_html_page("Home", "Bienvenido a la página principal.")
elif st.session_state["page"] == "about":
    render_html_page("About", "Esta es la página About. Aquí puedes escribir sobre ti o tu proyecto.")
elif st.session_state["page"] == "contact":
    render_html_page("Contact Me", "Esta es la página Contact Me. Aquí puedes proporcionar información de contacto.")
else:
    render_html_page("Error", "Página no encontrada.")
