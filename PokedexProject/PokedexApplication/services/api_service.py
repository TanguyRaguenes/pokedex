import requests

from ..models import PokemonModel


class ApiService:

    @classmethod
    def get_pokemon_by_id(cls,pokemon_id):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
        if response.status_code == 200:
            print(response.json())
            name = response.json()['forms'][0]['name']
            image = response.json()['sprites']['other']['official-artwork']['front_default']
            pokemon = PokemonModel(name=name, image=image)
            return pokemon
        else:
            print("Unable to contact API")
            return []

    @classmethod
    def get_pokemons_list(cls):

        response = requests.get('https://pokeapi.co/api/v2/pokemon')

        if response.status_code == 200:

            print(response.json())

            pokemon_list = []
            for pokemon in response.json()['results']:
                pokemon_list.append(pokemon['name'])

            return pokemon_list

        else:
            print("Unable to contact API")
            return []






