"""
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
"""
import math
#ympyrän pinta-alan kaava on pi * r^2
# säde, r on halkaisija, d / 2 -> pinta-ala halkaisijan avulla on pi/4 * d^2

def yks_hinta(hinta, halkaisija):
    neliohinta = hinta / (math.pi/4*halkaisija)
    return neliohinta

hinta = float(input("Anna pitsan myyntihinta:"))
halkaisija = float(input("Anna pitsan halkaisija (cm):"))
print(yks_hinta(hinta, halkaisija))

