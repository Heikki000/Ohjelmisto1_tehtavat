"""
Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
"""
print("Ohjelma tulostaa kolmella jaolliset luvut väliltä 1..1000")
print()
times = 1000
number = 0
while number < times:
    number += 1
#   print(number) testaa, että ohjelma käy läpi kaikki halutut numerot
    if number % 3 == 0:
        print(number)
print("Ohjelma valmis!")



