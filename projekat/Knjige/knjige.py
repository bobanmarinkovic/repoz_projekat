from repoz_projekat.projekat.Knjige.knjigeIO import ucitaj_knjige

def prikaz_svih_knjiga():
    print('1.) Sortirajte po naslovu knjige')
    print('2.) Sortirajte po kategoriji')
    print('3.) Sortirajte po autoru')
    print('4.) Sortirajte po izdavacu')
    print('5.) Sortirajte po ceni')
    print('6.) Izlaz')

    m = int(input('Izaberte opciju:'))
    if m == 1:
        po_naslovu_knjige()
    elif m == 2:
        po_kategoriji()
    elif m == 3:
        po_autoru()
    elif m == 4:
        po_izdavacu()
    elif m == 5:
        po_ceni()
    elif m == 6:
        return


def po_naslovu_knjige():
    x = ucitaj_knjige()
    z = 0
    for i in range(len(x)):
        for j in x:
            if x[i]["Naslov"] < x[j]["Naslov"]:
                z = x[i]["Naslov"]
                x[i]["Naslov"] = x[j]["Naslov"]
                x[j]["Naslov"] = z
def po_kategoriji():
    x = ucitaj_knjige()
    z = 0
    for i in range(len(x)):
        for j in x:
            if x[i]["Kategorija"] < x[j]["Kategorija"]:
                z = x[i]["Kategorija"]
                x[i]["Kategorija"] = x[j]["Kategorija"]
                x[j]["Kategorija"] = z

def po_autoru():
    x = ucitaj_knjige()
    z = 0
    for i in range(len(x)):
        for j in x:
            if x[i]["Autor"] < x[j]["Autor"]:
                z = x[i]["Autor"]
                x[i]["Autor"] = x[j]["Autor"]
                x[j]["Autor"] = z
def po_izdavacu():
    x = ucitaj_knjige()
    z = 0
    for i in range(len(x)):
        for j in x:
            if x[i]["Izdavac"] < x[j]["Izdavac"]:
                z = x[i]["Izdavac"]
                x[i]["Izdavac"] = x[j]["Izdavac"]
                x[j]["Izdavac"] = z
def po_ceni():
    x=ucitaj_knjige()
    z=0
    for i in range(len(x)):
        for j in x:
            if x[i]["Cena"] < x[j]["Cena"]:
                z=x[i]["Cena"]
                x[i]["Cena"]=x[j]["Cena"]
                x[j]["Cena"]=z



def pks(k ,v):
    knj=ucitaj_knjige()
    fk=[]

    for knjiga in knj:
        if v.lower() in knjiga[k].lower():
            fk.append(knjiga)

