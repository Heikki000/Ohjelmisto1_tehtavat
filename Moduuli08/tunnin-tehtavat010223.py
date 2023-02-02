#ladataan tarvittava moduuli
import mysql.connector

#muodostetaan yhteys tietokantaan
yhteys = mysql.connector.connect(
         host='127.0.0.1', # on sama asia kuin localhost
         port= 3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True    #muutokset tietokantaan tehdään heti
         )

