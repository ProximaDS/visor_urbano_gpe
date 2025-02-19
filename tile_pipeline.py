import os
from scripts import raster_transformer, tiles_generator

def main():
    print("\nIniciando pipeline de procesamiento de raster...\n")

    # Ejecutar transformación de proyección
    print("\nEjecutando transformación de proyección...\n")
    try:
        raster_transformer.transform_rasters()
        print("\nTransformación de proyección completada.\n")
    except Exception as e:
        print(f"\nError en la transformación de proyección: {e}")
        return  # Detiene el pipeline en caso de error

    # Ejecutar generación de tiles
    print("\nEjecutando generación de tiles...\n")
    try:
        tiles_generator.generate_tiles()
        print("\nGeneración de tiles completada.\n")
    except Exception as e:
        print(f"\nError en la generación de tiles: {e}")

if __name__ == "__main__":
    main()




