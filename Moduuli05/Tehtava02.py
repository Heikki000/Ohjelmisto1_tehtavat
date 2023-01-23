"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla
sort-metodille argumentiksi reverse=True.
"""
print("Anna numeroita ja lopuksi paina ENTER, niin saat listan 5 suurimmasta luvusta suurimmasta alkaen: ")
luvut = []
luku = input("Anna ensimmäinen luku: ")
while luku != "":
    luvut.append (int(luku))
    luku = input("Anna seuraava luku tai lopeta painamalla ENTER: ")

luvut.sort(reverse=True)

print(f"{luvut[0:5]}")