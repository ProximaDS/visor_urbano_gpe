from flask import Flask, send_from_directory, abort, jsonify
import os

app = Flask(__name__)

# Directorio base de los tiles.
# Se asume que se ejecuta desde la raíz del proyecto "visor_urbano_gpe"
tiles_folder = os.path.join(os.getcwd(), "raster_tiles")

@app.route('/tiles/<raster>/<z>/<x>/<y>.png')
def serve_tile(raster, z, x, y):
    # Construir la ruta completa al tile solicitado
    tile_path = os.path.join(tiles_folder, raster, z, x, f"{y}.png")
    if os.path.exists(tile_path):
        directory = os.path.join(tiles_folder, raster, z, x)
        return send_from_directory(directory, f"{y}.png")
    else:
        abort(404)

@app.route('/layer3')
def layer3():
    # Lista todos los rasters disponibles en 'raster_tiles'
    if not os.path.exists(tiles_folder):
        return jsonify({"rasters": []})
    
    raster_names = [name for name in os.listdir(tiles_folder) if os.path.isdir(os.path.join(tiles_folder, name))]
    rasters = []
    for raster in raster_names:
        rasters.append({
            "name": raster,
            "url": f"http://microservice3:5003/tiles/{raster}/{{z}}/{{x}}/{{y}}.png",
            "min_zoom": 12,  # Ajusta según corresponda
            "max_zoom": 20   # Ajusta según corresponda
        })
    return jsonify({"rasters": rasters})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=False)


