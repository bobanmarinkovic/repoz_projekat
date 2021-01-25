from repoz_projekat.projekat.Knjige.knjigeIO import ucitaj_knjige, sacuvaj_knjige
from repoz_projekat.projekat.kcije.AkcijeIO import sacuvaj_akcije,ucitaj_akcije
def prikaz_svih_knjiga():
    print('1.) Sortirajte po naslovu knjige')
    print('2.) Sortirajte po kategoriji')
    print('3.) Sortirajte po autoru')
    print('4.) Sortirajte po izdavacu')
    print('5.) Sortirajte po ceni')
    print('6.) Izlaz')

    m = int(input('Izaberte opciju:'))
    if m == 1:
        knjige = po_naslovu_knjige()
    elif m == 2:
        knjige = po_kategoriji()

    elif m == 3:
        knjige = po_autoru()
    elif m == 4:
        knjige = po_izdavacu()
    elif m == 5:
        knjige = po_ceni()
    elif m == 6:
        return None
    else:
        print("Izabrali ste nepostojecu opciju")

    for knjiga in knjige:
        print(knjiga)

def po_naslovu_knjige():
    x = ucitaj_knjige()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Naslov"] < x[j]["Naslov"]:
                z = x[i]["Naslov"]
                x[i]["Naslov"] = x[j]["Naslov"]
                x[j]["Naslov"] = z
    return x
def po_kategoriji():
    x = ucitaj_knjige()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Kategorija"] < x[j]["Kategorija"]:
                z = x[i]["Kategorija"]
                x[i]["Kategorija"] = x[j]["Kategorija"]
                x[j]["Kategorija"] = z
    return x

def po_autoru():
    x = ucitaj_knjige()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Autor"] < x[j]["Autor"]:
                z = x[i]["Autor"]
                x[i]["Autor"] = x[j]["Autor"]
                x[j]["Autor"] = z
    return x
def po_izdavacu():
    x = ucitaj_knjige()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Izdavac"] < x[j]["Izdavac"]:
                z = x[i]["Izdavac"]
                x[i]["Izdavac"] = x[j]["Izdavac"]
                x[j]["Izdavac"] = z
    return x
def po_ceni():
    x=ucitaj_knjige()
    z=0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Cena"] < x[j]["Cena"]:
                z=x[i]["Cena"]
                x[i]["Cena"]=x[j]["Cena"]
                x[j]["Cena"]=z

    return x



def pks(kljuc ,vrednost):
    knjige=ucitaj_knjige()
    fk=[]

    for knjiga in knjige:
        if vrednost.lower() == knjiga[kljuc].lower():
            fk.append(knjiga)

    return fk


def pretrazi_knjige():
    print("1.) Pretraga knjige po sifri")
    print("2.) Pretraga knjige po naslovu")
    print("3.) Pretraga knjige po autoru")
    print("4.) Pretraga knjige po kategoriji")
    print("5.) Pretraga knjige po izdavacu")
    print("6.) Pretraga knjige po opsegu cene")
    print("7.) Izlaz")

    m= int(input("\nUnesite zeljenu opciju: "))

    if m==1:
        l = pretraga_po_sifri()
        print(l)
    elif m==2:
        l= pretraga_po_naslovu()

        print(l)
    elif m==3:
        l=pretraga_po_autoru()
        print(l)
    elif m==4:
        l=pretraga_po_kategoriji()
        print(l)

    elif m==5:
        l=pretraga_po_izdavacu()
        print(l)
    elif m==6:
        l=pretraga_po_opsegucene()
        print(l)
    elif m==7:
        return None
    else:
        print("Izabrali ste nepostojecu opciju")


def pretraga_po_naslovu ():
    naslov = input("Unesite naslov: ")
    x=pks("Naslov", naslov)
    return x
def pretraga_po_autoru():
    autor=input("Unesite autora: ")
    x=pks("Autor", autor)
    return x
def pretraga_po_kategoriji():
    m=input("Unesite kategoriju: ")
    x=pks("Katregorija", m)
    return x
def pretraga_po_izdavacu():
    autor=input("Unesite izdavaca: ")
    x=pks("Izdavac", autor)
    return x
def pretraga_po_sifri():
    knjige = ucitaj_knjige()
    sifra=int(input("Unesite sifru: "))
    fk = []
    for knjiga in knjige:
        if sifra == knjiga["Sifra"]:
            fk.append(knjiga)
    return fk
def pretraga_po_opsegucene():
    knjige=ucitaj_knjige()
    cmin=int(input("Unesite donju granicu cene: "))
    cmax=int(input("Unesite gornju ganicu cene: "))
    lista=[]
    for knjiga in knjige:
        if cmin <= knjiga["Cena"] and cmax >= knjiga["Cena"]:
            lista.append(knjiga)
    return lista
def dodavanje_knjige():
    knjige=ucitaj_knjige()
    s=int(input("Unesite sifru nove knjige: "))
    for z in knjige:
        if z["Sifra"] == s:
            print("Knjiga sa tom sifrom je vec uneta")
            return None
    n=input("Unesite naslov:")
    isbn=int(input("Unesite isbn: "))
    a=input("Unesite autora: ")
    i=input("Unesite izdavaca: ")
    br=int(input("Unesite broj strana: "))
    g=int(input("Unesite godinu izdavanja: "))
    c=float(input("Unesite cenu: "))
    k=input("Unesite kategoriju: ")

    novaknjiga={
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
    sacuvaj_knjige(knjige)



def izmena_knjige():


    sifra=int(input("Unesite sifru knjige koju zelite da izemnite: "))
    knjige = ucitaj_knjige()
    brojac=0
    akcije=ucitaj_akcije()
    for i in knjige:
        if i["Sifra"] == sifra:
                brojac=brojac+1
                n=input("Unesite novi naslov: ")
                if n == "":
                    i["Naslov"]=i["Naslov"]


                else:
                    i["Naslov"]=n
                isbn = int(input("Unesite novi isbn, ukoliko zelite da isbn ostene ne promenjen pritisnit 0: "))
                if isbn == 0:
                    i["Isbn"] = i["Isbn"]


                else:
                    i["Isbn"] = isbn
                a= input("Unesite novog autora: ")
                if a == "":
                    i["Autor"] = i["Autor"]

                else:
                    i["Autor"] = a
                iz = input("Unesite novog izdavaca: ")
                if iz == "":
                    i["Izdavac"] = i["Izdavac"]

                else:
                    i["Izdavac"] = iz
                b = int(input("Unesite novi broj strana, ukoliko zelite da broj strana ostane nepromenjen pristite 0: "))
                if b == 0:
                    i["Broj_strana"] = i["Broj_strana"]

                else:
                    i["Broj_strana"] = b
                g = int(input("Unesite novu godinu, ukoliko zelite da godina ostene nepromenjena unesite 0: "))
                if g == 0:
                    i["Godina"] = i["Godina"]

                else:
                    i["Godina"] = g
                c = float(input("Unesite novu cenu, ukoliko zelite da cena ostane nepromenjena uneite 0: "))
                if c == 0:
                    i["Cena"] = i["Cena"]

                else:
                    i["Cena"] = c
                k = input("Unesite novu kategoriju: ")
                if k == "":
                    i["Kategorija"] = i["Kategorija"]

                else:
                    i["Kategorija"] = k


    if brojac==0:
        print("Uneli ste pogresnu sifru probajte ponovo!")



    sacuvaj_knjige(knjige)





