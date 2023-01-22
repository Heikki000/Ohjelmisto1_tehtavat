"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
"""
luku = float(input("Anna lukuja ja paina lopuksi 'ENTER' niin kerron, mitkä luvut olivat suurin ja pienin:"))
while luku != '3':
    luku = (input("Anna luku: "))
else:
    print(f"Suurin antamasi luku oli {max(luku)} ja pienin luku oli {min(luku)} !")

print()
print("Ohjelma loppu!")
