from ..models import PokemonModel

class PokemonDao:

    # CREATE
    @classmethod
    def save_new_pokemon(cls, pokemon: PokemonModel):
        pokemon.save()
        return pokemon

    # READ
    @classmethod
    def get_pokemon_by_id(cls, pokemon_id: int):
        try:
            return PokemonModel.objects.get(pk=pokemon_id)
        except PokemonModel.DoesNotExist:
            return None

    @classmethod
    def get_all_pokemons(cls):
        return PokemonModel.objects.all()

    # UPDATE
    @classmethod
    def update_pokemon(cls, pokemon_id: int, **kwargs):
        try:
            pokemon = PokemonModel.objects.get(pk=pokemon_id)
            for key, value in kwargs.items():
                if hasattr(pokemon, key):
                    setattr(pokemon, key, value)
            pokemon.save()
            return pokemon
        except PokemonModel.DoesNotExist:
            return None

    # DELETE
    @classmethod
    def delete_pokemon(cls, pokemon_id: int):
        try:
            pokemon = PokemonModel.objects.get(pk=pokemon_id)
            pokemon.delete()
            return True
        except PokemonModel.DoesNotExist:
            return False