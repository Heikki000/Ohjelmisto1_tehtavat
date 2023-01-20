"""
while = niin kauan kuin....
for = tietty määrä toistoja
mutta eivät ole täysin toistensa sulkevia ja ero ei niin tarkkarajainen
number = 1
while number <= 5:
    #number += 1
# number+= 1 on lyhenne asiasta number = number + 1
    print(f"tulostetaan jotain, kierros: {number}")
    number = number + 1
    print("tulostetaan vaikka arvo olisi jo 6")
print("silmukan suoritus lopppui")
print(f"number-muuttujan arvo lopuksi: {number}")
"if-lauseella tämä testattaisiin vain 1 kerran (eli se on valintarakenne)"
"""
# iteroiva while-looppi
times = int(input("Montako kierrosta ajetaan?"))
number = 1
while number <= times:
    #number += 1
# number+= 1 on lyhenne asiasta number = number + 1
    print(f"tulostetaan jotain, kierros: {number}")
    number = number + 1
    print("tulostetaan vaikka arvo olisi jo 6")
print("silmukan suoritus lopppui")
print(f"number-muuttujan arvo lopuksi: {number}")

#käyttäjästä riippuva toisto ja sisäkkäinen if-else
application_running = True
while application_running:
    command =input("Anna komento:")
    if command == 'lopeta':
        application_running = False
    elif command == "kerro vitsi":
        print("Chuck Morris...")
    else:
        print("ok, jatketaan sitten")
    print("jatketaan suoritusta")

print("Ohjelman suoritus loppuu")

#noppaesimerkki materiaalista
import random
noppa1 = noppa2 = heitot = 0
while (noppa1 != 6 or noppa2 != 6):
    noppa1 = random.randint(1, 6)
    noppa2 = random.randint(1, 6)
    heitot = heitot + 1
    print(f"{heitot}, kierrokset tulokset: {noppa1}, {noppa2}:")
print(f"Tarvittiin {heitot:d} heittoa.")









