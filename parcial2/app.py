
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Carga de datos desde el archivo Excel
datos = pd.read_excel(r'c/direccion en e escritorio/API_SH.IMM.MEAS_DS2_en_excel_v2_50281.xls', header= None)  # Reemplaza esta ruta con la ruta correcta a tu archivo Excel

# Ruta para obtener todos los datos
@app.route('/datos', methods=['GET'])
def obtener_datos():
    # Convierte los datos a formato JSON y los devuelve
    return jsonify(datos.to_dict(orient='records'))

# Ruta para obtener datos por ID
@app.route('/datos/<int:id>', methods=['GET'])
def obtener_dato_por_id(id):
    # Filtra los datos por el ID proporcionado
    dato = datos[datos['ID'] == id]
    # Convierte el dato a formato JSON y lo devuelve
    return jsonify(dato.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=8080) 


