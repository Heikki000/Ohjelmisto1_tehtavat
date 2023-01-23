

lukuStr = input("Anna kokonaisluku, tyhjä lopettaa:")

#ekaluku on alkuarvo suurimmallle ja pienimmälle (jos se ei ole tyhjä)
if lukuStr != "":
        pienin = suurin = int(lukuStr)

while lukuStr != "":

    luku = int(lukuStr)

    if luku > suurin:
        suurin = luku

    lukuStr = input("Anna kokonaisluku, tyhjä lopettaa: ")

# muilla ohjelmointikielilllä taulukko = array list, pythonissa se on "lista""!
# pythonin lista on paljon joustavampi kuin esim javan ja muiden:
# kun poistaa solun niin muut siirtyvät ja "täyttävät" solun.

nimet = []
...
indeksit 0,  1,   2,   3       !!!!!
        [A]-[Cc]-[B]-[Vika]
nimet viittaa koko tuohon listaan (alkio tai solu: A on 1. ja Vika on 4.)

vikaNimi = nimet[3]
nimet[2] = "Uusi"   tarkoittaa: [B] --->  [Uusi]