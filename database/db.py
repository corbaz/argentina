import sqlite3

import streamlit as st

# Crear la conexión a la base de datos
conn = sqlite3.connect("database/usuarios.sqlite")
cursor = conn.cursor()

# Crear una tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")
conn.commit()

# Interfaz de Streamlit
st.title("Gestión de Usuarios con SQLite")

# Formulario para agregar usuarios
st.header("Agregar Usuario")
nombre = st.text_input("Nombre")
email = st.text_input("Email")
if st.button("Agregar"):
    try:
        cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
        conn.commit()
        st.success("Usuario agregado exitosamente")
    except sqlite3.IntegrityError:
        st.error("El email ya está registrado")

# Mostrar los usuarios
st.header("Usuarios Registrados")
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for id, nombre, email in usuarios:
    st.write(f"**ID**: {id}, **Nombre**: {nombre}, **Email**: {email}")

# Cerrar la conexión al final
conn.close()
