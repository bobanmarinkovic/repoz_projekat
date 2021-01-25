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
    s=ucitaj_korisnike()
    ki=input("Unesite zeljeno korisnicko ime: ")
    for z in s:
        if ki == z["Korisnicko_ime"]:
            print("Korisnicko ime je zauzeto!")
            return None

    l=input("Unesite zeljenu lozinku: ")
    i=input("Unesite ime: ")
    p=input("Unesite prezime: ")
    m = input("Unesite da li je novi korisnik  menadzer (unosenjem broja 1), prodavac (unosenjem broja 2) ili nesto drugo (unosenjem broja 3): ")


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

def prikaz_svih_korisnika():
    print("1.) Sortirajte po imenu")
    print("2.) Sortirajte po prezimenu")
    print("3.) Sortirajte po tipu korisnika")

    m=input("Unesite zeljenu opciju: ")
    if m == 1 :
        o=spimenu()

    elif  m ==2 :
        o=spprezimenu()


    else :
        o=sptipu()

    print("Korisnicko ime     Ime      Prezime   Tip ")
    for i in o:
        x=i["Korisnicko_ime"]
        print(x, i["Ime"] , i["Prezime"], i["Tip_korisnika"])




def spimenu() :
    x = ucitaj_korisnike()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Ime"] < x[j]["Ime"]:
                z = x[i]["Ime"]
                x[i]["Ime"] = x[j]["Ime"]
                x[j]["Ime"] = z
    return x
def spprezimenu():
    x=ucitaj_korisnike()
    z=0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Prezime"] < x[j]["Prezime"]:
                z = x[i]["Prezime"]
                x[i]["Prezime"] = x[j]["Prezime"]
                x[j]["Prezime"] = z
    return x


def sptipu():
    x = ucitaj_korisnike()
    z = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]["Tip_korisnika"] < x[j]["Tip_korisnika"]:
                z = x[i]["Tip_korisnika"]
                x[i]["Tip_korisnika"] = x[j]["Tip_korisnika"]
                x[j]["Tip_korisnika"] = z
    return x