
from repoz_projekat.projekat.racun.racunIO import ucitaj_racun, sacuvaj_racun
from repoz_projekat.projekat.Knjige.knjigeIO import ucitaj_knjige
from datetime import date
from repoz_projekat.projekat.kcije.AkcijeIO import ucitaj_akcije

def prodaja_knjiga():
    knjige=ucitaj_knjige()
    akcije=ucitaj_akcije()
    korpa=[]
    ukcena=0
    cena=0
    knj=[]
    prodato=[]
    proizvod=0
    print("Zelim da pogledam"
          "\n1.Akcije"
          "\n2.Redovnu ponudu")
    opcija=int(input("Unesote zeljenu opciju: "))
    if opcija==2:
        while True:
            print("U ponudi trenutno imamo:")
            for i in knjige:
                if i["Obrisano"]!="Obrisano":
                    print(i["Sifra"] ,i["Naslov"], i["Cena"])
            x=int(input("Unesite sifru knjige koju zelite da kupite: "))
            for o in knjige:
                if o["Sifra"]==x:
                    kolicina=int(input("Unesite koju kolicinu zelite da kupite: "))
                    ukcena= ukcena+kolicina*o["Cena"]
                    prodataknjiga={
                        "Sifra": o["Sifra"],
                        "Naslov": o["Naslov"],
                        "Autor": o["Autor"],
                        "Izdavac": o["Izdavac"],
                        "Kolicina": kolicina,
                        "Jedinicna_cena": o["Cena"]
                    }
                    korpa.append(o)
                    prodato.append(prodataknjiga)
            m=int(input("Da li zelite da pogledate trenutno stanje korpe i zavrsite kupovinu?"
                                "\n1. DA"
                                "\n2. NE"))
            if m==1:
                print("U korpi trentno imate:\n")
                print("Naslov     Autor     Izdavac     Katregorija     Kolicina\n")
                for l in korpa:
                    print(l["Naslov"], l["Autor"], l["Izdavac"], l["Kategorija"] , kolicina)
                print("Ukupna cena je: ",ukcena)
                print("\nDa li zelite da potvrdite kupovinu: "
                      "\n1. Zelim da potvrdim kupovinu."
                      "\n2. Zelim da odustanem od kupovine."
                      "\n3. Zelim da nastavim sa kupovinom.")
                h=int(input("Unesite zeljenu opciju: "))
                if h == 1:
                    s=1
                    racun=ucitaj_racun()
                    datum=str(date.today())
                    for q in racun:

                            s=q["Sifra"]+1

                    prod=input("Unesite korisnicko ime: ")

                    noviracun = {
                        "Sifra": s,
                        "Prodavac": prod,
                        "Knjige": prodato,
                        "Datum": datum,
                        "Ukupnacena": ukcena,
                        "Akcija": 0

                    }

                    racun.append(noviracun)
                    sacuvaj_racun(racun)
                    print("Hvala Vam, uspesno ste izvrsili kupovinu!")
                    break
                elif h==2:
                    break
                    return None
                else:
                    continue

            elif m==2:
                continue
            else:
                print("Izabrali ste ne posrojecu opciju!\n")

    elif opcija==1:
        while True:
            print("U ponudi trenutno imamo:")
            for j in akcije:
                if j["Datum"] > str(date.today()):
                    cena=0
                    print("\tPod sifrom akcije ",j["Sifra"], " imamo u ponudi knjige:")
                    print("Naslov     Autor    Kategorija     Izdavac")
                    for i in j["Knjige_i_njihove_nove_cene"]:

                        print(i["Naslov"], i["Autor"], i["Kategorija"], i["Izdavac"])
                        cena=cena+i["Cena"]
                    print("\tCena ove akcije iznosi: ", cena,"\n")


            x = int(input("Unesite akcije knjige koju zelite da kupite: "))
            for o in akcije:

                if o["Sifra"] == x:
                    kolicina = int(input("Unesite koju kolicinu zelite da kupite: "))

                    for v in o["Knjige_i_njihove_nove_cene"]:
                        cena1=0
                        cena1=cena1+v["Cena"]
                        ukcena=ukcena+kolicina*cena1
                        prodataknjiga = {
                            "Sifra_akcije":x,
                            "Sifra": v["Sifra"],
                            "Naslov": v["Naslov"],
                            "Autor": v["Autor"],
                            "Izdavac": v["Izdavac"],
                            "Kolicina": kolicina,
                            "Jedinicna_cena": cena1
                        }


                        korpa.append(o)
                        prodato.append(prodataknjiga)
            m = int(input("Da li zelite da pogledate trenutno stanje korpe i zavrsite kupovinu?"
                          "\n1. DA"
                          "\n2. NE"))
            if m == 1:
                print("U korpi trentno imate:\n")
                print("Naslov     Autor     Izdavac     Katregorija     Kolicina\n")
                for l in korpa:
                    for u in l["Knjige_i_njihove_nove_cene"]:
                        print(u["Naslov"], u["Autor"], u["Izdavac"], u["Kategorija"], kolicina)
                print("Ukupna cena je: ", ukcena)
                print("\nDa li zelite da potvrdite kupovinu: "
                      "\n1. Zelim da potvrdim kupovinu."
                      "\n2. Zelim da odustanem od kupovine."
                      "\n3. Zelim da nastavim sa kupovinom.")
                h = int(input("Unesite zeljenu opciju: "))
                if h == 1:
                    racun = ucitaj_racun()
                    datum = str(date.today())
                    for q in racun:
                        s=q["Sifra"]+1
                    prod = input("Unesite korisnicko ime: ")

                    noviracun = {
                            "Sifra": s,
                            "Prodavac": prod,
                            "Knjige": prodato,
                            "Datum": datum,
                            "Ukupnacena": ukcena,
                            "Akcija": 1

                        }

                    racun.append(noviracun)
                    sacuvaj_racun(racun)

                    print("Hvala Vam, uspesno ste izvrsili kupovinu!")
                    break
                elif h == 2:
                    break
                    return None
                else:
                    continue

            elif m == 2:
                continue
            else:
                print("Izabrali ste ne posrojecu opciju!\n")


