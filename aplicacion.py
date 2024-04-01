import pymongo

# Conectarse a la base de datos de MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["presupuesto"]
collection = db["articulos"]

def registrar_articulo():
    nombre = input("Nombre del artículo: ")
    precio = float(input("Precio del artículo: "))
    articulo = {"nombre": nombre, "precio": precio}
    collection.insert_one(articulo)
    print("Artículo registrado exitosamente.")

def buscar_articulo():
    nombre = input("Ingrese el nombre del artículo a buscar: ")
    articulo = collection.find_one({"nombre": nombre})
    if articulo:
        print("Resultado de la búsqueda:")
        print(articulo)
    else:
        print("No se encontró ningún artículo con ese nombre.")

def editar_articulo():
    nombre = input("Ingrese el nombre del artículo a editar: ")
    nuevo_nombre = input("Nuevo nombre del artículo: ")
    nuevo_precio = float(input("Nuevo precio del artículo: "))
    collection.update_one({"nombre": nombre}, {"$set": {"nombre": nuevo_nombre, "precio": nuevo_precio}})
    print("Artículo editado exitosamente.")

def eliminar_articulo():
    nombre = input("Ingrese el nombre del artículo a eliminar: ")
    resultado = collection.delete_one({"nombre": nombre})
    if resultado.deleted_count == 1:
        print("Artículo eliminado exitosamente.")
    else:
        print("No se encontró ningún artículo con ese nombre.")

def mostrar_menu():
    while True:
        print("\n*** Menú ***")
        print("1. Registrar artículo")
        print("2. Buscar artículo")
        print("3. Editar artículo")
        print("4. Eliminar artículo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_articulo()
        elif opcion == "2":
            buscar_articulo()
        elif opcion == "3":
            editar_articulo()
        elif opcion == "4":
            eliminar_articulo()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
