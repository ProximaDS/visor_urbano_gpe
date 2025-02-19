import folium
import requests

# Crear el mapa base (ajusta la ubicación y el zoom según tus necesidades)
m = folium.Map(location=[23.6345, -102.5528], zoom_start=5)

# Cargar capa 1 desde microservice1 (por ejemplo, GeoJSON)
try:
    response1 = requests.get("http://microservice1:5001/layer1")
    data1 = response1.json()
    folium.GeoJson(data1, name="Layer 1").add_to(m)
except Exception as e:
    print("Error al cargar Layer 1:", e)

# Cargar capa 2 desde microservice2 (por ejemplo, GeoJSON)
try:
    response2 = requests.get("http://microservice2:5002/layer2")
    data2 = response2.json()
    folium.GeoJson(data2, name="Layer 2").add_to(m)
except Exception as e:
    print("Error al cargar Layer 2:", e)

# Cargar la capa de tiles (raster) desde microservice3
try:
    response3 = requests.get("http://microservice3:5003/layer3")
    data3 = response3.json()
    for raster in data3.get("rasters", []):
        tile_url = raster.get("url")  # Ejemplo: "http://microservice3:5003/tiles/corredores_verdes_transformed/{z}/{x}/{y}.png"
        layer_name = raster.get("name", "Raster")
        min_zoom = raster.get("min_zoom", 12)
        max_zoom = raster.get("max_zoom", 20)
        
        folium.raster_layers.TileLayer(
            tiles=tile_url,
            attr='Tiles GDAL',
            name=layer_name,
            overlay=True,
            control=True,
            tms=False,  # Establece en False para el esquema XYZ estándar
            min_zoom=min_zoom,
            max_zoom=max_zoom
        ).add_to(m)
except Exception as e:
    print("Error al cargar capa de raster:", e)

# Agregar control de capas para activar/desactivar cada capa
folium.LayerControl().add_to(m)

# Guardar el mapa en un archivo HTML
m.save("index.html")
print("Mapa guardado en index.html")
