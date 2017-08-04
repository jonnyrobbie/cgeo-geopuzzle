www.geotrophy.net

# GeoPuzzle

## CZ

Tento skript slouží ke generování GeoPuzzle trofejí z waypoyntů exportovaných aplikací C:GEO. Stačí, když máte někde soubory .gpx, a ovládání je pak již velice jednoduché.

Číslo puzzle je to číslíčko v adresovém řádku na stránkách GeoTrophy, např. české rozhledny na ardese "http://www.geotrophy.net/GeoPuzzle/?puzzle=9" mají číslo 9.

Pozadí je jedno z pěti možných: černobílé kostky, šedivý, modrý, zelený, vlajka. Pozadi je nepovine, v případě jeho absence jsou zvoleny černobílé kostky.

Použití je pak jednoduché: `./geopuzzle-gen.py -p cislo_puzzle -b pozadi exportovane_kesky.gpx` nebo třeba `./geopuzzle-gen.py -p cislo_puzzle slozka_s_exportovanymi_keskami/*.gpx`.

pro vice informaci spuste `./geopuzzle-gen.py -h`.

Je tady pak jeste `make all`, které vygeneruje kód pro všechny typy GeoPuzzlí a ulozi je do souboru `all_puzzles`.

## EN

This script is used to generate GeoPuzzle trophys from gpx files exported using C:GEO app. All you need is your .gpx files.

Puzzle number is the number in the address line at GeoTrophy, ie. Czech watchtowers from "http://www.geotrophy.net/GeoPuzzle/?puzzle=9" have number 9.

Background is one of five possible: black-white puzzles, gray, blue, green, flag. Selecting background is optional, the default one is black-white puzzles.

Usage is simple: `./geopuzzle-gen.py -p no_puzzle -b backgroundi exported_caches.gpx` or for example `./geopuzzle-gen.py -p no_puzzle folder_with_exported_caches/*.gpx`.

For more info, run `./geopuzzle-gen.py -h`.

Then there's `make all` which generates code for all of the GeoPuzzles and saves it to `all_puzzles`.
