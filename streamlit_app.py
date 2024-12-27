
#
# st.title("🎈 julio.corbaz@gmail.com 📌")
# st.write(
#     "¡Empecemos a construir! Para obtener ayuda e inspiración, dirígete a [docs.streamlit.io](https://docs.streamlit.io/)."
# )


from flask import Flask, request, render_template_string
import streamlit as st
app = Flask(__name__)

# Plantilla HTML
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Input Nombre</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f4f8;
        }
        .container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        input[type="text"] {
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 8px;
            width: 100%;
            max-width: 300px;
        }
        button {
            margin-top: 10px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            background-color: #4caf50;
            color: white;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #45a049;
        }
        p {
            margin-top: 20px;
            font-size: 18px;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Ingresa tu Nombre</h1>
        <form method="POST">
            <input type="text" name="name" placeholder="Escribe aqui tu nombre aquí">
            <button type="submit">Mostrar Nombre</button>
        </form>
        {% if name %}
        <p>Hola, {{ name }}!</p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    st.title("🎈 julio.corbaz@gmail.com 📌")
    name = None
    if request.method == "POST":
        name = request.form.get("name")
    return render_template_string(html_template, name=name)

if __name__ == "__main__":
    app.run(debug=True)
