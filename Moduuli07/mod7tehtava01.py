"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
(kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
"""
vuodenajat = ("syksy", "talvi", "kevät", "kesä")
#syksy = (9, 10, 11)
#talvi = (12, 1, 2)
#kevät = (3, 4, 5)
#kesä = (6, 7, 8)
#vuodenaika = ((9,10,11),(12,1,2),(3,4,5),(6,7,8))
kk_nro = int(input("Anna kuukauden numero (1-12): "))

if (kk_nro == 12 or kk_nro == 1 or kk_nro == 2):
    vuodenaika = vuodenajat[1]
elif (kk_nro >= 3 and kk_nro <= 5):
    vuodenaika = vuodenajat[2]
elif (kk_nro >= 6 and kk_nro <= 8):
    vuodenaika = vuodenajat[3]
elif (kk_nro >= 9 and kk_nro <= 11):
    vuodenaika = vuodenajat[0]
else:
    vuodenaika = "tuntematon"
print(vuodenaika)
#vuodenajat[print(f"Antamasi kuukausi, {kk_nro} vastaa vuodenaikaa str{vuodenaika}.")