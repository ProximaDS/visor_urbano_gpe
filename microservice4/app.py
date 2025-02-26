from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

# Carpeta base donde se encuentran los tiles para "corredores_verdes_transformed"
# Actualizamos la ruta para que coincida con la estructura interna del contenedor
tiles_folder = '/app/raster_tiles/corredores_verdes_transformed'

@app.route('/tiles/<z>/<x>/<y>.png')
def serve_tile(z, x, y):
    # Construir la ruta completa: /raster_tiles/corredores_verdes_transformed/{z}/{x}/{y}.png
    file_path = os.path.join(tiles_folder, z, x, f"{y}.png")
    app.logger.info("Buscando tile: %s", file_path)
    if os.path.exists(file_path):
        return send_from_directory(os.path.join(tiles_folder, z, x), f"{y}.png")
    else:
        app.logger.error("Archivo no encontrado: %s", file_path)
        abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)



