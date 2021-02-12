from repoz_projekat.projekat.Knjige.knjigeIO import ucitaj_knjige, sacuvaj_knjige
from repoz_projekat.projekat.kcije.AkcijeIO import sacuvaj_akcije,ucitaj_akcije
def prikaz_svih_knjigaA():
    while True:
        print('\n1.) Sortirajte po naslovu knjige')
        print('2.) Sortirajte po kategoriji')
        print('3.) Sortirajte po autoru')
        print('4.) Sortirajte po izdavacu')
        print('5.) Sortirajte po ceni')
        print('6.) Izlaz')

        m = int(input('\tIzaberte opciju:'))
        b=0
        if m == 1:
            knjige = po_naslovu_knjige()
            b=1
        elif m == 2:
            knjige = po_kategoriji()
            b=1

        elif m == 3:
            knjige = po_autoru()
            b=1
        elif m == 4:
            knjige = po_izdavacu()
            b=1
        elif m == 5:
            knjige = po_ceni()
            b=1
        elif m == 6:
            return None
        else:
            print("Izabrali ste nepostojecu opciju, pokusajte ponovo!")
        if b==1:
            print(
                "Sifra      Naslov                Autor                   Izdavac                 Cena          Kategorija     Log.Brisanje ")
            print("_________________________________________________________________________________________________________________________")
            for knjiga in knjige:
                sif = str(knjiga["Sifra"])
                k = " " * (7 - len(sif))
                p = " " * int((20 - len(knjiga["Naslov"])))
                l = " " * (20 - len(knjiga["Autor"]))
                g = " " * (20 - len(knjiga["Izdavac"]))
                c = " " * (10 - len(str(knjiga["Cena"])))
                s= " "*(10-len(knjiga["Kategorija"]))
                print(knjiga["Sifra"], k,"|", knjiga["Naslov"], p,"|", knjiga["Autor"], l,"|", knjiga["Izdavac"], g,"|", knjiga["Cena"], c,"|",
                      knjiga["Kategorija"],s,"|",knjiga["Obrisano"])
def prikaz_svih_knjiga():
    while True:
        print('\n1.) Sortirajte po naslovu knjige')
        print('2.) Sortirajte po kategoriji')
        print('3.) Sortirajte po autoru')
        print('4.) Sortirajte po izdavacu')
        print('5.) Sortirajte po ceni')
        print('6.) Izlaz')

        m = int(input('\tIzaberte opciju:'))
        b=0
        if m == 1:
            knjige = po_naslovu_knjige()
            b=1
        elif m == 2:
            knjige = po_kategoriji()
            b=1

        elif m == 3:
            knjige = po_autoru()
            b=1
        elif m == 4:
            knjige = po_izdavacu()
            b=1
        elif m == 5:
            knjige = po_ceni()
            b=1
        elif m == 6:
            return None
        else:
            print("Izabrali ste nepostojecu opciju, pokusajte ponovo!")
        if b==1:
            print(
                "Sifra      Naslov                Autor                   Izdavac                 Cena          Kategorija")
            print("________________________________________________________________________________________________________")
            for knjiga in knjige:
                sif = str(knjiga["Sifra"])
                k = " " * (7 - len(sif))
                p = " " * int((20 - len(knjiga["Naslov"])))
                l = " " * (20 - len(knjiga["Autor"]))
                g = " " * (20 - len(knjiga["Izdavac"]))
                c = " " * (10 - len(str(knjiga["Cena"])))
                print(knjiga["Sifra"], k,"|", knjiga["Naslov"], p,"|", knjiga["Autor"], l,"|", knjiga["Izdavac"], g,"|", knjiga["Cena"], c,"|",
                      knjiga["Kategorija"])

def po_naslovu_knjige():
    x = ucitaj_knjige()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Naslov"] < x[j]["Naslov"]:
                z = x[i]
                x[i] = x[j]
                x[j] = z

    return x

def po_kategoriji():
    x = ucitaj_knjige()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Kategorija"] < x[j]["Kategorija"]:
                z = x[i]
                x[i] = x[j]
                x[j] = z
    return x

def po_autoru():
    x = ucitaj_knjige()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Autor"] < x[j]["Autor"]:
                z = x[i]
                x[i] = x[j]
                x[j] = z
    return x
def po_izdavacu():
    x = ucitaj_knjige()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Izdavac"] < x[j]["Izdavac"]:
                z = x[i]
                x[i] = x[j]
                x[j] = z
    return x
