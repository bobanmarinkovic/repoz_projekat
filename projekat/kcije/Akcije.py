from repoz_projekat.projekat.kcije.AkcijeIO import ucitaj_akcije, sacuvaj_akcije
from repoz_projekat.projekat.Knjige.knjigeIO import ucitaj_knjige

from datetime import date


def Prikaz_akcija():
    while True:
        print("\n1.) Sortiraj akcije po datumu")
        print("2.) Sortiraj akcije po sifri")
        print("3.) Izlaz")
        m= int(input("\tUnesite zeljenu opciju: "))
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
                z = x[i]
                x[i] = x[j]
                x[j] = z
    vreme = date.today()
    brojac=0
    for m in x:
        b=1
        if m["Datum"] > str(vreme):
            print("\n\tU ponudi imamo knjige sa akcijskom sifrom ", m["Sifra"])
            print("Sifra        Naslov                 Autor                   Izdavac                 Cena          Datum               Kategorija")
            print("__________________________________________________________________________________________________________________________________")
            for l in m["Knjige_i_njihove_nove_cene"]:
                if m["Datum"] > str(vreme):

                    brojac=brojac+1

                    q=" "*(10-(len(str(l["Sifra"]))))
                    w=" "*(20-len(l["Naslov"]))
                    e=" "*(20-len(l["Autor"]))
                    t=" "*(20-len(l["Izdavac"]))
                    y=" "*(10- len(str(l["Cena"])))
                    o = " " * (15 - len(str(m["Datum"])))

                    print(l["Sifra"],q,"|", l["Naslov"],w,"|", l["Autor"],e,"|", l["Izdavac"],t,"|", l["Cena"],y,"|", m["Datum"],o,"|",l["Kategorija"])

    if brojac==0:
        print("Nemamo trenutno aktivnih akcija")

def po_sifri():
    x = ucitaj_akcije()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Sifra"] < x[j]["Sifra"]:
                z = x[i]
                x[i] = x[j]
                x[j] = z
    vreme = date.today()
    brojac = 0
    for m in x:
        if m["Datum"] > str(vreme):
            print("\n\tU ponudi imamo knjige sa akcijskom sifrom ", m["Sifra"])
        print("Sifra        Naslov                 Autor                   Izdavac                 Cena          Datum               Kategorija")
        print(
            "___________________________________________________________________________________________________________________________________")
        for l in m["Knjige_i_njihove_nove_cene"]:
            if m["Datum"] > str(vreme):
                brojac = brojac + 1
                brojac = brojac + 1

                q = " " * (10 - (len(str(l["Sifra"]))))
                w = " " * (20 - len(l["Naslov"]))
                e = " " * (20 - len(l["Autor"]))
                t = " " * (20 - len(l["Izdavac"]))
                y = " " * (10 - len(str(l["Cena"])))
                o = " " * (15 - len(str(m["Datum"])))
                print(l["Sifra"], q, "|", l["Naslov"], w, "|", l["Autor"], e, "|", l["Izdavac"], t, "|", l["Cena"], y,
                      "|", m["Datum"],o,"|",l["Kategorija"])

    if brojac == 0:
        print("Nemamo trenutno aktivnih akcija")


def pretraga_akcija():
    while True:
        x=ucitaj_akcije()
        print("\n1.) Pretraga akcija po sifri")
        print("2.) Pretraga akcija po naslovu")
        print("3.) Pretraga akcija po autoru")
        print("4.) Pretraga akcija po kategoriji")
        print("5.) Izlaz")

        m = int(input("\nUnesite zeljenu opciju: "))

        if m == 1:
            pretraga_po_sifri()



        elif m == 2:
            l = pretraga_po_naslovu()


        elif m == 3:
            l = pretraga_po_autoru()

        elif m == 4:
            l = pretraga_po_kategoriji()
        elif m==5:
            return None
        else:
            print("Izabrali ste ne postojecu opciju, pokusajte ponovo!")

def pretraga_po_naslovu ():
    m = ucitaj_akcije()
    sifra = input("Unesite naslov knjige: ")
    brojac = 0
    print(
        "Sifra        Naslov                 Autor                   Izdavac                 Cena          Datum               Kategorija")
    print(
        "_________________________________________________________________________________________________________________________________")
    for p in m:
        if p["Datum"] > str(date.today()):

            s = p["Knjige_i_njihove_nove_cene"]
            for l in s:
                if l["Naslov"].lower() == sifra.lower():
                    brojac = brojac + 1
                    q = " " * (10 - (len(str(l["Sifra"]))))
                    w = " " * (20 - len(l["Naslov"]))
                    e = " " * (20 - len(l["Autor"]))
                    t = " " * (20 - len(l["Izdavac"]))
                    y = " " * (10 - len(str(l["Cena"])))
                    o = " " * (15 - len(str(p["Datum"])))
                    print(l["Sifra"], q, "|", l["Naslov"], w, "|", l["Autor"], e, "|", l["Izdavac"], t, "|", l["Cena"],
                          y,
                          "|", p["Datum"],o,"|",l["Kateorija"])

    if brojac == 0:
        print("\nTrenutno nemamo akciju za tu knjigu")
