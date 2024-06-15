import streamlit as st
import requests
import pandas as pd

def main():
    st.title('Sistema de Facturación')

    # Input de datos del cliente
    nombre = st.text_input('Nombre del Cliente')
    email = st.text_input('Email del Cliente')
    monto = st.number_input('Monto de la Factura', min_value=0.0)

    if st.button('Generar Factura'):
        # Validaciones
        if not nombre or not email or monto <= 0:
            st.error('Por favor, rellene todos los campos correctamente.')
        else:
            # Llamadas a las APIs
            data = {'nombre': nombre, 'email': email, 'monto': monto}

            response_csv = requests.post('http://localhost:8000/api/csv', json=data)
            response_sheet = requests.post('http://localhost:8000/api/google_sheets', json=data)
            response_invoice = requests.post('http://localhost:8000/api/generate_invoice', json=data)

            if response_csv.status_code == 200 and response_sheet.status_code == 200 and response_invoice.status_code == 200:
                st.success('Factura generada y registrada con éxito.')
            else:
                st.error('Hubo un error al generar la factura.')

if __name__ == '__main__':
    main()