"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
joka kysytään käyttäjältä ohjelman suorituksen alussa.
"""

import random

def roll_die(number_of_sides):
    return random.randint(1, number_of_sides)

#roll_die(number_of_sides)

def play_game():
    result = 0
    while result != number_of_sides:
        result = roll_die(number_of_sides)
        print(result)

number_of_sides = int(input("Anna nopan tahkojen määrä eli maksimisilmäluku: "))

play_game()