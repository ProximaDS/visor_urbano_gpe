from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/layer2', methods=['GET'])
def get_layer2():
    geojson_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"name": "Feature de Layer 2"},
                "geometry": {
                    "type": "Point",
                    "coordinates": [-90.5, 40.5]
                }
            }
        ]
    }
    return jsonify(geojson_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
