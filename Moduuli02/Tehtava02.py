"""
Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
"""
# = pi x r ^ 2
import math
r = float(input("Anna ympyrän säde (m): "))
area = math.pi * r * r

print(f" Ympytän pinta-ala on {area} neliömetriä.")