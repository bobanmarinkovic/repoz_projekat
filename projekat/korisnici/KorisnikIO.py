import json
datoteka= './datoteke/Korisnik.json'

def sacuvaj_knjige(korisnik):

    with open(datoteka, "w") as f:
        json.dump(korisnik,f)

def ucitaj_knjige():
    with open(datoteka, "r") as f:
            return json.load(f)

ucitaj_knjige()