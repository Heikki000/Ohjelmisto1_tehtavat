"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma,
jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
"""

def summa(numerolista):
    for n in numerolista:
        #print(sum(numerolista))
        return (sum(numerolista))

lista = [1, 2, 3, 4, 5]
summa(lista)
print(summa(lista))
