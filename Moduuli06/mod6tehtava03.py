"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja
palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma,
joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.
"""

def konversio(gallona):
    litra = float(gallona * 3.785)
    #print(litra)
    return litra

gallona = 0

while gallona >= 0:
    gallona = float(input("Anna tilavuus nestegallonoina: "))
    if gallona >= 0:
        litra = konversio(gallona)
        print(f" Antamasi tilavuus litroina on {litra:.2f} litraa.")

print("\nOhjelma loppu.")
