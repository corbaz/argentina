import streamlit as st
from flask import Flask, request
from threading import Thread

# Crear la app de Flask
flask_app = Flask(__name__)

@flask_app.route('/backend', methods=['GET'])
def backend():
    nombre = request.args.get('nombre', 'Invitado')
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bienvenido</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f7f9fc;
            }}
            .container {{
                background-color: white;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bienvenido, {nombre}!</h1>
        </div>
    </body>
    </html>
    """

# Ejecutar el servidor Flask en un subproceso
def run_flask():
    flask_app.run(port=5000, debug=False, use_reloader=False)

# Iniciar Flask en segundo plano
flask_thread = Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

# Streamlit App
st.title("Streamlit + Flask")
st.write("Esta es la página inicial de Streamlit.")

# Entrada de nombre
nombre = st.text_input("Introduce tu nombre:", placeholder="Escribe tu nombre aquí")

# Botón para redirigir a la página de Flask
if st.button("Enviar"):
    if nombre:
        flask_url = f"http://127.0.0.1:5000/backend?nombre={nombre}"
        st.markdown(f"[Ir a la página de bienvenida en Flask]({flask_url})", unsafe_allow_html=True)
    else:
        st.error("Por favor, ingresa tu nombre.")
