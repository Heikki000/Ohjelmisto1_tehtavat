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
    if number == 2:
        break
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
    elif command == 'noppa':
        import random

        noppa1 = noppa2 = heitot = 0
        tuli_samat = False
        while (noppa1 != 6 or noppa2 != 6):
            noppa1 = random.randint(1, 6)
            noppa2 = random.randint(1, 6)
            if noppa1 == noppa2 == 6:
                tuli_samat = True
            heitot = heitot + 1
            print(f"{heitot}, kierrokset tulokset: {noppa1}, {noppa2}:")
        print(f"Tarvittiin {heitot:d} heittoa.")
    else:
        print("ok, jatketaan sitten")
    print("jatketaan suoritusta")

print("Ohjelman suoritus loppuu")

#noppaesimerkki materiaalista
import random
noppa1 = noppa2 = heitot = 0
tuli_samat = False
while (noppa1 != 6 or noppa2 != 6):
    noppa1 = random.randint(1, 6)
    noppa2 = random.randint(1, 6)
    if noppa1 == noppa2 == 6:
            tuli_samat = True
    heitot = heitot + 1
    print(f"{heitot}, kierrokset tulokset: {noppa1}, {noppa2}:")
print(f"Tarvittiin {heitot:d} heittoa.")
# sisin suoritetaan aina loppuun ja sitten ajetaan ulompi niin kauan kuin jokin ehto on tosi jne......
# while/else rakennetta ei ole kai monissakaan ohjelmointikielissä joten tosi harvoin kai käytössä.......









