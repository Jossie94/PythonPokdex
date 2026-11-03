from Pokedex.Models.Color import Color
from Pokedex.Models.Pokémon import Pokémon
from Pokedex.Models.Type import Type

def test_pokemon_attributes():
    charmander = Pokémon(
        "Charmander",
        Type.Fire,
        Color.Red,
        5,
        6,
        2
    )

    assert charmander.get_name() == "Charmander"
    assert charmander.get_type() == Type.Fire
    assert charmander.get_color() == Color.Red
    assert charmander.get_height() == 5
    assert charmander.get_weight() == 6
    assert charmander.get_pokedexNr() == 2
