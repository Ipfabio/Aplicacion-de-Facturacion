¡Por supuesto! A continuación, te proporciono una sección adicional en el README que explica las clases y funciones principales de cada script, así como enlaces a recursos donde puedes aprender más sobre cada módulo o librería utilizada.

---

# Sistema de Facturación Personalizado con Python

Este proyecto es un sistema de facturación personalizado desarrollado con Python. Utiliza diversas bibliotecas y servicios para generar facturas, registrar datos en Google Sheets y CSV, enviar correos electrónicos y generar reportes de facturación.

## Estructura del Proyecto

El proyecto está compuesto por los siguientes scripts:

1. `app.py`: Script frontal utilizando Streamlit para la interfaz de usuario.
2. `google_sheets.py`: Script para interactuar con Google Sheets.
3. `csv_handler.py`: Script para interactuar con archivos CSV.
4. `send_email.py`: Script para enviar correos electrónicos con las facturas.
5. `generate_report.py`: Script para generar un reporte de la facturación.

## Requisitos Previos

Asegúrate de tener instalado Python y las siguientes librerías:

- `streamlit`
- `requests`
- `flask`
- `gspread`
- `oauth2client`
- `pandas`
- `matplotlib`

Puedes instalarlas ejecutando:

```bash
pip install streamlit requests flask gspread oauth2client pandas matplotlib
```

## Configuración

### Google Sheets

Para interactuar con Google Sheets, necesitarás configurar las credenciales:

1. Ve a [Google Cloud Console](https://console.cloud.google.com/).
2. Crea un nuevo proyecto.
3. Habilita la API de Google Sheets y la API de Google Drive.
4. Crea credenciales de cuenta de servicio y descarga el archivo JSON.
5. Guarda el archivo JSON en el directorio del proyecto y renómbralo a `creds.json`.

### SMTP

Configura las credenciales del servidor SMTP en `send_email.py` para enviar correos electrónicos. Puedes usar servicios como Gmail, configurando las variables `smtp_server`, `smtp_port`, `sender_email` y `sender_password`.

## Ejecución

### 1. Ejecutar el Script de Streamlit

Este script proporciona la interfaz de usuario.

```bash
streamlit run app.py
```

### 2. Ejecutar los Servidores Flask

Los scripts `google_sheets.py`, `csv_handler.py` y `send_email.py` necesitan ejecutarse como servidores Flask.

En terminales separadas, ejecuta:

```bash
python google_sheets.py
python csv_handler.py
python send_email.py
```

### 3. Generar Reporte de Facturación

Para generar un reporte de facturación:

```bash
python generate_report.py
```

## Uso

1. Abre la aplicación Streamlit (normalmente se abrirá en `http://localhost:8501`).
2. Introduce los datos del cliente: nombre, email y monto de la factura.
3. Haz clic en "Generar Factura".
4. La aplicación validará los datos y llamará a las APIs para:
   - Crear un registro en un archivo CSV.
   - Crear un registro en Google Sheets.
   - Generar y enviar una factura al email proporcionado (opcional).
5. Para ver el reporte de facturación, ejecuta el script `generate_report.py`. Se generará un archivo `reporte_facturacion.png` con un gráfico de las facturas por cliente y el total facturado.

## Explicación de Clases y Funciones

### `app.py`

- **Funciones Principales:**
  - `main()`: Configura y ejecuta la aplicación Streamlit. Recibe datos del usuario, valida entradas, y llama a las APIs correspondientes para procesar los datos.

- **Recursos para Aprender Más:**
  - [Documentación de Streamlit](https://docs.streamlit.io/)
  - [Guía de Inicio Rápido de Streamlit](https://docs.streamlit.io/library/get-started)

### `google_sheets.py`

- **Funciones Principales:**
  - `add_to_google_sheets()`: Recibe datos a través de una solicitud POST, y los añade a una hoja de cálculo de Google Sheets utilizando `gspread`.

- **Recursos para Aprender Más:**
  - [Documentación de Gspread](https://gspread.readthedocs.io/en/latest/)
  - [Uso de API de Google Sheets](https://developers.google.com/sheets/api/guides/concepts)

### `csv_handler.py`

- **Funciones Principales:**
  - `add_to_csv()`: Recibe datos a través de una solicitud POST y los añade a un archivo CSV utilizando el módulo `csv`.

- **Recursos para Aprender Más:**
  - [Documentación del Módulo CSV](https://docs.python.org/3/library/csv.html)

### `send_email.py`

- **Funciones Principales:**
  - `send_email()`: Recibe datos a través de una solicitud POST y envía un correo electrónico con la factura utilizando `smtplib`.

- **Recursos para Aprender Más:**
  - [Documentación del Módulo Smtplib](https://docs.python.org/3/library/smtplib.html)
  - [Enviar Emails en Python](https://realpython.com/python-send-email/)

### `generate_report.py`

- **Funciones Principales:**
  - `generate_report()`: Lee los datos de facturación desde un archivo CSV utilizando `pandas`, genera un reporte y lo guarda como una imagen PNG utilizando `matplotlib`.

- **Recursos para Aprender Más:**
  - [Documentación de Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
  - [Documentación de Matplotlib](https://matplotlib.org/stable/contents.html)

## Notas Adicionales

- Asegúrate de que los puertos configurados en los scripts Flask no estén en uso por otros servicios.
- Ajusta los nombres y rutas de archivos según tus necesidades.
- Para un entorno de producción, considera usar un servidor WSGI como Gunicorn y configurar un servidor web como Nginx para manejar las solicitudes.

---

Este README ahora incluye explicaciones de las clases y funciones principales de cada script, junto con recursos adicionales para aprender más sobre cada módulo o librería utilizada en el proyecto.