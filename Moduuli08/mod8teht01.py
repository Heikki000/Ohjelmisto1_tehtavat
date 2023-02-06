"""
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä
lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
"""
import mysql.connector

def connect_db():
    return mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True
         )
connection = connect_db()
#print connect
icao = input("Anna haettavan kentän ICAO: ")

def get_airport(icao):
    query = f"select name, municipality from airport where ident ='{icao}'"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()  #fetchall tuo kaikki monikkona... [] on lista ja () on dictionary tai setti
    if cursor.rowcount > 0:
        return f"Kentän nimi: {result[0]}, paikkakunta: {result[1]}"
    else:
        return "Ei tuloksia."

result = get_airport(icao)
print(result)
