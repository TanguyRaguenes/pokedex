
from django.shortcuts import render

from .dao.pokemon_dao import PokemonDao
from .services.api_service import ApiService


# Create your views here.
def index(request):

    offset = int(request.GET.get("offset", 0))
    limit = int(request.GET.get("limit", 5))


    pokemons_list = ApiService().get_pokemons_list(offset,limit)


    title='Pokedex!'
    context={
        'title':title,
        'pokemons_list':pokemons_list,
        'next_offset': offset + limit,
        'prev_offset': offset - limit,
        'limit': limit
    }
    return render(request, 'PokedexApplication/index.html', context)

def pokemon_detail(request,pokemon_id):

    pokemon = ApiService.get_pokemon_by_id(pokemon_id)
    pokemon_name=ApiService.get_pokemon_name_in_specific_language(pokemon_id,'fr')

    pokemon_recupere_en_bdd = PokemonDao.get_pokemon_by_id(pokemon_id)

    context={'pokemon_name':pokemon_name, 'pokemon_image':pokemon[1], 'pokemon_height':pokemon[2], 'pokemon_weight':pokemon[3]}
    return render(request, 'PokedexApplication/pokemon_detail.html', context)