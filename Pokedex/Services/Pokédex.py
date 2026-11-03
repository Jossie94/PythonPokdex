from Pokedex.Models.Pokémon import Pokémon
from Pokedex.Models.Color import Color
from Pokedex.Models.Type import Type


class Pokédex:
    def __init__(self):
        self.__pokemon_list = []

    # GET 
    def get_pokemon_list(self):
        return self.__pokemon_list

    # CREATE
    def create_Pokémon(self):
        try:
            name = input("Name: ")

            print("Choose type:")
            print("1. Grass")
            print("2. Fire")
            print("3. Water")
            print("4. Flying")
            print("5. Normal")
            type = Type(int(input("Type: ")))

            print("Choose color:")
            print("1. Red")
            print("2. Green")
            print("3. Blue")
            print("4. Grey")
            print("5. White")
            color = Color(int(input("Color: "))) 

            height = float(input("Height: "))
            weight = float(input("Weight: "))
            pokedexNr = int(input("Pokédex number: "))

            pokemon = Pokémon(name, type, color, height, weight, pokedexNr)
            self.__pokemon_list.append(pokemon)
            return pokemon
        
        except ValueError:
            print("Invalid Value input")
            return None

    # READ
    def show_all_pokemon(self):
        for pokemon in self.__pokemon_list:
            print(pokemon)

    # UPDATE
    def update_pokemon(self):
        try:
            pokedex_nr = int(input("Choose a Pokémon by Pokédex number: "))

        except ValueError:
             print("Invalid PokedexNr")
             return

        selected_pokemon = None

        for pokemon in self.__pokemon_list:
            if pokemon.get_pokedexNr() == pokedex_nr:
                selected_pokemon = pokemon
                break

        if selected_pokemon is None:
            print("Pokémon not found.")
            return

        print("\n----- Update Pokémon -----")
        print("1. Update Name")
        print("2. Update Color")
        print("3. Update Type")
        print("4. Update Height")
        print("5. Update Weight")

        try:

            choice = input("Choose what to update: ")

            match choice:
                case "1":
                    selected_pokemon.set_name(input("New name: "))

                case "2":
                    print("Choose color:")
                    print("1. Red")
                    print("2. Green")
                    print("3. Blue")
                    print("4. Grey")
                    print("5. White")
                    selected_pokemon.set_color(Color(int(input("New color: "))))

                case "3":
                    print("Choose type:")
                    print("1. Grass")
                    print("2. Fire")
                    print("3. Water")
                    print("4. Flying")
                    print("5. Normal")
                    selected_pokemon.set_type(Type(int(input("New type: "))))

                case "4":
                    selected_pokemon.set_height(float(input("New height: ")))

                case "5":
                    selected_pokemon.set_weight(float(input("New weight: ")))

                case _:
                    print("Invalid choice.")
                    return

            print("Pokémon updated.")
        except ValueError:
             print("Invalid value input")

    # DELETE
    def delete_pokemon(self):
        pokedex_nr = int(input("Choose a Pokémon by Pokédex number: "))

        for pokemon in self.__pokemon_list:
            if pokemon.get_pokedexNr() == pokedex_nr:
                self.__pokemon_list.remove(pokemon)
                print("Pokémon deleted.")
                return True
            
        else:
            print("Pokémon not found.")
            return False

    # SORT
    def sort_pokemon(self):
        print("\n----- Sort Pokémon -----")
        print("1. Sort Name")
        print("2. Sort Color")
        print("3. Sort Type")
        print("4. Sort Height")
        print("5. Sort Weight")

        choice = input("Choose what to sort: ")
        
        match choice:
                case "1":
                        self.__pokemon_list.sort(
                        key=lambda pokemon: pokemon.get_name()
                                )
                        for pokemon in self.__pokemon_list:
                                print(pokemon)
                case "2":
                        self.__pokemon_list.sort(
                        key=lambda pokemon: pokemon.get_color().value
                                                        )
                        for pokemon in self.__pokemon_list:
                                print(pokemon)
                case "3":
                        self.__pokemon_list.sort(
                        key=lambda pokemon: pokemon.get_type().value
                                                        )
                        for pokemon in self.__pokemon_list:
                                print(pokemon)
                case "4":
                        self.__pokemon_list.sort(
                        key=lambda pokemon: pokemon.get_height()
                                                        )
                        for pokemon in self.__pokemon_list:
                                print(pokemon)
                case "5":
                        self.__pokemon_list.sort(
                        key=lambda pokemon: pokemon.get_weight()
                                                        )
                        for pokemon in self.__pokemon_list:
                                print(pokemon)

   
