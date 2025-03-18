from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

sensor_data = [
    {'id': 4, 'date': '04-01-2024', 'unit': '°C', 'measurement': 25.5},
    {'id': 3, 'date': '17-02-2024', 'unit': 'm/s', 'measurement': 1.2},
    {'id': 5, 'date': '05-11-2024', 'unit': 'bar', 'measurement': 1.8},
    {'id': 2, 'date': '25-09-2024', 'unit': 'l/m^2', 'measurement': 15},
    {'id': 6, 'date': '06-06-2024', 'unit': 'ppm', 'measurement': 300},
    {'id': 1, 'date': '09-10-2024', 'unit': 'l/m^2', 'measurement': 10}
]

@app.route('/sensor_data', methods=['GET'])
def get_sensor_full():
    return jsonify(sensor_data)

@app.route('/sensor_data/<int:id>', methods=['GET'])
def get_sensor_by_id(id: int):
    sensor = get_sensor_id(id)
    if sensor is None:
        return jsonify({'error': 'Sensor does not exist'}), 404
    return jsonify(sensor)

def get_sensor_id(id):
    return next((e for e in sensor_data if e['id'] == id), None)

@app.route('/getLastMeasureBySensor', methods=['GET'])
def get_last_measure_by_sensor():
    now = datetime.now()

    latest_measure = max(sensor_data, key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y') if datetime.strptime(x['date'], '%d-%m-%Y') <= now else datetime.min)

    return jsonify({
        'code': latest_measure['id'],
        'fechamuestreo': latest_measure['date'],
        'unidad': latest_measure['unit'],
        'medicion': latest_measure['measurement']
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
