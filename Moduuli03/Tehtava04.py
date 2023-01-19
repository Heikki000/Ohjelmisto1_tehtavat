"""
Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia
vain jos ne ovat jaollisia myös neljälläsadalla.
"""
Print:("Ohjelma kertoo, onko antamasi vuosiluku karkausvuosi.")
vuosi = int(input("Anna vuosiluku"))
if(vuosi % 4 == 0):
    if(vuosi % 400 == 0 or vuosi % 100 != 0):
        print("Antamasi vuosi on karkausvuosi")
    else:
        (print("Vuosi ei ole karkausvuosi!"))