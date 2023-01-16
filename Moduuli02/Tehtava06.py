"""
tehtävä 6
Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
"""
import random
# pythonin käytäntö nimeämisessä alaviiva, mutta joissain muissa ok käyttää isoja ja pieniä kirjaimia "randomNumber"

random_number1 = random.randint(0, 9)
random_number2 = random.randint(0, 9)
random_number3 = random.randint(0, 9)
#code = str(random_number1) + str(random_number2) + str(random_number3)
code = f"{random_number1}{random_number2}{random_number3}"

random_number4 = random.randint(1, 6)
random_number5 = random.randint(1, 6)
random_number6 = random.randint(1, 6)
random_number7 = random.randint(1, 6)
code2 = f"{random_number4}{random_number5}{random_number6}{random_number7}"


print(f"Numerolukon kolmenumeroinen koodi on: {code}")
print(f"Numerolukon nelinumeroinen koodi on: {code2}")
