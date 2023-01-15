"""
Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

Yksi leiviskä on 20 naulaa.
Yksi naula on 32 luotia.
Yksi luoti on 13,3 grammaa.
"""
import math
print()
print("Kerro minulle massa keskiaikaisina mittoina leivisköinä, nauloina ja luoteina")
print("niin muutan sen kilogrammoiksi ja grammoiksi sinulle:")
print()
leiv_str = input("Leivisköiden määrä:")
naula_str = input("Naulojen määrä:")
luoti_str = input("Luotien määrä:")
#muutetaan numeroiksi
leiv = float(leiv_str)
naula = float(naula_str)
luoti = float(luoti_str)
#muutetaan grammoiksi
luoti2 = 13.3 * luoti
naula2 = 32 * 13.3 * naula
leiv2 = 20 * 32 * 13.3 * leiv

massaGramma = luoti2 + naula2 + leiv2
massaKg = math.floor(massaGramma / 1000)
massaG = massaGramma - massaKg * 1000


print(f"Antamasi massa on yhteensä {massaKg:.0f} kg ja {massaG:.1f} grammaa.")