from repoz_projekat.projekat.korisnici.KorisnikIO import ucitaj_korisnike, sacuvaj_korisnike
def prijava():
    korisnici= ucitaj_korisnike()

    br = 0
    for br in range(3):
        k_i = input("Unesite korisnicko ime: ")
        l = input("Unesite lozinku: ")

        for i in korisnici:
            if i['Korisnicko_ime'] == k_i and i['Lozinka'] == l:
                return i
        print("Uneli ste pogresnu sifru/korisrnicko ime, pokusajte ponovo")
    return None
def registracija():
    while True:
        s=ucitaj_korisnike()
        ki=input("Unesite zeljeno korisnicko ime: ")
        for z in s:
                if ki == z["Korisnicko_ime"]:
                    print("Korisnicko ime je zauzeto, pokusajte ponovo!")
                    return


        l=input("Unesite zeljenu lozinku: ")
        i=input("Unesite ime: ")
        p=input("Unesite prezime: ")
        m = int(input("Unesite da li je novi korisnik:"
                      "\n1.Menadzer"
                      "\n2.Prodavac "
                      "\n3.Nista od navedenog"
                      "\n"))


        if m==1:
            t="Menadzer"
        elif m==2:
            t="Prodavac"
        elif m==3:


            print("Nije moguce uneti korisnika!")
            return None

        else:
            print("Izabrali ste ne postojecu opciju!")
            return None

        novikorisnik = {
            "Korisnicko_ime": ki,
            "Lozinka": l,
            "Ime": i,
            "Prezime": p,
            "Tip_korisnika": t

        }
        s=ucitaj_korisnike()
        s.append(novikorisnik)
        sacuvaj_korisnike(s)
        print("Uspesno ste uneli korisnika.")
        while True:
            print("Da li zelite da nastavite sa unosom kosrisnika?"
                  "\n1. DA"
                  "\n2. NE")
            izbor=int(input("Unesite zeljenu opciju: "))
            if izbor== 1 :
                break
            elif izbor== 2:

                return None
            else:
                print("Uneli ste pogresnu opciju, pokusaj te ponovo!")


def prikaz_svih_korisnika():
    while True:
        print("1.) Sortirajte po imenu")
        print("2.) Sortirajte po prezimenu")
        print("3.) Sortirajte po tipu korisnika")
        bro=0

        opcija=int(input("Unesite zeljenu opciju: "))
        if opcija == 1:
            o=spimenu()


        elif  opcija ==2 :
            o=spprezimenu()


        elif opcija==3 :
            o=sptipu()
        else:
            print("\n\tUneli ste pogresnu opciju!")
            bro=1


        print("Korisnicko ime        Ime                 Prezime                Tip ")
        print("_________________________________________________________________________________________")
        if bro==0:
            for i in o:
                x = i["Korisnicko_ime"]
                q = " " * (20 - len(x))
                w = " " * (15 - len(i["Ime"]))
                e = " " * (20 - len(i["Prezime"]))

                print(x, q, "|", i["Ime"], w, "|", i["Prezime"], e, "|", i["Tip_korisnika"])
        print("\nDa li zelite da nastavite sa prikazom korisnika?"
                  "\n1. DA"
                  "\n2. NE")

        op=int(input("Unesite zeljenu opciju: "))
        if op==1:
                continue

        else:
                return None






def spimenu() :
        x = ucitaj_korisnike()
        z = 0
        for i in range(len(x)):
            for j in range(len(x)):
                if x[i]["Ime"] < x[j]["Ime"]:
                    z = x[i]
                    x[i] = x[j]
                    x[j] = z

        return x
def spprezimenu():
    x = ucitaj_korisnike()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Prezime"] < x[j]["Prezime"]:
                z = x[i]
                x[i] = x[j]
                x[j] = z

    return x


def sptipu():
    x = ucitaj_korisnike()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Tip_korisnika"] < x[j]["Tip_korisnika"]:
                z = x[i]
                x[i] = x[j]
                x[j]= z
    return x