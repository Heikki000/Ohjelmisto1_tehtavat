"""
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden
lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon
miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman
yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)
"""

def lisaa():
    tunnus = input("Anna lentoaseman tunnus: ")
    nimi = input("Anns lentoaseman nimi")
    lentoasemat[tunnus] = nimi
    
    return

def hae():
    tunnus = input("Anna lentoaseman ICAO koodi: ")
    if tunnus in lentoasemat:
        print
    return

def lopeta():
    return

#pääohjelma

lentoasemat = {"Helsinki-Vantaa": "EFHK" ,"Ivalo" : "EFIV" ,
               "Kuusamo" : "EFKS" , "Oulu" : "EFOU"}

toiminto = -1

while toiminto != 3:
    print("1 = Lisää uusi lentoasema")
    print("2 = Hae lentoasema")
    print("3 = Lopeta")

    toiminto = int(input("Valitse toiminto: "))
    if toiminto == 1:
        lisaa()
    if toiminto == 2:
        hae()
    if toiminto == 3:
        lopeta()
print(lentoasemat)
print("\nOhjelma lopetettu!")