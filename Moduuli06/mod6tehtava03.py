"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja
palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma,
joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.
"""
gallona = 0
def konversio(gallona):
    litra = float(gallona * 3.785)
    #print(litra)
    return litra

konversio(gallona)
#gallona = 0
while gallona >= 0:
    gallona = float(input("Anna tilavuus nestegallonoina: "))
    if gallona > 0:
        litra = konversio(gallona)
        print(f" Antamasi tilavuus litroina on {litra} litraa.")

#kutsuu aliohjelman tuloksen
litra = konversio(gallona)

#if gallona >= 0:
    #print(f"\nAntamasi tilavuus litroina on {litra} litraa.")
