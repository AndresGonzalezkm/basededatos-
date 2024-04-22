import requests

def get_smallest_starship_name():
    url = "https://swapi.dev/api/films/1/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Iterar sobre cada URL de nave espacial en la lista de 'starships'
        smallest_length = float('inf')  # Inicializar con un valor grande
        smallest_starship_name = None
        for starship_url in data['starships']:
            starship_response = requests.get(starship_url)
            if starship_response.status_code == 200:
                starship_data = starship_response.json()
                # Actualizar la nave espacial más pequeña si encontramos una con longitud menor
                if float(starship_data['length']) < smallest_length:
                    smallest_length = float(starship_data['length'])
                    smallest_starship_name = starship_data['name']
            else:
                print("Error al obtener información de la nave espacial:", starship_url)
        return smallest_starship_name
    else:
        print("Error al obtener información de la API")
        return None

# Respuesta a la pregunta c)
print("c) La aeronave más pequeña en la primera película se llama:", get_smallest_starship_name())
