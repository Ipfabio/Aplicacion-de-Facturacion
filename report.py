import pandas as pd
import matplotlib.pyplot as plt

def generate_report():
    # Leer el CSV de facturas
    df = pd.read_csv('facturas.csv', names=['Nombre', 'Email', 'Monto'])

    # Generar reportes básicos
    total_facturado = df['Monto'].sum()
    facturas_por_cliente = df.groupby('Nombre').size()

    # Graficar resultados
    plt.figure(figsize=(10, 5))
    facturas_por_cliente.plot(kind='bar')
    plt.title('Facturas por Cliente')
    plt.xlabel('Cliente')
    plt.ylabel('Número de Facturas')
    plt.savefig('reporte_facturacion.png')

    print(f'Total facturado: {total_facturado}')
    print('Reporte de facturación generado y guardado como reporte_facturacion.png')

if __name__ == '__main__':
    generate_report()