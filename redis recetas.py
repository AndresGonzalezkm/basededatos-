import redis

# Conexión a la base de datos Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Función para agregar una nueva receta
def agregar_receta():
    nombre = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes: ")
    pasos = input("Ingrese los pasos: ")

    id_receta = r.incr("receta:id")  # Generar un nuevo ID de receta
    r.hset(f"receta:{id_receta}", "nombre", nombre)
    r.hset(f"receta:{id_receta}", "ingredientes", ingredientes)
    r.hset(f"receta:{id_receta}", "pasos", pasos)

    print("Receta agregada exitosamente.")

# Función para actualizar una receta existente
def actualizar_receta():
    id_receta = input("Ingrese el ID de la receta que desea actualizar: ")
    nombre = input("Ingrese el nuevo nombre de la receta: ")
    ingredientes = input("Ingrese los nuevos ingredientes: ")
    pasos = input("Ingrese los nuevos pasos: ")

    r.hset(f"receta:{id_receta}", "nombre", nombre)
    r.hset(f"receta:{id_receta}", "ingredientes", ingredientes)
    r.hset(f"receta:{id_receta}", "pasos", pasos)

    print("Receta actualizada exitosamente.")

# Función para eliminar una receta existente
def eliminar_receta():
    id_receta = input("Ingrese el ID de la receta que desea eliminar: ")
    
    # Verificar que la clave sea un hash antes de eliminarla
    if r.type(f"receta:{id_receta}") == b'hash':
        r.delete(f"receta:{id_receta}")
        print("Receta eliminada exitosamente.")
    else:
        print("La clave no corresponde a una receta.")

# Función para ver el listado de recetas
def ver_recetas():
    keys = r.keys("receta:*")
    for key in keys:
        # Verificar que la clave sea un hash antes de obtener sus valores
        if r.type(key) == b'hash':
            receta = r.hgetall(key)
            decoded_receta = {k.decode("utf-8"): v.decode("utf-8") for k, v in receta.items()}
            print("ID:", key.decode("utf-8").split(":")[-1])
            print("Nombre:", decoded_receta['nombre'])
            print("Ingredientes:", decoded_receta['ingredientes'])
            print("Pasos:", decoded_receta['pasos'])
            print("")
        else:
            print("La clave", key.decode("utf-8"), "no corresponde a una receta.")

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
