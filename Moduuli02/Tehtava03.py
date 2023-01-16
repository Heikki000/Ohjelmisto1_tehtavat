"""
Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
Ohjelma tulostaa suorakulmion piirin ja pinta-alan. Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.
"""

print("Anna suorakulmion kanta (cm):")
kanta = float(input())
print("Anna suorakulmion korkeus (cm):")
korkeus = float(input())
pintaala = int(kanta) * int(korkeus)
piiri = int(kanta) * 2 + int(korkeus) * 2

#print("Suorakulmion pinta-ala on " + str(pintaala) + " cm^2 ja piiri on " + str(piiri) + " cm.")
#tai vastaavasti f-stringiä käyttäen:
print(f"Suorakulmion pinta-ala on {pintaala} cm^2 ja piiri on {piiri} cm.")