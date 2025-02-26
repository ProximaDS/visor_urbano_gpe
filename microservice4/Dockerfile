FROM python:3.11-slim

WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia todo el contenido (incluyendo app.py y la carpeta que contiene los tiles)
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Inicia la aplicación
CMD ["python", "app.py"]

