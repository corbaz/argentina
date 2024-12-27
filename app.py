import streamlit as st

# Estilo personalizado para Streamlit
st.markdown(
    """
    <style>
        .container {
            background-color: #f7f9fc;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 400px;
            margin: auto;
            font-family: Arial, sans-serif;
        }
        .input-text {
            margin: 10px 0;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 8px;
            width: 100%;
        }
        .submit-button {
            background-color: #4caf50;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
            cursor: pointer;
        }
        .submit-button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Formulario HTML incrustado en Streamlit
st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown("<h2>Ingresa tu Nombre</h2>", unsafe_allow_html=True)

# Crear el formulario con componentes de Streamlit
name = st.text_input("Nombre:", placeholder="Escribe aquí tu nombre")
if st.button("Mostrar Nombre"):
    if name:
        st.success(f"Hola, {name}!")
    else:
        st.error("Por favor, ingresa tu nombre.")

st.markdown("</div>", unsafe_allow_html=True)
