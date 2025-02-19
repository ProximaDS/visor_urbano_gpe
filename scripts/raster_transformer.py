import subprocess
import os

input_folder = r'/Users/proxima/Documents/Proxima/Clientes/UANL/raw_raster_data'
output_folder = r'/Users/proxima/Documents/Proxima/Clientes/UANL/raster_data_transformed'

# Definimos una función transform_rasters()
def transform_rasters():
    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    # Obtener lista de archivos .tif en la carpeta de entrada
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith('.tif'):
            input_tif = os.path.join(input_folder, file_name)
            projected_tif = os.path.join(
                output_folder,
                f"{os.path.splitext(file_name)[0]}_transformed.tif"
            )
            
            # Comando para proyectar a EPSG:3857
            command = f'gdalwarp -t_srs EPSG:3857 "{input_tif}" "{projected_tif}"'
            
            try:
                subprocess.run(command, shell=True, check=True)
                print('Reproyección completada:', projected_tif)
            except subprocess.CalledProcessError as e:
                print(f'Error al reproyectar {input_tif}: {e}')




