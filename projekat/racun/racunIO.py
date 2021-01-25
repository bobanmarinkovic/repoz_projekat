import json
datoteka= './datoteke/racun.json'

def sacuvaj_racun(racun):

    with open(datoteka, "w") as f:
        json.dump(racun, f)

def ucitaj_racun():
    with open(datoteka, "r") as f:
            return json.load(f)