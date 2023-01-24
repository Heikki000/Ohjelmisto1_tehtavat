"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
"""
print("Anna lukuja ja paina lopuksi ENTER niin kerron, mitkä luvut olivat suurin ja pienin.")
luku = (input("Anna luku: "))
iso = int(luku)
pieni = int(luku)

while luku != "":
    luku = input("Anna luku: ")
    if luku != "":
        luku = int(luku)
        if luku > iso:
            iso = luku
        elif luku < pieni:
            pieni = luku

print(f"Suurin antamasi luku oli {iso} ja pienin luku oli {pieni} !")

print("Ohjelma loppu!")

"""
while luku != "":            
    luku = input("Anna luku: ")
    luku = int(luku)
    if luku > iso:
        iso = luku
    elif luku < pieni:
        pieni = luku
else:
    print(f"Suurin antamasi luku oli {iso} ja pienin luku oli {pieni} !")
"""



"""
while luku == float:
    luku = float(input("Anna luku: "))
while luku == "":
    print(f"Suurin antamasi luku oli {max(luku)} ja pienin luku oli {min(luku)} !")

    print()
print("Ohjelma loppu!")
"""