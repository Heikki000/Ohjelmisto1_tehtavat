"""
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
Kuha on alamittainen, jos sen pituus on alle 37 cm.
"""

pituus = float(input("Anna kuhan pituus senttimetreinä (cm):"))
if pituus < 37:
    print("Kuha on alamittainen.")
    ero = 37 - pituus
    print(f"Laske kuha takaisin järveen, koska alimmasta sallitusta pyyntimitasta puuttuu {ero:.1f} senttimetriä.")