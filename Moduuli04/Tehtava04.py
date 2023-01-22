"""
Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
"""
import random
arpa = random.randint(1, 10)
print("Kone on arponut kokonaisluvun väliltä 1..10. Osaatko arvata sen?")
#print(arpa) #testataan, toimiiko numeron kanssa oikein
arvaus = float(input("Anna arvauksesi: "))
while arvaus != arpa:
    if arvaus < arpa:
        arvaus = float(input("Liian pieni arvaus. Arvaappa uudelleen: "))
    elif arvaus > arpa:
        arvaus = float(input("Liian suuri arvaus. Arvaappa uudellen:"))
while arvaus == arpa:
   break
print("\nOikein!")