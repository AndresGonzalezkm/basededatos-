"""from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Ruta para obtener todos los datos
@app.route('/datos', methods=['GET'])
def obtener_datos():
    # Carga los datos desde el archivo Excel
    datos = pd.read_excel('C:\Users\andre\OneDrive\Desktop\U\Python2/datos.xlsx')  # Reemplaza esta ruta con la ruta correcta a tu archivo Excel
    # Convierte los datos a formato JSON y los devuelve .... 'ruta/al/directorio/datos.xlsx'
    return jsonify(datos.to_dict(orient='records'))

# Ruta para obtener datos por ID (por ejemplo, si tu Excel tiene un ID único para cada fila)
@app.route('/datos/<int:id>', methods=['GET'])
def obtener_dato_por_id(id):
    # Carga los datos desde el archivo Excel
    datos = pd.read_excel('ruta/al/directorio/datos.xlsx')  # Reemplaza esta ruta con la ruta correcta a tu archivo Excel
    # Filtra los datos por el ID proporcionado
    dato = datos[datos['ID'] == id]
    # Convierte el dato a formato JSON y lo devuelve
    return jsonify(dato.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)"""

"""
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Ruta para obtener todos los datos
@app.route('/datos', methods=['GET'])
def obtener_datos():
    # Carga los datos desde el archivo Excel
    datos = pd.read_excel(r'C:\Users\andre\OneDrive\Desktop\U\Python2\datos.xlsx')  # Reemplaza esta ruta con la ruta correcta a tu archivo Excel
    # Convierte los datos a formato JSON y los devuelve
    return jsonify(datos.to_dict(orient='records'))

# Ruta para obtener datos por ID (por ejemplo, si tu Excel tiene un ID único para cada fila)
@app.route('/datos/<int:id>', methods=['GET'])
def obtener_dato_por_id(id):
    # Carga los datos desde el archivo Excel
    datos = pd.read_excel(r'C:\Users\andre\OneDrive\Desktop\U\Python2\datos.xlsx')  # Reemplaza esta ruta con la ruta correcta a tu archivo Excel
    # Filtra los datos por el ID proporcionado
    dato = datos[datos['ID'] == id]
    # Convierte el dato a formato JSON y lo devuelve
    return jsonify(dato.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
"""
"""
from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Ruta para obtener todos los datos
@app.route('/datos', methods=['GET'])
def obtener_datos():
    # Construye la ruta del archivo Excel
    ruta_archivo = os.path.join('C:', 'Users', 'andre', 'OneDrive', 'Desktop', 'U', 'Python2', 'parcial 2', 'datos.xlsx')
    # Carga los datos desde el archivo Excel
    datos = pd.read_excel(ruta_archivo)  
    # Convierte los datos a formato JSON y los devuelve
    return jsonify(datos.to_dict(orient='records'))

# Ruta para obtener datos por ID (por ejemplo, si tu Excel tiene un ID único para cada fila)
@app.route('/datos/<int:id>', methods=['GET'])
def obtener_dato_por_id(id):
    # Construye la ruta del archivo Excel
    ruta_archivo = os.path.join('C:', 'Users', 'andre', 'OneDrive', 'Desktop', 'U', 'Python2', 'parcial 2', 'datos.xlsx')
    # Carga los datos desde el archivo Excel
    datos = pd.read_excel(ruta_archivo)  
    # Filtra los datos por el ID proporcionado
    dato = datos[datos['ID'] == id]
    # Convierte el dato a formato JSON y lo devuelve
    return jsonify(dato.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
"""
"""
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Carga de datos desde el archivo CSV
datos = pd.read_csv('C:\Users\andre\OneDrive\Desktop\U\Python2\parcial 2\API_SH.IMM.MEAS_DS2_en_excel_v2_50281.xlsx')  # Reemplaza esta ruta con la ruta correcta a tu archivo CSV

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
    app.run(debug=True)"""


from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Carga de datos desde el archivo Excel
datos = pd.read_excel(r'c:/Users/andre/OneDrive/Desktop/U/Python2/parcial 2/API_SH.IMM.MEAS_DS2_en_excel_v2_50281.xls', header= None)  # Reemplaza esta ruta con la ruta correcta a tu archivo Excel

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
    app.run(debug=True, port=8080)  # Cambiar el puerto a 8080 (o cualquier otro número)


