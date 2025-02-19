FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Primero se genera el mapa y luego se inicia el servidor HTTP
CMD ["sh", "-c", "python generate_map.py && python serve.py"]

