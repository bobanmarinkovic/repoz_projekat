from repoz_projekat.projekat.korisnici.korisnici import prijava

def prijava():
    x= prijava()
    if x==None:
        print('Neuspela prijava')
        return None
    else:
        print('Prijavljeni ste kao:', korisnik['tip_korisnika'])


def adimistrator():
    print('1.) Prikaz knjiga')
    print('2.) Pretraga knjiga')
    print('3.) Prikaz akcija')
    print('4.) Pretraga akcija')
    print('5.) Registracija')
    print('6.) Prikaz svih korisnika')
    print('7.) Dodavanje knjige')
    print('8.) Izmena knjige')
    print('9.) Logicko brisanje knjige')
    print('10.) Izlaz')

    m = int(input("Izaberite opciju: "))
    if m == 1:
        prikaz_knjige()
    elif m == 2:
        pretrazi_knjige()
    elif m==3:
        prikaz_akcije()
    elif m==4:
        pretraga_akcija()
    elif m==5:
        registracija()
    elif m==6:
        prikaz_svih_korisnika()
    elif m==7:
        dodavanje_knjige()
    elif m==8:
        izmena_knjige()
    elif m==9:
        logicko_brisanje_knjige()
    elif m==10:
        return

adimistrator()

def prikaz_knjige():

    print('1.) Sortirajte po naslovu knjige')
    print('2.) Sortirajte po kategoriji')
    print('3.) Sortirajte po autoru')
    print('4.) Sortirajte po izdavacu')
    print('5.) Sortirajte po ceni')
    print('6.) Izlaz')

    m=int(input('Izaberte opciju:'))
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





adimistrator()
