"""
Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
"""
# = pi x r ^ 2
import math
r = float(input("Anna ympyrän säde (m): "))
area = math.pi * r * r
# potenssiin 2 voi myös merkitä r**2
print()
print(f"Ympyrän pinta-ala on {area:.2f} neliömetriä.")