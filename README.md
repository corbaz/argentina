# 🎈 Plantilla de Aplicación Streamlit

Una plantilla sencilla y personalizable para tus proyectos con Streamlit.

[![Deployed on Streamlit](https://img.shields.io/badge/Streamlit-Deployed-brightgreen)](https://argentina.streamlit.app/)

---

## 🚀 Cómo Ejecutar Localmente

### Requisitos Previos

- Asegúrate de tener Python 3.7 o una versión posterior instalada.
- Instala pip (el gestor de paquetes de Python).

### Pasos

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/corbaz/argentina.git
   cd argentina
   ```

2. **Instalar Dependencias**
   Instala las bibliotecas necesarias de Python:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la Aplicación**
   Inicia la aplicación de Streamlit:
   ```bash
   streamlit run app.py
   ```

4. **Acceder a la Aplicación**
   Abre tu navegador y dirígete a:
   ```
   http://localhost:8501
   ```

---

## 🛠️ Flujo de Trabajo para Desarrollo

### Verificar Bibliotecas Instaladas
Lista todas las bibliotecas instaladas:
```bash
pip list
```

### Eliminar Bibliotecas No Usadas
Para desinstalar una biblioteca (por ejemplo, Flask):
```bash
pip uninstall Flask
```

### Actualizar Dependencias
Si modificas `requirements.txt`, actualiza tu entorno:
```bash
pip install -r requirements.txt
```

### Actualizar Todas las Bibliotecas
Para verificar y actualizar todas las bibliotecas a sus versiones compatibles más recientes:
1. Instala `pip-review`:
   ```bash
   pip install pip-review
   ```
2. Lista las bibliotecas desactualizadas:
   ```bash
   pip-review
   ```
3. Actualiza automáticamente todas las bibliotecas:
   ```bash
   pip-review --auto
   ```

---

## 🌟 Características

- **Diseño Modular**: Componentes fácilmente personalizables.
- **Integración con Streamlit**: Listo para proyectos de visualización de datos o aprendizaje automático.
- **Requisitos Ligeros**: Dependencias mínimas para facilitar el despliegue.

---

## 📂 Estructura del Proyecto

```
project/
├── app.py               # Archivo principal de la aplicación
├── requirements.txt     # Dependencias de Python
├── README.md            # Documentación del proyecto (este archivo)
├── layout/              # Plantillas de diseño y HTML
│   └── layout.html      # Plantilla base de diseño
├── routes/              # Páginas dinámicas de la aplicación con sus rutas
│   ├── alta.html
│   ├── consulta.html
│   ├── modificación.html
│   └── baja.html
```

---

## 🌐 Despliega tu Aplicación

Despliega fácilmente tu aplicación en Streamlit Cloud:

1. Sube tu código a un repositorio público en GitHub.
2. Ve a [Streamlit Cloud](https://streamlit.io/cloud) y conecta tu repositorio.
3. ¡Despliega y comparte el enlace de tu aplicación!

---

## 👨‍💻 Contribuidores

- **[Tu Nombre](https://github.com/corbaz)** - Creador

Siéntete libre de contribuir enviando problemas o solicitudes de extracción.

---

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
