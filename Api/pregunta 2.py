import requests

def count_wookies():
    url = "https://swapi.dev/api/species/3/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # La clave 'people' contiene una lista de URLs de personajes que son Wookies
        # Contamos el número de URLs en la lista para obtener el número de Wookies
        num_wookies = len(data['people'])
        return num_wookies
    else:
        print("Error al obtener información de la API")
        return None

# Respuesta a la pregunta b)
print("b) Hay", count_wookies(), "Wookies que aparecen en toda la saga.")
