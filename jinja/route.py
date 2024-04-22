from flask import Flask, render_template, request, redirect
import redis

app = Flask(__name__)
# Conexión a la base de datos Redis
db = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        # Guardar en Redis
        db.hmset(nombre, {'cantidad': cantidad})
        return redirect('/')
    return render_template('registro.html')

@app.route('/busqueda', methods=['GET', 'POST'])
def busqueda():
    if request.method == 'POST':
        nombre = request.form['nombre']
        presupuesto = db.hgetall(nombre)
        if presupuesto:
            presupuesto_decoded = {key.decode('utf-8'): value.decode('utf-8') for key, value in presupuesto.items()}
            return render_template('resultado_busqueda.html', presupuesto=presupuesto_decoded)
        else:
            return render_template('resultado_busqueda.html', presupuesto=None)
    return render_template('busqueda.html')

@app.route('/edicion', methods=['GET', 'POST'])
def edicion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        # Actualizar en Redis
        db.hmset(nombre, {'cantidad': cantidad})
        return redirect('/')
    return render_template('edicion.html')

@app.route('/eliminacion', methods=['GET', 'POST'])
def eliminacion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        # Eliminar de Redis
        db.delete(nombre)
        return redirect('/')
    return render_template('eliminacion.html')

@app.route('/salir')
def salir():
    return "¡Hasta luego!"

if __name__ == '__main__':
    app.run(debug=True)
