# huom tentti ap 9.2. (harjoitustenttimahdollisuus 2.2.)
# globaalit muuttujat on määritelty "ulkona"
#lokaalit muuttujat on määritelty vain sisennetyille muuttujille

#globaaleja muuttujia
to_whom ="jollekin"
something = "jotain globaalia"

def say_hello(to_whom):
    to_whom = to_whom.upper()
    print(f"Terve {to_whom}!")
    print(f"ja heippa, {to_whom}")
    #tulostetaan globaalin muuttujan arvo
    print(something)
    return "valmista tuli"

to_whom = "Kalle"
result = say_hello("Kalle")
print(result)
print(say_hello("Viivi"))
#globaalin muuttujan arvo on pysynyt samana
print(to_whom)

def calculateSum(number1, number2):
    return number1 + number2

print(calculateSum(11, 34))
import random
# mod t4 funktion avulla
correct_int = random.randint(1,10)
print(correct_int)

def checkGuess(guess):
    if guess < correct_int:
        return 'Liian pieni arvaus'
    elif guess > correct_int:
        return ' Liian suuri arvaus'
    else:
        return 'Oikein!'
#pääohjelma (arvauspeli) omassa funktiossaan
def guessGame():
    game_on = True
    while game_on:
        user_guess = int(input("Arvaa luku:"))
        result = checkGuess(user_guess)
        print(checkGuess(user_guess))
        if result == 'Oikein!':
            print("Peli loppui!")
            game_on = False

# guessGame()

#lista parametrina(materiaalista)
def inventaario(tavarat):
    tavarat.append("tussi")
    print("Sinulla on seuraavat tavarat:")
    for tavara in tavarat:
        print("- " + tavara)

koulureppu = ["kynä", "kumi", "viivotin"]
inventaario(koulureppu)
print(koulureppu)
#listajuttuja
# tulostetaan kaikki alkiot : for in
lista = [1, 3, 4, 5, 6]
for number in lista:
    print(number)
print("---------------")
#tulostetaan joka toisen alkion arvo
for i in range(len(lista)):
    if i%2 == 0:
        print(lista[i])

#listan kopiointi
lista2 = lista.copy()
lista2.remove(3)
print(lista)
