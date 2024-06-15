import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    email = data['email']
    nombre = data['nombre']
    monto = data['monto']

    # Confitgurar el servidor SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'tu_email.gmail.com'
    sender_password = 'tu_contraseña'

    # Crear el correo electrónico
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = 'Factura Generada'

    body = f'Hola {nombre}, \n\nAdjunto encontrarás la factura por el monto de {monto}. \n\nSaludos.'
    msg.attach(MIMEText(body, 'plain'))

    # Enviar el correo
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(send_email, email, msg.as_string())

    return jsonify({"message": "Correo enviado con éxito."}), 200

if __name__ == '__main__':
    app.run(port=8000)