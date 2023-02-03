"""
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä
lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
"""
import mysql.connector



def connect_db():
    return mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True
         )
connect = connect_db()
#print connect

def get_airport():
    query = "select name, sumicipality from airport where ident ='efhk'"
    cursor = connection.cursor()
    cursor.execute(query)