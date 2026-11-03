from Pokedex.Models.Pokémon import Pokémon
from Pokedex.Models.Color import Color
from Pokedex.Models.Type import Type
from Pokedex.Services.Pokédex import Pokédex

from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "pokemon.txt"


class FileManagement:
    @staticmethod
    def save_to_file(pokemon_list):

        if not pokemon_list:
            print("Nothing to save. The list is empty")
            return False
        try:
            DATA_FILE.parent.mkdir(exist_ok=True)

            with DATA_FILE.open("w", encoding="utf-8") as file:
      
                    file.write("=== Pokémon Register ===\n\n")
                   # pokemon = Pokémon
                    for pokemon in pokemon_list:
                        file.write(f"Name  : {pokemon.get_name()}\n")
                        file.write(f"Color : {pokemon.get_color().name}\n")
                        file.write(f"PokédexNr : {pokemon.get_pokedexNr()}\n")
                        file.write(f"Type  : {pokemon.get_type().name}\n")
                        file.write(f"Height: {pokemon.get_height()} cm\n")
                        file.write(f"Weight: {pokemon.get_weight()} kg\n")
                        file.write("-" * 30 + "\n")

                    return True
        except(TypeError, AttributeError, ValueError):
            print("The file could not be saved")
            return False

    @staticmethod
    def read_from_file():
        try:
            pokemon_list = []
    
            with DATA_FILE.open("r", encoding="utf-8") as file:
    
                lines = file.readlines()
    
            i = 0
    
            while i < len(lines):
    
                if lines[i].startswith("Name"):
                    name = lines[i].split(":")[1].strip()

                    color_name = (
                        lines[i + 1]
                        .split(":")[1]
                        .strip()
                    )
    
                    color = Color[color_name]

                    pokedexNr = int(
                            lines[i + 2]
                            .split(":")[1]
                            .strip())

                    type_name = (
                        lines[i + 3]
                        .split(":")[1]
                        .strip()
                    )

                    pokemon_type = Type[type_name]

                    height = float(
                            lines[i + 4]
                            .split(":")[1]
                            .replace("cm", "")
                            .strip()
                          
                    )

                    weight = float(
                            lines[i + 5]
                            .split(":")[1]
                            .replace("kg", "")
                            .strip()
                          
                    )

                    pokemon = Pokémon(
                        name,
                        pokemon_type,
                        color,
                        height,
                        weight,
                        pokedexNr
                    )
    
                    pokemon_list.append(pokemon)
    
                i += 1
    
            return pokemon_list
        
        except FileNotFoundError:
             print("File not found")
             return []

        except (ValueError, KeyError, TypeError):
             print("The file contains invalid data")
             return []
