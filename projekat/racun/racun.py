
from repoz_projekat.projekat.racun.racunIO import ucitaj_racun, sacuvaj_racun
from repoz_projekat.projekat.Knjige.knjigeIO import ucitaj_knjige



def prodaja_knjiga():
    knjige=ucitaj_knjige()

    korpa=[]
    ukcena=0
    proizvod=0
    while True:
        print(knjige)
        x=int(input("\n\tUnesite sifru knjige koju zelite da kuipte: "))
        for i in knjige:
            if i["Sifra"]==x:
                    korpa.append(i)
                    z = int(input("Unesite kolicinu koju zelite da kupite: "))
                    proizvod=proizvod+z
                    print("Imate  ",proizvod, "proizvoda tenutno u korpi")


                    ukcena = ukcena+i["Cena"] * z
                    print("Ukupna cena: ",ukcena, "dinara")
                    print("\nDa li zelite da pogledate korpu?"
                          "\n1.) DA"
                          "\n2.)NE")
                    j=int(input("Unesite zeljenu opciju"))
                    if j==1:
                        print("Trenutno u korpi imate:")
                        for g in korpa:
                            print(g, )

                    print("\nDa li zelite da nastavite sa kupovinom?"
                          "\n1.) DA"
                          "\n2.) NE")

                    l=int(input("Unesite zeljenu opciju"))
                    if l==2:
                        print("\n1.) Pregled korpe")
                        print("2.) Izlaz")