from Pokedex.Models.Color import Color
from Pokedex.Models.Type import Type
from Pokedex.Models.Pokémon import Pokémon

def test_create_pokemon():
    pokemon = Pokémon(
        "Bulbasaur",
        Type.Grass,
        Color.Green,
        2.0,
        6.0,
        1
    )

    assert pokemon.get_name() == "Bulbasaur"
    assert pokemon.get_type() == Type.Grass
    assert pokemon.get_color() == Color.Green
    assert pokemon.get_height() == 2.0
    assert pokemon.get_weight() == 6.0
    assert pokemon.get_pokedexNr() == 1
