from Pokedex.Services.Pokédex import Pokédex
from Pokedex.Services.PokemonFileManagement import FileManagement


def main():
    pokedex = Pokédex()

    while True:
        print("\n----- Pokédex Menu -----")
        print("1. Create Pokémon")
        print("2. Show all Pokémon")
        print("3. Update Pokémon")
        print("4. Delete Pokémon")
        print("5. Sort Pokémon") 
        print("6. Save file")
        print("7. Read from file")
        print("0. End program")

        valg = input("Choose menuoption: ")

        match valg:
            case "1":
                pokemon = pokedex.create_Pokémon()

                if pokemon is not None:
                    print("Created a Pokémon")

            case "2":
                pokedex.show_all_pokemon()

            case "3":
                pokedex.update_pokemon()

            case "4":
                pokedex.delete_pokemon()

            case "5":
                pokedex.sort_pokemon()

            case "6":
                all_pokemon = pokedex.get_pokemon_list()

                if FileManagement.save_to_file(all_pokemon):
                    print("Saved all Pokémons to a file")

            case "7":
                pokemon_list = FileManagement.read_from_file()

                for pokemon in pokemon_list:
                    print(pokemon)

            case "0":
                break

            case _:
                print("Invalid menu option.")


if __name__ == "__main__":
    main()
