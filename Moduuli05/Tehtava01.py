"""Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta."""
print()
print("Ohjelma heittää niin monta arpakuutioita kun haluat!\n")


import random
summa = 0
lukumäärä = int(input("Anna kuutioiden määrä: "))

for index in range(lukumäärä):
    noppa = random.randint(1, 6)
    print(f"Nopan silmäluku on {noppa}.")
    summa = summa + noppa

print(f"\nNoppien summa on {summa}!")

"""
print()
kuutiot = int(input("Anna arpakuutioiden lukumäärä: "))
"""