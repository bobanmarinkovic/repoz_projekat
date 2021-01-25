from repoz_projekat.projekat.kcije.AkcijeIO import ucitaj_akcije, sacuvaj_akcije

from datetime import date


def Prikaz_akcija():
    print("1.) Sortiraj akcije po datumu")
    print("2.) Sortiraj akcije po sifri")
    print("3.) Izlaz")
    m= int(input("Unesite zeljenu opciju: "))
    if m==1:
      po_datumu()
    elif m==2:
      po_sifri()
    elif m==3:
        return None
    else:
        print("Uneli ste nepostojecu opciju!")


def po_datumu():
    x = ucitaj_akcije()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Datum"] < x[j]["Datum"]:
                z = x[i]["Datum"]
                x[i]["Datum"] = x[j]["Datum"]
                x[j]["Datum"] = z
    vreme = date.today()
    brojac=0
    for m in x:
        if m["Datum"] > str(vreme):
            brojac=brojac+1
            print(m["Knjige_i_njihove_nove_cene"])

    if brojac==0:
        print("Nemamo trenutno aktivnih akcija")
def po_sifri():
    x = ucitaj_akcije()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Sifra"] < x[j]["Sifra"]:
                z = x[i]["Sifra"]
                x[i]["Sifra"] = x[j]["Sifra"]
                x[j]["Sifra"] = z
    vreme = date.today()
    brojac = 0
    for m in x:
        if m["Datum"] > str(vreme):
            brojac = brojac + 1
            print(m["Knjige_i_njihove_nove_cene"])

    if brojac == 0:
        print("Nemamo trenutno aktivnih akcija")


def pretraga_akcija():
    x=ucitaj_akcije()
    print("1.) Pretraga akcija po sifri")
    print("2.) Pretraga akcija po naslovu")
    print("3.) Pretraga akcija po autoru")
    print("4.) Pretraga akcija po kategoriji")

    m = int(input("\nUnesite zeljenu opciju: "))

    if m == 1:
        l = pretraga_po_sifri()

    elif m == 2:
        l = pretraga_po_naslovu()

        print(l)
    elif m == 3:
        l = pretraga_po_autoru()
        print(l)
    elif m == 4:
        l = pretraga_po_kategoriji()
        print(l)

def pretraga_po_naslovu ():
    m = ucitaj_akcije()
    sifra = input("Unesite naslov knjige: ")
    brojac = 0
    for p in m:
        if p["Datum"] > str(date.today()):
            s = p["Knjige_i_njihove_nove_cene"]
            for k in s:
                if k["Naslov"].lower() == sifra.lower():
                    brojac = brojac + 1
                    print(s)
                    break
    if brojac == 0:
        print("\nTrenutno nemamo akciju za tu knjigu")
def pretraga_po_kategoriji():
    m = ucitaj_akcije()
    sifra = input("Unesite kategorju knjige: ")
    brojac = 0
    for p in m:
        if p["Datum"] > str(date.today()):
            s = p["Knjige_i_njihove_nove_cene"]
            for k in s:
                if k["Kategorija"].lower() == sifra.lower():
                    brojac = brojac + 1
                    print(s)
                    break
    if brojac == 0:
        print("\nTrenutno nemamo akciju za tu knjigu")
def pretraga_po_autoru():
    m = ucitaj_akcije()
    sifra = input("Unesite autora knjige: ")
    brojac = 0
    for p in m:
        if p["Datum"]>str(date.today()):
            s = p["Knjige_i_njihove_nove_cene"]
            for k in s:
                if k["Autor"].lower() == sifra.lower():
                    brojac = brojac + 1
                    print(s)
                    break



    if brojac == 0:
        print("\nTrenutno nemamo akciju za tu knjigu")

def pretraga_po_sifri():
    m = ucitaj_akcije()
    sifra =int(input("Unesite sifru knjige: "))
    brojac = 0
    for p in m:
        if p["Datum"] > str(date.today()):
            s = p["Knjige_i_njihove_nove_cene"]
            for k in s:
                if k["Sifra"]== sifra:
                    brojac = brojac + 1
                    print(s)
                    break
    if brojac == 0:
        print("\nTrenutno nemamo akciju za tu knjigu")

def kreiranje_akcijske_ponude():
    akcije=ucitaj_akcije()
    knjige=[]

    print("\tUnesite podatke o knjizi")
    while True:
        s = int(input("\nUnesite sifru nove knjige: "))
        for z in akcije:
            r=z["Knjige_i_njihove_nove_cene"]
            for q in r:
                if z["Sifra"] == s:
                    print("Knjiga sa tom sifrom je vec uneta")
                    return None
        n = input("Unesite naslov:")
        isbn = int(input("Unesite isbn: "))
        a = input("Unesite autora: ")
        i = input("Unesite izdavaca: ")
        br = int(input("Unesite broj strana: "))
        g = int(input("Unesite godinu izdavanja: "))
        c = float(input("Unesite cenu: "))
        k = input("Unesite kategoriju: ")

        novaknjiga = {
            "Sifra": s,
            "Naslov": n,
            "Isbn": isbn,
            "Autor": a,
            "Izdavac": i,
            "Broj_strana": br,
            "Godina": g,
            "Cena": c,
            "Kategorija": k

        }

        knjige.append(novaknjiga)
        print("Da li zelite da nastavite sa unosom knjiga?"
              "\n 1.) DA"
              "\n 2.) NE")
        h=int(input("Unesite zeljenu opciju"))
        if h==2:
            break




    for b in akcije:
            x=b["Sifra"]
            sifra = x + 1

    datum = input("Unesi datum do kad vazi akcija (po primeru: godina-mesec-dan): ")
    akcijska_ponuda={
            "Sifra": sifra,
            "Knjige_i_njihove_nove_cene":knjige,
            "Datum": datum

        }
    akcije.append(akcijska_ponuda)
    sacuvaj_akcije(akcije)

