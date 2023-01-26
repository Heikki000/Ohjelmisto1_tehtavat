"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
"""
# % 0 jakojäännös
number = int(input("Anna luku:"))
is_prime = True

for iterator in range(2, number):
    print(f"testataan lukua jakamalla se arvolla {iterator}")
    print(f"jakojäännös: {number % iterator}")
    if number % iterator == 0:
        print(f"{number} ei ole alkuluku.")
        is_prime = False
        break

# if is_prime == true:
if is_prime:
    print(f"{number} on alkuluku.")
