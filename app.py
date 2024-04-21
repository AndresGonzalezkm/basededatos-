from flask import Flask, render_template, request, redirect, url_for
import redis
import os

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Aplicación de Registro de Artículos</title>
    </head>
    <body>
        <h1>Aplicación de Registro de Artículos</h1>
        <form action="/registrar" method="post">
            <label for="nombre">Nombre del artículo:</label>
            <input type="text" id="nombre" name="nombre"><br>
            <label for="precio">Precio del artículo:</label>
            <input type="text" id="precio" name="precio"><br>
            <input type="submit" value="Registrar">
        </form>
        <!-- Otros formularios para buscar, editar y eliminar -->
        <br>
        <a href="/articulos">Ver Artículos</a>
    </body>
    </html>
    """

@app.route('/registrar', methods=['POST'])
def registrar_articulo():
    nombre = request.form['nombre']
    precio = float(request.form['precio'])
    articulo = {"nombre": nombre, "precio": precio}
    redis_client.hmset(nombre, articulo)
    return redirect(url_for('index'))

@app.route('/buscar', methods=['POST'])
def buscar_articulo():
    nombre = request.form['nombre']
    articulo = redis_client.hgetall(nombre)
    if articulo:
        return f"Resultado de la búsqueda:<br>{articulo}"
    else:
        return "No se encontró ningún artículo con ese nombre."

@app.route('/editar', methods=['POST'])
def editar_articulo():
    nombre = request.form['nombre']
    nuevo_nombre = request.form['nuevo_nombre']
    nuevo_precio = float(request.form['nuevo_precio'])
    if redis_client.exists(nombre):
        articulo = {"nombre": nuevo_nombre, "precio": nuevo_precio}
        redis_client.hmset(nuevo_nombre, articulo)
        if nuevo_nombre != nombre:
            redis_client.delete(nombre)
        return "Artículo editado exitosamente."
    else:
        return "No se encontró ningún artículo con ese nombre."

@app.route('/eliminar', methods=['POST'])
def eliminar_articulo():
    nombre = request.form['nombre']
    if redis_client.exists(nombre):
        redis_client.delete(nombre)
        return "Artículo eliminado exitosamente."
    else:
        return "No se encontró ningún artículo con ese nombre."

@app.route('/articulos', methods=['GET', 'POST'])
def ver_articulos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        if redis_client.exists(nombre):
            redis_client.delete(nombre)
            return redirect(url_for('ver_articulos'))
        else:
            return "No se encontró ningún artículo con ese nombre."
    else:
        keys = redis_client.keys('*')
        articulos = []
        for key in keys:
            if redis_client.type(key) == b'hash':
                articulo = redis_client.hgetall(key)
                articulos.append(articulo)
        
        return render_template('ver_articulos.html', articulos=articulos)

if __name__ == "__main__":
    app.run(debug=True)
