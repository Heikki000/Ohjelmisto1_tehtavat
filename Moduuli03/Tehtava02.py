"""
Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja
tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
Tehtävässä on käytettävä if/elif/else-toistorakennetta.

LUX on parvekkeellinen hytti yläkannella.
A on ikkunallinen hytti autokannen yläpuolella.
B on ikkunaton hytti autokannen yläpuolella.
C on ikkunaton hytti autokannen alapuolella.

Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.
"""
luokka= input("Anna hyttiluokka: ")
if (luokka == "LUX" or luokka == "lux"):
    print("LUX on parvekkeellinen hytti yläkannella.")

elif (luokka == "A" or luokka == "a"):
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif (luokka == "B" or luokka == "b"):
    print("B on ikkunaton hytti autokannen yläpuolella.")

elif (luokka == "C" or luokka == "c"):
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka.")