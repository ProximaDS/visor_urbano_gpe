from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/layer1', methods=['GET'])
def get_layer1():
    # Simulamos la conversión de un shapefile a GeoJSON
    geojson_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"name": "Feature de Layer 1"},
                "geometry": {
                    "type": "Point",
                    "coordinates": [-90.0, 40.0]
                }
            }
        ]
    }
    return jsonify(geojson_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