def po_ceni():
    x=ucitaj_knjige()
    z=0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Cena"] < x[j]["Cena"]:
                z=x[i]
                x[i]=x[j]
                x[j]=z

    return x



def pks(kljuc ,vrednost):
    knjige=ucitaj_knjige()
    fk=[]

    for knjiga in knjige:
        if vrednost.lower() == knjiga[kljuc].lower():
            fk.append(knjiga)

    return fk


def pretrazi_knjige():
    while True:
        print("\n1.) Pretraga knjige po sifri")
        print("2.) Pretraga knjige po naslovu")
        print("3.) Pretraga knjige po autoru")
        print("4.) Pretraga knjige po kategoriji")
        print("5.) Pretraga knjige po izdavacu")
        print("6.) Pretraga knjige po opsegu cene")
        print("7.) Izlaz")

        m= int(input("\nUnesite zeljenu opciju: "))
        b=0
        if m==1:
            x = pretraga_po_sifri()
            b=1

        elif m==2:
            x= pretraga_po_naslovu()
            b=1

        elif m==3:
            x=pretraga_po_autoru()
            b=1
        elif m==4:
            x=pretraga_po_kategoriji()
            b=1



        elif m==5:
            x=pretraga_po_izdavacu()
            b=1
        elif m==6:
            x=pretraga_po_opsegucene()
            b=1
        elif m==7:
            return None
        else:
            print("Izabrali ste nepostojecu opciju, pokusajte ponovo!")
        if b==1:
            print(
                "Sifra      Naslov                Autor                   Izdavac                 Cena          Kategorija")
            print(
                "__________________________________________________________________________________________________________")
            for knjiga in x:
                sif = str(knjiga["Sifra"])
                k = " " * (7 - len(sif))
                p = " " * int((20 - len(knjiga["Naslov"])))
                l = " " * (20 - len(knjiga["Autor"]))
                g = " " * (20 - len(knjiga["Izdavac"]))
                c = " " * (10 - len(str(knjiga["Cena"])))
                print(knjiga["Sifra"], k, "|", knjiga["Naslov"], p, "|", knjiga["Autor"], l, "|", knjiga["Izdavac"], g, "|",
                      knjiga["Cena"], c, "|",
                      knjiga["Kategorija"])


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
    x=pks("Kategorija", m)
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
    while True:
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
            "Kategorija": k,
            "Obrisano": "Nije obrisano"

        }
        knjige.append(novaknjiga)
        sacuvaj_knjige(knjige)
        print("Uspesno ste dodali knjigu!")
        print("\nDa li zelite da nastavite sa dodavanjem knjiga?"
              "\n1. DA"
              "\n2. NE")
        while True:
            opcija=int(input("Unesite zeljenu opciju: "))
            if opcija==2:
                return None

            elif opcija==1:
                break
            else:
                print("Izabrali ste nepostojecu opciju, pokusajte ponovo")






def izmena_knjige():

    while True:
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
                    print("\nUspesno ste izmenili knjigu!")


        if brojac==0:
            print("Uneli ste pogresnu sifru probajte ponovo!")

        sacuvaj_knjige(knjige)

        print("\nDa li zelite da nastavite sa izmenom knjiga?"
              "\n1. DA"
              "\n2. NE")
        while True:
            opcija = int(input("Unesite zeljenu opciju: "))
            if opcija == 2:
                return None

            elif opcija == 1:
                break
            else:
                print("Izabrali ste nepostojecu opciju, pokusajte ponovo")

def logicko_brisanje_knjige():
    while True:
        k=ucitaj_knjige()
        brojac=0
        sifra=int(input("Unesite sifru knjige koju zelite da obriste: "))
        for i in k:

            if i["Sifra"]==sifra:
                i["Obrisano"]="Obrisano"
                print("Obrisali ste knjigu!")
                brojac=1

        if brojac==0:
            print("Knjiga sa unetom sifrom nepostoji, pokusajte ponovo!")

        sacuvaj_knjige(k)
        print("\nDa li zelite da nastavite sa brisanjem knjiga?"
              "\n1. DA"
              "\n2. NE")
        while True:
            opcija = int(input("Unesite zeljenu opciju: "))
            if opcija == 2:
                return None

            elif opcija == 1:
                break
            else:
                print("Izabrali ste nepostojecu opciju, pokusajte ponovo")









