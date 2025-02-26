import folium
import requests

# Coordenadas centrales del mapa (ajusta según la extensión de tu raster)
centro = [25.671658916865567, -100.24925884994464]
m = folium.Map(location=centro, zoom_start=14)

# Cargar capa 1 (por ejemplo, GeoJSON) desde microservice1
try:
    response1 = requests.get("http://microservice1:5001/layer1")
    data1 = response1.json()
    folium.GeoJson(data1, name="Layer 1").add_to(m)
except Exception as e:
    print("Error al cargar Layer 1:", e)

# Cargar capa 2 (por ejemplo, GeoJSON) desde microservice2
try:
    response2 = requests.get("http://microservice2:5002/layer2")
    data2 = response2.json()
    folium.GeoJson(data2, name="Layer 2").add_to(m)
except Exception as e:
    print("Error al cargar Layer 2:", e)

# URL de los tiles servidos por el microservicio4
tile_url = 'http://localhost:8000/tiles/{z}/{x}/{y}.png'

folium.raster_layers.TileLayer(
    tiles=tile_url,
    attr='Tiles GDAL',
    name='Raster Tiles',
    overlay=True,
    control=True,
    tms=True,
    min_zoom=14,
    max_zoom=20
).add_to(m)

folium.LayerControl().add_to(m)
m.save("mapa_con_tiles.html")
print("Mapa guardado en mapa_con_tiles.html")
