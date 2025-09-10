
from django.shortcuts import render

from .services.api_service import ApiService


# Create your views here.
def index(request):

    pokemons_list = ApiService().get_pokemons_list()

    title='Pokedex!'
    context={'title':title, 'pokemons_list':pokemons_list}
    return render(request, 'PokedexApplication/index.html', context)

def pokemon_detail(request,pokemon_id):

    pokemon = ApiService.get_pokemon_by_id(pokemon_id)

    context={'pokemon_name':pokemon.name, 'pokemon_image':pokemon.image}
    return render(request, 'PokedexApplication/pokemon_detail.html', context)