def kreiranje_izvestaja():
    while True:
        knjige=ucitaj_knjige()
        racun=ucitaj_racun()
        akcije=ucitaj_akcije()
        print("Izaberite tip izvstaja:"
              "\n1. Ukupna prodaja svih kniga"
              "\n2. Ukupna prodaja svih akcija"
              "\n3. Ukupna prodaja knjiga odobranog autora"
              "\n4. Ukupna prodaja svih knjiga odabranog izdavaca"
              "\n5. Ukupna prodaja svih knjiga odabranog kategorije"
              "\n6. Izlaz")

        x=int(input("Izaberite zeljenu opciju: "))
        if x== 1:
            print("\nSifra      Naslov                  Autor                   Izdavac                 Kategorija         Kolicina          Zarada")
            print("_____________________________________________________________________________________________________________________________")
            for j in knjige:
                prodatakolicina=0
                zarada=float(0)
                for i in racun:
                    for l in i["Knjige"]:
                        if l["Sifra"]==j["Sifra"]:
                            prodatakolicina=l["Kolicina"]+prodatakolicina


                            zarada=l["Jedinicna_cena"]*l["Kolicina"]+zarada
                q=" "*(8-len(str(j["Sifra"])))
                w=" "*(20-len(j["Naslov"]))
                e=" "*(20-len(j["Autor"]))
                r=" "*(20-len(j["Izdavac"]))
                t=" "*(15-len(j["Kategorija"]))
                y=" "*(15-len(str(prodatakolicina)))
                print(j["Sifra"],q,"|",j["Naslov"],w,"|", j["Autor"],e,"|", j["Izdavac"],r,"|", j["Kategorija"],t,"|", prodatakolicina,y,"|", zarada)
        elif x==2:
            while True:

                d = 1
                print(
                    "\nSifra      Naslov                  Autor                   Izdavac                 Kategorija         Kolicina          Zarada")
                print(
                    "_____________________________________________________________________________________________________________________________")
                for j in knjige:

                            prodatakolicina = 0
                            zarada = float(0)
                            for i in racun:
                                if i["Akcija"]==1:
                                    for l in i["Knjige"]:
                                        if l["Sifra"] == j["Sifra"]:
                                            prodatakolicina = l["Kolicina"] + prodatakolicina

                                            zarada = l["Jedinicna_cena"] * l["Kolicina"] + zarada

                            q = " " * (8 - len(str(j["Sifra"])))
                            w = " " * (20 - len(j["Naslov"]))
                            e = " " * (20 - len(j["Autor"]))
                            r = " " * (20 - len(j["Izdavac"]))
                            t = " " * (15 - len(j["Kategorija"]))
                            y = " " * (15 - len(str(prodatakolicina)))
                            print(j["Sifra"], q, "|", j["Naslov"], w, "|", j["Autor"], e, "|", j["Izdavac"], r, "|",
                                  j["Kategorija"], t, "|", prodatakolicina, y, "|", zarada)
                            d = 0




        elif x==3:
            while True:
                autor=input("Unesite autora knjige: ")
                d=1
                print(
                    "\nSifra      Naslov                  Autor                   Izdavac                 Kategorija         Kolicina          Zarada")
                print(
                    "_____________________________________________________________________________________________________________________________")
                for j in knjige:
                    if j["Autor"].lower()==autor.lower():
                        prodatakolicina = 0
                        zarada = float(0)
                        for i in racun:
                            for l in i["Knjige"]:
                                if l["Sifra"] ==j["Sifra"]:
                                    prodatakolicina = l["Kolicina"] + prodatakolicina

                                    zarada = l["Jedinicna_cena"] * l["Kolicina"] + zarada

                        q = " " * (8 - len(str(j["Sifra"])))
                        w = " " * (20 - len(j["Naslov"]))
                        e = " " * (20 - len(j["Autor"]))
                        r = " " * (20 - len(j["Izdavac"]))
                        t = " " * (15 - len(j["Kategorija"]))
                        y = " " * (15 - len(str(prodatakolicina)))
                        print(j["Sifra"], q, "|", j["Naslov"], w, "|", j["Autor"], e, "|", j["Izdavac"], r, "|",
                              j["Kategorija"], t, "|", prodatakolicina, y, "|", zarada)
                        d=0

                if d==1:
                    print("Nemamo knjige tog autora na stanju!")
                print("Da li zelite da nastavite?"
                      "\n 1. DA"
                      "\n 2. NE")
                opcija=int(input("Unesite zeljenu opciju: "))
                if opcija==1:
                    continue
                elif opcija==2:
                    return None
                else:
                    print("Izabrali ste nepostojecu opciju, pokusajte ponovo.")


        elif x==4:
            while True:
                autor=input("Unesite izdavaca knjige: ")
                d=1
                print(
                    "\nSifra      Naslov                  Autor                   Izdavac                 Kategorija         Kolicina          Zarada")
                print(
                    "_____________________________________________________________________________________________________________________________")
                for j in knjige:
                    if j["Izdavac"].lower()==autor.lower():
                        prodatakolicina = 0
                        zarada = float(0)
                        for i in racun:
                            for l in i["Knjige"]:
                                if l["Sifra"] ==j["Sifra"]:
                                    prodatakolicina = l["Kolicina"] + prodatakolicina

                                    zarada = l["Jedinicna_cena"] * l["Kolicina"] + zarada

                        q = " " * (8 - len(str(j["Sifra"])))
                        w = " " * (20 - len(j["Naslov"]))
                        e = " " * (20 - len(j["Autor"]))
                        r = " " * (20 - len(j["Izdavac"]))
                        t = " " * (15 - len(j["Kategorija"]))
                        y = " " * (15 - len(str(prodatakolicina)))
                        print(j["Sifra"], q, "|", j["Naslov"], w, "|", j["Autor"], e, "|", j["Izdavac"], r, "|",
                              j["Kategorija"], t, "|", prodatakolicina, y, "|", zarada)
                        d=0

                if d==1:
                    print("Nemamo knjige tog izdavaca na stanju!")
                print("Da li zelite da nastavite?"
                      "\n 1. DA"
                      "\n 2. NE")
                opcija=int(input("Unesite zeljenu opciju: "))
                if opcija==1:
                    continue
                elif opcija==2:
                    return None
                else:
                    print("Izabrali ste nepostojecu opciju, pokusajte ponovo.")
        elif x==5:
            while True:
                autor=input("Unesite kategoriju knjige: ")
                d=1
                print(
                    "\nSifra      Naslov                  Autor                   Izdavac                 Kategorija         Kolicina          Zarada")
                print(
                    "_____________________________________________________________________________________________________________________________")
                for j in knjige:
                    if j["Kategorija"].lower()==autor.lower():
                        prodatakolicina = 0
                        zarada = float(0)
                        for i in racun:
                            for l in i["Knjige"]:
                                if l["Sifra"] ==j["Sifra"]:
                                    prodatakolicina = l["Kolicina"] + prodatakolicina

                                    zarada = l["Jedinicna_cena"] * l["Kolicina"] + zarada

                        q = " " * (8 - len(str(j["Sifra"])))
                        w = " " * (20 - len(j["Naslov"]))
                        e = " " * (20 - len(j["Autor"]))
                        r = " " * (20 - len(j["Izdavac"]))
                        t = " " * (15 - len(j["Kategorija"]))
                        y = " " * (15 - len(str(prodatakolicina)))
                        print(j["Sifra"], q, "|", j["Naslov"], w, "|", j["Autor"], e, "|", j["Izdavac"], r, "|",
                              j["Kategorija"], t, "|", prodatakolicina, y, "|", zarada)
                        d=0

                if d==1:
                    print("Nemamo knjige te kategorije na stanju!")
                print("Da li zelite da nastavite?"
                      "\n 1. DA"
                      "\n 2. NE")
                opcija=int(input("Unesite zeljenu opciju: "))
                if opcija==1:
                    continue
                elif opcija==2:
                    return None
                else:
                    print("Izabrali ste nepostojecu opciju, pokusajte ponovo.")

        elif x==6:
            return None
        else:
            print("Izabrali ste ne postojecu opciju!")

