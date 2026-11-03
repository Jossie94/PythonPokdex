from Pokedex.Models.Color import Color
from Pokedex.Models.Pokémon import Pokémon
from Pokedex.Models.Type import Type

def test_pokemon_get():
    #Arrange/Act
    charmander = Pokémon(
        "Charmander",
        Type.Fire,
        Color.Red,
        5,
        6,
        2
    )
    # Assert
    assert charmander.get_name() == "Charmander"
    assert charmander.get_type() == Type.Fire
    assert charmander.get_color() == Color.Red
    assert charmander.get_height() == 5
    assert charmander.get_weight() == 6
    assert charmander.get_pokedexNr() == 2

def test_pokemon_set():
    #Arrange
    squirtle = Pokémon(
        "Squirtle",
        Type.Water,
        Color.Blue,
        4,
        10,
        3
    )
    # Act
    squirtle.set_name("Wartortle")
    squirtle.set_height(8.0)
    squirtle.set_weight(11.5)

    # Assert
    assert squirtle.get_name() == "Wartortle"
    assert squirtle.get_height() == 8.0
    assert squirtle.get_weight() == 11.5

def test_invalid_height():
    # Arrange
    bulbasaur = Pokémon(
        "Bulbasaur",
        Type.Grass,
        Color.Green,
        2.0,
        6.0,
        1
    )
    # Act
    bulbasaur.set_height(-10)
    # Assert
    assert bulbasaur.get_height() == 2.0

def test_invalid_weight():
    # Arrange
    pidgey = Pokémon(
        "Pidgey",
        Type.Flying,
        Color.White,
        5.00,
        6.0, # En stor pidgey.... bruger Meter og Kg 
        4
    )
    # Act
    pidgey.set_weight(-20)

    # Assert
    assert pidgey.get_weight() == 6.00
