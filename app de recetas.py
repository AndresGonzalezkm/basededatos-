from pymongo import MongoClient
from bson import ObjectId
# Conexión a la base de datos MongoDB
client = MongoClient('localhost', 27017)
db = client['recetas_db']
collection = db['recetas']

# Función para agregar una nueva receta
def agregar_receta():
    nombre = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes: ")
    pasos = input("Ingrese los pasos: ")

    nueva_receta = {
        'nombre': nombre,
        'ingredientes': ingredientes,
        'pasos': pasos
    }

    collection.insert_one(nueva_receta)
    print("Receta agregada exitosamente.")

# Función para actualizar una receta existente
def actualizar_receta():
    id_receta = input("Ingrese el ID de la receta que desea actualizar: ")
    nombre = input("Ingrese el nuevo nombre de la receta: ")
    ingredientes = input("Ingrese los nuevos ingredientes: ")
    pasos = input("Ingrese los nuevos pasos: ")

    query = {'_id': ObjectId(id_receta)}
    nueva_data = {'$set': {'nombre': nombre, 'ingredientes': ingredientes, 'pasos': pasos}}

    result = collection.update_one(query, nueva_data)
    if result.modified_count > 0:
        print("Receta actualizada exitosamente.")
    else:
        print("Receta no encontrada.")

# Función para eliminar una receta existente
def eliminar_receta():
    id_receta = input("Ingrese el ID de la receta que desea eliminar: ")

    query = {'_id': ObjectId(id_receta)}
    result = collection.delete_one(query)

    if result.deleted_count > 0:
        print("Receta eliminada exitosamente.")
    else:
        print("Receta no encontrada.")

# Función para ver el listado de recetas
def ver_recetas():
    recetas = collection.find()
    for receta in recetas:
        print("ID:", receta['_id'])
        print("Nombre:", receta['nombre'])
        print("Ingredientes:", receta['ingredientes'])
        print("Pasos:", receta['pasos'])
        print("")

# Función principal para ejecutar la aplicación
def main():
    while True:
        print("=====================================")
        print("          LIBRO DE RECETAS           ")
        print("=====================================")
        print("a) Agregar nueva receta")
        print("b) Actualizar receta existente")
        print("c) Eliminar receta existente")
        print("d) Ver listado de recetas")
        print("e) Salir")
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
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
