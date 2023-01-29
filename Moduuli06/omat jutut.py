lista = [1, 2, 3, 10]

for alkio in lista:
    print(alkio * 2)


def muokkaa(sanoja):
    lista2 = []
    for solu in sanoja:
        if solu < 3:
            lista2.append(solu)
    return lista2
lista2 = muokkaa(lista)
print(lista)
print(lista2)
print(muokkaa(lista))


