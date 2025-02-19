import subprocess
import os

transformed_folder = r'/Users/proxima/Documents/Proxima/Clientes/UANL/raster_data_transformed'
tiles_output_folder = r'/Users/proxima/Documents/Proxima/Clientes/UANL/visor_urbano_gpe/raster_tiles'

def generate_tiles():
    # Crear carpeta de salida si no existe
    os.makedirs(tiles_output_folder, exist_ok=True)

    # Obtener lista de archivos .tif transformados en la carpeta de salida del primer proceso
    for file_name in os.listdir(transformed_folder):
        if file_name.lower().endswith('_transformed.tif'):
            projected_tif = os.path.join(transformed_folder, file_name)

            # Crear subcarpeta para los tiles de este archivo
            tile_folder = os.path.join(
                tiles_output_folder,
                os.path.splitext(file_name)[0]
            )
            os.makedirs(tile_folder, exist_ok=True)

            # Comando para generar los tiles
            zoom_range = '14-20'
            tile_command = f'gdal2tiles.py -z {zoom_range} -w none "{projected_tif}" "{tile_folder}"'

            try:
                subprocess.run(tile_command, shell=True, check=True)
                print("Tiles generados en la carpeta:", tile_folder)
            except subprocess.CalledProcessError as e:
                print(f'Error al generar tiles para {projected_tif}: {e}')


