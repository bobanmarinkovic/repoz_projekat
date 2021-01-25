from repoz_projekat.projekat.korisnici.korisnici import prijava
from repoz_projekat.projekat.Knjige.knjige import prikaz_svih_knjiga
from repoz_projekat.projekat.Knjige.knjige import pretrazi_knjige
from repoz_projekat.projekat.korisnici.korisnici import registracija
from repoz_projekat.projekat.korisnici.korisnici import prikaz_svih_korisnika
from repoz_projekat.projekat.Knjige.knjige import izmena_knjige
from repoz_projekat.projekat.Knjige.knjige import dodavanje_knjige
from repoz_projekat.projekat.Knjige.knjige import prodaja_knjiga
from repoz_projekat.projekat.kcije.Akcije import Prikaz_akcija
from repoz_projekat.projekat.kcije.Akcije import pretraga_akcija
from repoz_projekat.projekat.kcije.Akcije import kreiranje_akcijske_ponude

def Prijava():
    x= prijava()
    if x==None:
        print('Neuspela prijava')
        return None
    else:
        print('Prijavljeni ste kao:', x['Tip_korisnika'])
    if x['Tip_korisnika']=='Administrator':
        administrator()
    elif x['Tip_korisnika']=='Menadzer':
        menadzer()
    else:
        prodavac()


def administrator():
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
            prikaz_svih_knjiga()
    elif m == 2:
            pretrazi_knjige()
    elif m==3:
            Prikaz_akcija()
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
            return None





def menadzer():
    print('1.) Prikaz knjiga')
    print('2.) Pretraga knjiga')
    print('3.) Prikaz akcija')
    print('4.) Pretraga akcija')
    print('5.) Registracija')
    print('6.) Prikaz svih korisnika')
    print('7.) Kreiranje akcijske ponude')
    print('8. Kreiranje izvestaja')
    print('9.) Izlaz')

    m = int(input("Izaberite opciju: "))
    if m == 1:
        prikaz_svih_knjiga()
    elif m == 2:
        pretrazi_knjige()
    elif m==3:
        Prikaz_akcija()
    elif m==4:
        pretraga_akcija()
    elif m==5:
        registracija()
    elif m==6:
        prikaz_svih_korisnika()
    elif m==7:
            kreiranje_akcijske_ponude()
    elif m==8:
            kreiranje_izvestaja()
    else:
            return None

def prodavac():
    print('1.) Prikaz knjiga')
    print('2.) Pretraga knjiga')
    print('3.) Prikaz akcija')
    print('4.) Pretraga akcija')
    print('5.) Prodaja knjiga')
    print('6.) Dodavanje knjige')
    print('7.) Izmena knjige')
    print('8.) Logicko brisanje knjige')
    print('9.) Izlaz')

    m = int(input("Izaberite opciju: "))
    if m == 1:
        prikaz_svih_knjiga()
    elif m == 2:
        pretrazi_knjige()
    elif m == 3:
        Prikaz_akcija()
    elif m == 4:
        pretraga_akcija()
    elif m == 5:
        prodaja_knjiga()
    elif m == 6:
        dodavanje_knjige()
    elif m == 7:
        izmena_knjige()
    elif m == 8:
        logicko_brisanje_knjige()
    elif m == 9:
        return
Prijava()
