'''import folium

centro = [25.674453699177754, -100.21357677942221]
m = folium.Map(location=centro, zoom_start=12)

m.save('./docs/index.html')'''

import folium
import requests

# Crear un mapa base centrado en una ubicación
m = folium.Map(location=[40.0, -90.0], zoom_start=8)

# Consultar el microservicio 1 para obtener la capa 1
try:
    response1 = requests.get("http://microservice1:5001/layer1")
    data1 = response1.json()
    folium.GeoJson(data1, name="Layer 1").add_to(m)
except Exception as e:
    print("Error al cargar Layer 1:", e)

# Consultar el microservicio 2 para obtener la capa 2
try:
    response2 = requests.get("http://microservice2:5002/layer2")
    data2 = response2.json()
    folium.GeoJson(data2, name="Layer 2").add_to(m)
except Exception as e:
    print("Error al cargar Layer 2:", e)

# Agregar control de capas
folium.LayerControl().add_to(m)

# Guardar el mapa en un archivo HTML
m.save("index.html")
print("Mapa guardado en index.html")

