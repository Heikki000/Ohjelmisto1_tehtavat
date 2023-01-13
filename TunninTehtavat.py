import math
#importit käytännön mukaan aina koodin alussa
print("huomenta user!")
#kommentti, muuttujan esittely ja arvon sijoittaminen muuttujaan
# yleensä kommentteja mahdollisimman vähän ja koodi sen verran helppolukuista ettei niitä tarvitse
#kotitehtävissä kuitenkin kommentit hyviä jne...

print()

#syötteen lukeminen käyttäjältä
name = input("Anna nimesi:")
ageString = input("Anna ikäsi")
# arvon tyypin muunnos merkkijojo (string) -> kokonaisluku(int)
#  int("3") -> 3
age = int(ageString)
age = age + 1
print("")
message = "Huomenta " + name + ", olet ensi vuonna " + str(age) + "-vuotias."
print(message)
# sama käyttäen f-stringiä (joka tunnistaa mm esim numerot, joten ei tarvita esim str(age)
message_f = f"Morjes {name}, olet ensi vuonna {age:3.0f}-vuotias."
print(message_f)
print("END")
print(f"Piin likiarvo by Python:{math.pi:.5f}")