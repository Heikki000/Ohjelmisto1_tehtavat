#ladataan tarvittava moduuli
import mysql.connector

#Funktio hakee ja tulostaa pelaajan nimen ja paikan
#Funktio tarvitsee parametrina pelaajan nimen.
#Funktio ei palauta mitään.
def pelaajan_paikka(nimi):
    sql = "SELECT screen_name, location " + \
          "FROM game" +\
          "WHERE screen_name = '" + nimi + "'"

    print(sql)  # tulostetaan lopullinen sql-lause
    kursori = yhteys.cursor()  # kursorin avulla välitetään tietoa python-koodin
    # tietokannan välillä
    kursori.execute(sql)  # suoritetaan sql-lause
    tulos = kursori.fetchall()  # haetaan haun tulos ja sijoitetaan se muuttujaan tulos
    if kursori.rowcount >= 1:  # saatiinko dataa?
        for rivi in tulos:
            print(f"Nimi: {rivi[0]} on paikassa: {rivi[1]}")
    return


#Funktio hakee ja tulostaa kaikkien pelaajien nimet ja paikat.
#Funktio ei tarvitse parametreja eikä palauta mitään.
#Funktio käyttää pääohjelmassa luotua tietokantayhteyttä.
def tulosta_pelaajat():
    sql = "SELECT screen_name, location " +\
        "FROM game"
    print(sql)                  #tulostetaan lopullinen sql-lause
    kursori = yhteys.cursor()   #kursorin avulla välitetään tietoa python-koodin
                                #tietokannan välillä
    kursori.execute(sql)        #suoritetaan sql-lause
    tulos = kursori.fetchall()  #haetaan haun tulos ja sijoitetaan se muuttujaan tulos
    if kursori.rowcount >= 1:   #saatiinko dataa?
        for rivi in tulos:
            print(f"Nimi: {rivi[0]} on paikassa: {rivi[1]}")
    return



#pääohjelma alkaa
#muodostetaan yhteys tietokantaan
yhteys = mysql.connector.connect(
         host='127.0.0.1', # on sama asia kuin localhost
         port= 3306,    #tietyille asioille on omat porttinsa, esim. näppäimistö, internet
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True    #muutokset tietokantaan tehdään heti
         )
#kutsutaan funktiota, joka tulostaa pelaajien nimet ja paikat
tulosta_pelaajat()

#funktio tulostaa halutun pelaajan paikan
pelaaja = input("Anna pelaajan nimi: ")
pelaajan_paikka(pelaaja)
#suljetaan yhteys
yhteys.close()

