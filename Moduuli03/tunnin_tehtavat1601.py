#"tunnin tehtävät ja asiat 16.1.23 klo 13-16"
#int = kokonaisluku
#float = desimaaliluku
# jakolaskuna pythonissa // palauttaa aina KOKONAISLUVUN! desimaalin sijaan (edellisen moduulin kilogrammatehtävä)
# HUOM! yhtäsuuruusmerkki on == eli 2 x =
"""
rahat = float(input("Anna rahamäärä: "))
if rahat>=5:
    print("Voit ostaa latten.")

ika = int(input("Anna ikasi:"))
if (ika >=18):
    print("Olet siis taysi-ikainen.")
    aika = ika - 18
    print(f"Olet ollut sitä jo {aika} vuotta")
    """
print("Yritä antaa parillinen kokonaisluku väliltä 11..20")
luku = int(input("Anna lukusi: "))
#testataan että täyttääkö luku ehdot vai ei
if((11<= luku <= 20) and luku % 2 == 0):
    print("Kato osasit!")
else:
    print("Tollo!")

#tämä tulostetaan aina:
print("Ohjelma loppui.")