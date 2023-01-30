"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu
lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan,
kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
"""
def ei_parittomia(objekti_lista):
    muokattu_lista = []
    for luku in objekti_lista:
        if luku % 2 == 0:
            muokattu_lista.append(luku)
    return muokattu_lista


testi_lista = [1, 23, 45, 67, 100, 200]
print("Alkuperäinen lista on " + str(testi_lista) + ".")
#print(testi_lista)
print("\nMuokattu lista ilman parittomia lukuja on " + str(ei_parittomia(testi_lista)) + ".")
#print(testi_lista)
