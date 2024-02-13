import sqlite3

# Función para inicializar o crear la base de datos
def inicializar_base_datos():
    conexion = sqlite3.connect('recetas.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recetas (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            ingredientes TEXT,
            pasos TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

# Función para agregar una nueva receta
def agregar_receta():
    nombre = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes: ")
    pasos = input("Ingrese los pasos: ")
    
    conexion = sqlite3.connect('recetas.db')
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO recetas (nombre, ingredientes, pasos) VALUES (?, ?, ?)', (nombre, ingredientes, pasos))
    conexion.commit()
    conexion.close()

# Función para actualizar una receta existente
def actualizar_receta():
    id_receta = int(input("Ingrese el ID de la receta que desea actualizar: "))
    nombre = input("Ingrese el nuevo nombre de la receta: ")
    ingredientes = input("Ingrese los nuevos ingredientes: ")
    pasos = input("Ingrese los nuevos pasos: ")
    
    conexion = sqlite3.connect('recetas.db')
    cursor = conexion.cursor()
    cursor.execute('UPDATE recetas SET nombre=?, ingredientes=?, pasos=? WHERE id=?', (nombre, ingredientes, pasos, id_receta))
    conexion.commit()
    conexion.close()

# Función para eliminar una receta existente
def eliminar_receta():
    id_receta = int(input("Ingrese el ID de la receta que desea eliminar: "))
    
    conexion = sqlite3.connect('recetas.db')
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM recetas WHERE id=?', (id_receta,))
    conexion.commit()
    conexion.close()

# Función para ver el listado de recetas
def ver_recetas():
    conexion = sqlite3.connect('recetas.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM recetas')
    recetas = cursor.fetchall()
    conexion.close()
    
    for receta in recetas:
        print("ID:", receta[0])
        print("Nombre:", receta[1])
        print("Ingredientes:", receta[2])
        print("Pasos:", receta[3])
        print("")

# Función para buscar ingredientes y pasos de una receta
def buscar_receta():
    palabra_clave = input("Ingrese la palabra clave para buscar en las recetas: ")
    
    conexion = sqlite3.connect('recetas.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM recetas WHERE ingredientes LIKE ? OR pasos LIKE ?', ('%' + palabra_clave + '%', '%' + palabra_clave + '%'))
    recetas = cursor.fetchall()
    conexion.close()
    
    if recetas:
        print("Recetas encontradas:")
        for receta in recetas:
            print("ID:", receta[0])
            print("Nombre:", receta[1])
            print("Ingredientes:", receta[2])
            print("Pasos:", receta[3])
            print("")
    else:
        print("No se encontraron recetas que coincidan con la palabra clave.")

# Función principal para ejecutar la aplicación
def main():
    inicializar_base_datos()
    
    while True:
        print("=====================================")
        print("          LIBRO DE RECETAS           ")
        print("=====================================")
        print("a) Agregar nueva receta")
        print("b) Actualizar receta existente")
        print("c) Eliminar receta existente")
        print("d) Ver listado de recetas")
        print("e) Buscar ingredientes y pasos de receta")
        print("f) Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == 'a':
            agregar_receta()
        elif opcion == 'b':
            actualizar_receta()
        elif opcion == 'c':
            eliminar_receta()
        elif opcion == 'd':
            ver_recetas()
        elif opcion == 'e':
            buscar_receta()
        elif opcion == 'f':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
