from flask import Flask, send_from_directory, abort, jsonify
import os

app = Flask(__name__)

# Carpeta base donde se encuentran los tiles (en el contenedor se asume que la raíz del proyecto es /app)
tiles_folder = '/app/raster_tiles'

@app.route('/tiles/<raster>/<z>/<x>/<y>.png')
def serve_tile(raster, z, x, y):
    # Construir la ruta al tile solicitado
    file_path = os.path.join(tiles_folder, raster, z, x, f"{y}.png")
    if os.path.exists(file_path):
        # Se utiliza send_from_directory para enviar el archivo
        return send_from_directory(os.path.join(tiles_folder, raster, z, x), f"{y}.png")
    else:
        abort(404)

@app.route('/layer3')
def layer3():
    # Lista los rasters disponibles (las carpetas que se encuentran en 'raster_tiles')
    if not os.path.exists(tiles_folder):
        return jsonify({"rasters": []})
    raster_names = [name for name in os.listdir(tiles_folder) if os.path.isdir(os.path.join(tiles_folder, name))]
    
    rasters = []
    for raster in raster_names:
        # Se crea la URL plantilla para cada raster.
        rasters.append({
            "name": raster,
            "url": f"http://microservice3:5003/tiles/{raster}/{{z}}/{{x}}/{{y}}.png",
            "min_zoom": 12,  # Ajusta estos valores según corresponda
            "max_zoom": 20
        })
    return jsonify({"rasters": rasters})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=False)



