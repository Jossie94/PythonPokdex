# Pokédex
Disposition Pokédex

Indledning
Projektet handler om man kan oprette sin egen Pokémon (i simpel version) og det gemmes i en Pokédex. Brugeren kan derefter se sin Pokémon i Pokédexet og redigere eller slette. 

Funktionalitet

Input

Systemtet tager input fra brugeren oprette, læse, redigere og slette en Pokémon og viser resultatet ind i konsolen
Brugerforløb
Pokédex starter op og brugeren vælger så først de opretter en Pokémon (med mindre gemt i fil) fordi der er ikke database der gemmer den information og så taster brugeren ind de forskellige attributter (navn, type, dexnummer, højde, farve, og vægt). Så kommer de tilbage til menu og kan vælge så om de vil se deres Pokémon i liste, ændre, slette eller gem i fil

Vis forløbet

Se Diagram og screenshhots

Vigtigst funktioner
-	Menu, for komme til de forskellige CRUD operationer
-	Oprette Pokémon, for havde en Pokémon vi kan udføre forskellige CRUD  
-	Og Læse for se/verificere vi har en eller flere 

Hoveddelen

Pokédex project er en modul, med en Model folder der indeholder Pokémon properties og to enum classes, Color og Type. 
Så har vi Services folder med Pokédex class og Filemanagement, hvor vi har vores CRUD logik, sortering og fil håndtering
Så applikationen der håndtere selve UI menu og en test folder med py test class.

De vigtigst classes ligger i Pokédex, hele CRUD ligger der i – Oprette en Pokémon, læse listen, opdatere, slette.
Jeg har delt op på den her måde for adskille deres roller og funktioner, f.eks en Pokémon er ikke det samme som en Pokédex hvor man håndtere den Pokémon. Jeg kan også lige adskille hvad er model classes og hvilke er service classes, og applikation class er tynd fordi jeg foretrækker den kun kalder på functions fordi jeg bruger som main – jo tyndere main er, bedre arktitektur og læselig kode. 

Det er composite relation mellem Pokémon og Pokédex class – Pokémon har properties objekterog Pokédex bruger de til oprette Pokémon object eller andre CRUD operationer. 
Pokémon class har nærmest alle mine attributer som projketet skal bruge, bortset fra mine enum classes og Pokédex har mine vigtigst functions, som den gøre brug af fra Pokémon class. 

Jeg har brugt encaupsolution, CRUD, datatyper, classes, objekter.  Constructor bruger encaupslotation og mine getter setter metoder. 

Den kan nok udvides til man bruger database til at gemme Pokémon i stedet for filer, eller hver CRUD operation havde sin egen class. 

Konklusion
Rigtigt meget af strukturen følger marsvin applikationen, med nogle ændringer som f.eks PokédexApplication har væsentligt mindre kode, og det er bevidst lave, samt at update har match case på alle sine attributer i stedet for kun update på navn. De forbedringer jeg vil lave er udenfor pensumet, fordi det er mere avanceret, spørg Josefine, forfatteren. 
