class Pokémon:
    def __init__(self, name, type, color, height, weight, pokedexNr):
            self.set_name(name)
            self.set_type(type)
            self.set_color(color)
            self.set_height(height)
            self.set_weight(weight)
            self.set_pokedexNr(pokedexNr)
    
    def get_name(self):
                return self.__name
    
    def get_type(self):
                return self.__type
    
    def get_color(self):
                return self.__color
    
    def get_height(self):
             return self.__height
        
    def get_weight(self):
            return self.__weight

    def get_pokedexNr(self):
            return self.__pokedexNr
    
    def set_name(self, name):
            if name != "":
                self.__name = name
    
    def set_type(self, type):
                self.__type = type
    
    def set_color(self, color):
                self.__color = color
    
    def set_height(self, height):
        if height > 0:
            self.__height = height

    def set_weight(self, weight):
        if weight > 0:
            self.__weight = weight

    def set_pokedexNr(self, pokedexNr):
            if pokedexNr > 0:
                    self.__pokedexNr = pokedexNr
        
    def __str__(self):
            return f"{self.__name} ({self.__color}, {self.__weight} kg, {self.__type} type, {self.__height} m, {self.__pokedexNr})"