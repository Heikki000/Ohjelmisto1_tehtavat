"""
Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
Vuosi on karkausvuosi, jos se on jaollinen neljällä.
Sadalla jaolliset vuodet ovat karkausvuosia
VAIN jos ne ovat jaollisia myös neljälläsadalla.
"""
print("Ohjelma kertoo, onko antamasi vuosiluku karkausvuosi.")
vuosi = int(input("Anna vuosiluku: "))
if(vuosi % 4 == 0):
    if(vuosi % 400 == 0 or vuosi % 100 != 0):
        print(f"Antamasi vuosi, {vuosi} on karkausvuosi!")
    else:
        print(f"Antamasi vuosi, {vuosi} ei ole karkausvuosi!")