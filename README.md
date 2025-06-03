# Acreditación

Aplicación sencilla en Flask para acreditar personas mediante un código QR o de forma manual. Utiliza SQLite como base de datos y Tailwind para el diseño minimalista.

## Uso

1. Instalar dependencias:
   ```bash
   pip install flask flask_sqlalchemy werkzeug
   ```
2. Ejecutar la aplicación:
   ```bash
   python app.py
   ```
3. Acceder a `http://localhost:5000` e iniciar sesión con usuario **admin** y contraseña **admin**.

Desde el panel principal se pueden ver las personas acreditadas y la cantidad total. También es posible agregar personas manualmente.
