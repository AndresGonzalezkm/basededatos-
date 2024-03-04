from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Definición de la clase Receta que representa la tabla recetas en la base de datos
class Receta(Base):
    __tablename__ = 'recetas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    ingredientes = Column(String)
    pasos = Column(String)

# Función para inicializar o crear la base de datos
def inicializar_base_datos():
    engine = create_engine('sqlite:///recetas.db', echo=True)
    Base.metadata.create_all(engine)

# Función para agregar una nueva receta
def agregar_receta(session):
    nombre = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes: ")
    pasos = input("Ingrese los pasos: ")

    nueva_receta = Receta(nombre=nombre, ingredientes=ingredientes, pasos=pasos)
    session.add(nueva_receta)
    session.commit()

# Función para actualizar una receta existente
def actualizar_receta(session):
    id_receta = int(input("Ingrese el ID de la receta que desea actualizar: "))
    nombre = input("Ingrese el nuevo nombre de la receta: ")
    ingredientes = input("Ingrese los nuevos ingredientes: ")
    pasos = input("Ingrese los nuevos pasos: ")

    receta = session.query(Receta).filter_by(id=id_receta).first()
    if receta:
        receta.nombre = nombre
        receta.ingredientes = ingredientes
        receta.pasos = pasos
        session.commit()
    else:
        print("Receta no encontrada.")

# Función para eliminar una receta existente
def eliminar_receta(session):
    id_receta = int(input("Ingrese el ID de la receta que desea eliminar: "))
    
    receta = session.query(Receta).filter_by(id=id_receta).first()
    if receta:
        session.delete(receta)
        session.commit()
    else:
        print("Receta no encontrada.")

# Función para ver el listado de recetas
def ver_recetas(session):
    recetas = session.query(Receta).all()
    for receta in recetas:
        print("ID:", receta.id)
        print("Nombre:", receta.nombre)
        print("Ingredientes:", receta.ingredientes)
        print("Pasos:", receta.pasos)
        print("")

# Función para buscar ingredientes y pasos de una receta
def buscar_receta(session):
    palabra_clave = input("Ingrese la palabra clave para buscar en las recetas: ")

    recetas = session.query(Receta).filter(
        text("ingredientes LIKE :palabra_clave OR pasos LIKE :palabra_clave")).params(palabra_clave=f'%{palabra_clave}%').all()

    if recetas:
        print("Recetas encontradas:")
        for receta in recetas:
            print("ID:", receta.id)
            print("Nombre:", receta.nombre)
            print("Ingredientes:", receta.ingredientes)
            print("Pasos:", receta.pasos)
            print("")
    else:
        print("No se encontraron recetas que coincidan con la palabra clave.")

# Función principal para ejecutar la aplicación
def main():
    inicializar_base_datos()
    engine = create_engine('sqlite:///recetas.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

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
            agregar_receta(session)
        elif opcion == 'b':
            actualizar_receta(session)
        elif opcion == 'c':
            eliminar_receta(session)
        elif opcion == 'd':
            ver_recetas(session)
        elif opcion == 'e':
            buscar_receta(session)
        elif opcion == 'f':
            session.close()
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
