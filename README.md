# Pokédex
Disposition Pokédex

Indledning
Projektet handler om, at man kan oprette sin egen Pokémon (i en simpel version), og den gemmes i en Pokédex. Brugeren kan derefter se sin Pokémon i Pokédexet, redigere eller slette den.

Funktionalitet

Input

Systemet tager input fra brugeren for at oprette, læse, redigere og slette en Pokémon og viser resultatet i konsollen. Brugeren indtaster navn, type, pokedexnummer, højde, farve og vægt.

Brugerforløb
Pokédex starter op, og brugeren vælger først, om der skal oprettes en Pokémon. Derefter indtaster brugeren de forskellige attributter. Brugeren kommer tilbage til menuen og kan vælge, om Pokémon skal vises, ændres, slettes, sorteres eller gemmes i en fil.

Vis forløbet

Se diagram og screenshots for eksempler på brugerforløbene.

Vigtigste funktioner
- Menuen giver adgang til de forskellige CRUD-operationer.
- Oprettelse af Pokémon er vigtig, fordi de andre CRUD-operationer arbejder med de Pokémon, der er oprettet.
- Læsning viser og verificerer, at vi har en eller flere Pokémon.
- Sortering og filhåndtering er ekstra funktioner.

Hoveddelen

Pokédex-projektet er et modul med en Model-mappe, der indeholder Pokémon-properties og to enum-klasser, Color og Type.
Der er også en Services-mappe med Pokédex-klassen og FileManagement, hvor CRUD-logik, sortering og filhåndtering ligger. Applikationsmodulet `PokédexApplication.py` håndterer UI-menuen.

De vigtigste klasser ligger i Pokédex. Her ligger funktionerne til at oprette en Pokémon, læse listen, opdatere, slette og sortere. `PokédexApplication.py` har kun `main()`, fordi den primært skal kalde funktionerne og vise menuen.

Jeg har delt det op på denne måde for at adskille rollerne. En Pokémon er ikke det samme som en Pokédex, som håndterer Pokémon. FileManagement har ansvaret for at gemme og læse data fra filen.

Klasserne samarbejder ved, at `main()` kalder metoder i Pokédex, og Pokédex opretter og håndterer Pokémon-objekter. Pokédex har derfor en "har-en"-relation til Pokémon:

```python
self.__pokemon_list = []
```

Det er også et eksempel på composition, fordi Pokédex har en liste med Pokémon-objekter.

Den vigtigste klasse er Pokédex. Den har attributten `__pokemon_list` og metoderne `create_Pokémon()`, `show_all_pokemon()`, `update_pokemon()`, `delete_pokemon()` og `sort_pokemon()`.

Jeg har brugt encapsulation, CRUD, datatyper, klasser og objekter. Constructor bruger encapsulation sammen med mine getter- og setter-metoder. Et eksempel på encapsulation er `self.__pokemon_list`, hvor `__` gør attributten privat/name-mangled, så den tilgås gennem metoder.

Jeg kunne godt forbedre projektet ved at bruge en database i stedet for filer, eller ved at give hver CRUD-operation sin egen klasse. Det er dog mere avanceret end det, der er nødvendigt i dette projekt.

Se også [klassediagrammet](PokemonDiagram.mmd).

Konklusion
Strukturen følger i høj grad marsvin-applikationen, men med nogle ændringer - For eksempel har PokédexApplication væsentligt mindre kode, fordi den kun binder menuen sammen med funktionerne. Update har også match-case på alle de attributter, der kan opdateres, i stedet for kun at opdatere navnet.

Projektet kan senere udvides med en ekstra enum-klasse, for eksempel Secondary Type eller abilities, men det ligger uden for projektets scope.
