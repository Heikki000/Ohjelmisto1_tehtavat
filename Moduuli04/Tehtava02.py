"""
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
"""

tuuma = float(input("Anna tuumien määrä niin muutan sen sinulle senttimetreiksi: "))

while tuuma > 0:
    print(f"Antamasi luku on senttimetreinä {tuuma * 2.54} senttimetriä. ")
    tuuma = float(input("Anna tuumien määrä: "))
else:
    print()
    print("Taisit antaa virheellisen luvun.")

print("Ohjelma loppu.")