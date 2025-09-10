import requests

from ..dao.pokemon_dao import PokemonDao
from ..models import PokemonModel


class ApiService:

    @classmethod
    def get_pokemon_by_id(cls,pokemon_id):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
        if response.status_code == 200:
            print(response.json())
            french_name = ApiService.get_pokemon_name_in_specific_language(pokemon_id, 'fr')
            image = response.json()['sprites']['other']['official-artwork']['front_default']
            height = response.json()['height']
            weight = response.json()['weight']
            pokemon_details = (french_name, image,height,weight)
            return pokemon_details
        else:
            print("Unable to contact API")
            return []

    @classmethod
    def get_pokemons_list(cls,offset,limit):

        response = requests.get(f'https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}')

        if response.status_code == 200:

            print(response.json())

            pokemon_list = []
            for pokemon in response.json()['results']:
                id=pokemon['url'][34:][:-1]
                pokemon_details = ApiService.get_pokemon_by_id(id)
                pokemon_list.append(PokemonModel(id,pokemon['name'], pokemon_details[0], pokemon_details[1]))
                PokemonDao.save_new_pokemon(PokemonModel(id,pokemon['name'], pokemon_details[0], pokemon_details[1]))
            return pokemon_list

        else:
            print("Unable to contact API")
            return []

    @classmethod
    def get_pokemon_name_in_specific_language(cls, pokemon_id, language):

        response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}')

        if response.status_code == 200:

            print(response.json())

            names = response.json()['names']
            res = filter(lambda n: n['language']['name'] == language, names)
            res_list = list(res)
            return res_list[0]['name']

        else:
            print("Unable to contact API")
            return ''

