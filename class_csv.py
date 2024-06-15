import csv
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/csv', method=['POST'])
def add_to_csv():
    data = request.get_json()
    nombre = data['nombre']
    email = data['email']
    monto = data['monto']

    # Añadir datos al CSV
    with open('facturas.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, email, monto])

    
    return jsonify({"message": "Registro añadido al CSV"}), 200

if __name__ == '__main__':
    app.run(port=8000)