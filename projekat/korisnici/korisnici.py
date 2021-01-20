from repoz_projekat.projekat.korisnici.KorisnikIO import ucitaj_korisnike, sacuvaj_korisnike
def prijava():
    korisnici= ucitaj_korisnike()

    br = 0
    for br in range(3):
        k_i = input("Unesite korisnicko ime: ")
        l = input("Unesite lozinku: ")

        for i in korisnici:
            if i['Korisnicko_ime'] == k_i and i['Lozinka'] == l:
                return korisnik
    return None

def Registracija():
    korisnickoime= input("Unesite zeljeno korisnicko ime: ")
    lozinka= input("Unesite lozinku: ")
    korisnici= ucitaj_korisnike()
    for i in korisnici:
        if korisnickoime == i["Korisnicko_ime"]:
            print("Korisnicko ime je zauzeto, pokusaj te ponovo.")
        else:
            break
    ime=input("Unesite ime: ")
    prezime=input("Unesite prezime: ")
    tipkorisnika=input("Unesite da li je novi korisnik prodavac (unosenjem broja 1) ili menadzer (unosenjem broja 2): " )
    if tipkorisnika!= 1 or tipkorisnika!= 2:
                print("Nije moguce uneti korisnika!")
    else:
            return None


    novikorisnik={
        "Korisnicko_ime": '',
        "Lozinka": '',
        "Ime": '',
        "Prezime": '',
        "Tip_korisnika": ''

}
    novikorisnik['Korsnicko_ime']=korsnickoime
    novikorisnik['Lozinka']= lozinka
    novikorisnik['Ime']=ime
    novikorisnik['Prezime']=prezime
    if tipkorisnika==1:
            x='Prodavac'
    else:
            x='Menadzer'
    novikorisnik['Tip_korisnika']=x
    nk=[novikorisnik]
    list_one(nk)
    sacuvaj_korisnike(korisnici)

