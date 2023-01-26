"""
Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.
"""
print("Anna 5 kaupungin nimet yksi kerrallaan niin tulostan ne allekkain antamassasi järjestysksessä.\n")

kaupungit = []
enter1 = 0
kaupunki = input("Anna kaupunki: ")
while enter1 < 4:
    kaupungit.append(kaupunki)
    kaupunki = input("Anna seuraava kaupunki: ")
    enter1 += 1

print(kaupungit)
