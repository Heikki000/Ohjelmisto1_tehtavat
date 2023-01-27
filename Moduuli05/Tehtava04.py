"""
Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.
"""
print("Anna 5 kaupungin nimet yksi kerrallaan niin tulostan ne allekkain antamassasi järjestykssessä.\n")
kaupungit = []
for kaupunki in range(5):
    kaupungit.append(input("Anna kaupunki: "))
print()

"""
KÄYTTÄEN WHILE-TOISTORAKENNETTA

enter1 = 1
kaupunki = input("Anna kaupunki: ")
kaupungit.append(kaupunki)

while enter1 < 5:
    enter1 += 1
    kaupunki = input("Anna seuraava kaupunki: ")
    kaupungit.append(kaupunki)
"""
for kaupunki in kaupungit:
    print(f"{kaupunki}")
