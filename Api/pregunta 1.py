import requests

def count_arid_planet_appearances():
    url = "https://swapi.dev/api/planets/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        arid_planet_count = sum(1 for planet in data['results'] if 'arid' in planet['climate'].lower())
        return arid_planet_count
    else:
        print("Error al obtener información de la API")
        return None

# Respuesta a la pregunta a)
print("a) En", count_arid_planet_appearances(), "películas aparecen planetas cuyo clima es árido.")
