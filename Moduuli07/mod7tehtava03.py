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
    nimi = input("Anna lentoaseman nimi: ")
    tunnus = input("Anna lentoaseman ICAO-koodi: ")
    lentoasemat[tunnus] = nimi
    return

def hae():
    tunnus = input("Anna lentoaseman ICAO koodi (esim. 'ABCD': ")
    if tunnus in lentoasemat:
        print("Tunnusta vastaava lentoasema on " + lentoasemat[tunnus] + ".")
    return

def lopeta():
    return

def tulosta():
    for asema in lentoasemat:
        print(f"{lentoasemat}")
        return

#pääohjelma

lentoasemat = {"EFHK": "Helsinki-Vantaa","EFIV": "Ivalo",
               "EFKS": "Kuusamo", "EFOU": "Oulu"}

toiminto = -1

while toiminto != 3:
    print("0 = Tulosta lentoasemat")
    print("1 = Lisää uusi lentoasema")
    print("2 = Hae lentoasema")
    print("3 = Lopeta")

    toiminto = int(input("Valitse toiminto: "))
    if toiminto == 0:
        tulosta()
    if toiminto == 1:
        lisaa()
    if toiminto == 2:
        hae()
    if toiminto == 3:
        lopeta()
#print(lentoasemat) testataan, mitkä asemat sanakirjassa
print("\nOhjelma lopetettu!")