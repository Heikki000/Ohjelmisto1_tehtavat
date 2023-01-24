"""
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).

tunnus = str(python)
salasana = str(rules)
print("Anna käyttäjätunnus ja salasana:")
tunnus1 = input("käyttäjätunnus: ")
while tunnus1 != tunnus:
    salasana1 = input("salasana: ")
    if salasana1 == salasana:
        tunnus1 = input(str("Väärin, anna käyttäjätunnus:"))
    elif salasana1 != salasana:
        tunnus1 = input("Väärin, anna käyttäjätunnus: ")
else:
    salasana1 = input("salasana: ")
    if salasana1 == salasana:
        print("Tervetuloa!")
"""
kerta = 0
while kerta < 5:
    tunnus = input("Anna käyttäjä: ")
    salasana = input("Anna salasana: ")
    if tunnus == 'python' and salasana == 'rules':
        print("\nTervetuloa!")
        kerta = 5
    else:
        print("Annoit väärät tiedot, yritä uudelleen!")
        kerta += 1
        if kerta == 5:
            print("Pääsy evätty, liian monta yritystä!")

