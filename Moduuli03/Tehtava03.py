"""
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
"""
sukupuoli = input("Anna sukupuolesi (n/m)")
hg = float(input("Anna hemoglobiiniarvosi."))

if sukupuoli == "m":
    if hg < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hg > 195:
        print ("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

if sukupuoli == "n":
    if hg < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hg > 175:
        print ("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
else:
    print("Antamasi arvo ei ole kelvollinen.")