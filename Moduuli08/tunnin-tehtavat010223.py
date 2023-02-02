#ladataan tarvittava moduuli
import mysql.connector

#Funktio hakee ja tulostaa pelaajan nimen ja paikan
#Funktio tarvitsee parametrina pelaajan nimen.
#Funktio ei palauta mitään.
def pelaajan_paikka(nimi):
    print("Ei vielä ihan valmis")
    return

#Funktio hakee ja tulostaa kaikkien pelaajien nimet ja paikat.
#Funktio ei tarvitse parametreja eikä palauta mitään.
#Funktio käyttää pääohjelmassa luotua tietokantayhteyttä.
def tulosta_pelaajat():
    sql = "SELECT screen_name, location " +\
        "FROM game"
    print(sql)


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

#suljetaan yhteys
yhteys.close()

