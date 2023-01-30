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
    return float(neliohinta)

print("Ohjelma kertoo sinulle, kumpi pitsoista on yksikköhinnaltaan edullisempi.")

hinta1 = float(input("Anna ensimmäisen pitsan myyntihinta euroina:"))
halkaisija1 = float(input("Anna ensimmäisen pitsan halkaisija (cm):"))
yks_hinta(hinta1, halkaisija1)
neliohinta1 = float(yks_hinta(hinta1, halkaisija1))

hinta2 = float(input("Anna toisen pitsan myyntihinta euroina:"))
halkaisija2 = float(input("Anna toisen pitsan halkaisija (cm):"))
yks_hinta(hinta2, halkaisija2)
neliohinta2 = float(yks_hinta(hinta2, halkaisija2))

# testataan hinntojen oikeellisuus:
# print(f"{neliohinta1:.2f} ja {neliohinta2:.2f}.")
print()
if neliohinta1 < neliohinta2:
    print("Ensimmäinen pitsa antaa paremman vastineen rahoille!")
elif neliohinta1 == neliohinta2:
    print("Pitsat ovat samanhintaiset!")
else:
    print ("Toinen pitsa antaa paremman vastineen rahoille!")

