import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configurar la autenticación con Google Sheets
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/creads.json', scope)
client = gspread.authorize(creds)

sheet = client.open('nombre de tu Hoja de Cálculo').sheet1

@app.route('/api/google_sheets', methods=[POST])
def add_to_google_sheets():
    data = request.get_json()
    nombre = data['nombre']
    email = data['email']
    monto = data['monto']

    # Añadir datos a la hoja de cálculo
    sheet.append_row([nombre, email, monto])

    return jsonify(["message": "Registro añadido a Google Sheets"]), 200

if __name__ == "__main__":
    app.run(port=8000)