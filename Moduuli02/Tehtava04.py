"""
Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
"""
import math
print("Anna kolme kokonaislukua!")
one = input()
two = input()
three = input()

sum = int(one) + int(two) + int(three)
tulo = int(one) * int(two) * int(three)
average= (int(one) + int(two) + int(three)) / 3

print("Antamiesi lukujen summa on " + str(sum) + ".")
print("Antamiesi lukujen tulo on " + str(tulo) + ".")
print(f"Antamiesi lukujen keskiarvo on  {average:.1f}.")