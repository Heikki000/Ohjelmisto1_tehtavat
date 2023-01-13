"""
tehtävä 6
Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
"""
import random
# pythonin käytäntö nimeämisessä alaviiva, mutta joissain muissa ok käyttää isoja ja pieniä kirjaimia "randomNumber"
random_number = random.randint(1, 6)
print(f"Arpa on heitetty: {random_number}")