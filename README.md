# Pokédex

## Class diagram

```mermaid
classDiagram
    direction LR

    class Pokemon["Pokémon"] {
        -str __name
        -Type __type
        -Color __color
        -float __height
        -float __weight
        -int __pokedexNr
        +__init__(name, type, color, height, weight, pokedexNr)
        +get_name() str
        +get_type() Type
        +get_color() Color
        +get_height() float
        +get_weight() float
        +get_pokedexNr() int
        +set_name(name)
        +set_type(type)
        +set_color(color)
        +set_height(height)
        +set_weight(weight)
        +set_pokedexNr(pokedexNr)
        +__str__() str
    }

    class Pokedex["Pokédex"] {
        -int __pokedexNr
        -list __pokemon_list
        +__init__(pokedexNr)
        +get_pokemon_list() list
        +create_Pokémon(pokemon)
        +show_all_pokemon()
        +get_specific_pokemon(pokemon)
        +update_pokemon_name(old_name, new_name)
        +delete_pokemon(name)
        +__str__() str
    }

    class Type {
        <<enumeration>>
        Grass = 1
        Fire = 2
        Water = 3
        Flying = 4
        Normal = 5
    }

    class Color {
        <<enumeration>>
        Red = 1
        Green = 2
        Blue = 3
        Grey = 4
        White = 5
    }

    class PokedexApplication["PokédexApplication"] {
        +main()
    }

    Pokedex "1" o-- "0..*" Pokemon : manages
    Pokemon --> Type : has type
    Pokemon --> Color : has color
    PokedexApplication ..> Pokedex : uses
    PokedexApplication ..> Pokemon : creates
    PokedexApplication ..> Type : reads input
    PokedexApplication ..> Color : reads input
```

The diagram uses ASCII identifiers internally while displaying the project’s
original accented class names. The `Pokédex` collection manages zero or more
Pokémon, while each Pokémon has one `Type` and one `Color`.