def pretraga_po_kategoriji():
    m = ucitaj_akcije()
    sifra = input("Unesite kategorju knjige: ")
    brojac = 0
    print("Sifra        Naslov                 Autor                   Izdavac                 Cena          Datum               Kategorija")
    print(
        "__________________________________________________________________________________________________________________________________")
    for p in m:
        if p["Datum"] > str(date.today()):

            s = p["Knjige_i_njihove_nove_cene"]
            for l in s:
                if l["Kategorija"].lower() == sifra.lower():
                    brojac = brojac + 1
                    q = " " * (10 - (len(str(l["Sifra"]))))
                    w = " " * (20 - len(l["Naslov"]))
                    e = " " * (20 - len(l["Autor"]))
                    t = " " * (20 - len(l["Izdavac"]))
                    y = " " * (10 - len(str(l["Cena"])))
                    o = " " * (15 - len(str(p["Datum"])))
                    print(l["Sifra"], q, "|", l["Naslov"], w, "|", l["Autor"], e, "|", l["Izdavac"], t, "|", l["Cena"],
                          y,
                          "|", p["Datum"],o,"|",l["Kategorija"])
    if brojac == 0:
        print("\nTrenutno nemamo akciju za tu knjigu")
def pretraga_po_autoru():
    m = ucitaj_akcije()
    sifra = input("Unesite autora knjige: ")
    brojac = 0
    print(
        "Sifra        Naslov                 Autor                   Izdavac                 Cena          Datum               Kategorija")
    print(
        "________________________________________________________________________________________________________________________________")
    for p in m:

        if p["Datum"]>str(date.today()):

            s = p["Knjige_i_njihove_nove_cene"]
            for l in s:

                if l["Autor"].lower() == sifra.lower():
                    brojac = brojac + 1
                    q = " " * (10 - (len(str(l["Sifra"]))))
                    w = " " * (20 - len(l["Naslov"]))
                    e = " " * (20 - len(l["Autor"]))
                    t = " " * (20 - len(l["Izdavac"]))
                    y = " " * (10 - len(str(l["Cena"])))
                    o = " " * (15 - len(str(p["Datum"])))
                    print(l["Sifra"], q, "|", l["Naslov"], w, "|", l["Autor"], e, "|", l["Izdavac"], t, "|", l["Cena"],
                          y,
                          "|", p["Datum"],o,"|",l["Kategorija"])




    if brojac == 0:
        print("\nTrenutno nemamo akciju za tu knjigu")

def pretraga_po_sifri():
    m = ucitaj_akcije()
    sifra =int(input("Unesite sifru knjige: "))
    brojac = 0
    print(
        "Sifra        Naslov                 Autor                   Izdavac                 Cena          Datum               Kategorija")
    print(
        "_________________________________________________________________________________________________________________________________")
    for p in m:

        if p["Datum"] > str(date.today()):

            s = p["Knjige_i_njihove_nove_cene"]
            for l in s:

                if l["Sifra"]== sifra:
                    brojac = brojac + 1
                    q = " " * (10 - (len(str(l["Sifra"]))))
                    w = " " * (20 - len(l["Naslov"]))
                    e = " " * (20 - len(l["Autor"]))
                    t = " " * (20 - len(l["Izdavac"]))
                    y = " " * (10 - len(str(l["Cena"])))
                    o= " "*(15-len(str(p["Datum"])))
                    print(l["Sifra"], q, "|", l["Naslov"], w, "|", l["Autor"], e, "|", l["Izdavac"], t, "|", l["Cena"],
                          y,
                          "|", p["Datum"],o,"|",l["Kategorija"])

    if brojac == 0:
        print("\nTrenutno nemamo akciju za tu knjigu")

def kreiranje_akcijske_ponude():
    akcije=ucitaj_akcije()
    knjige=[]
    knj=ucitaj_knjige()


    while True:
        s = int(input("\nUnesite sifru knjige koju zelite da stavite na akciju: "))
        cen=float(input("Unesite snizenu cenu knjige: "))
        for q in knj:

                    if q["Sifra"]==s:


                        n = q["Naslov"]
                        isbn = q["Isbn"]
                        a = q["Autor"]
                        i = q["Izdavac"]
                        br = q["Broj_strana"]
                        g = q["Godina"]
                        c = cen
                        k = q["Kategorija"]



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
    print("Uspesno ste uneli akcijsku ponudu!")


