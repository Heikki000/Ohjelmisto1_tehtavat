"""
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin
koordinaatteihin. Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie asennus loppuun.
"""
import mysql.connector
import geopy

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True
)


def search_ICAO(input1, input2):
    sql_command = "select airport.latitude_deg, airport.longitude_deg from airport where ident = '" + input1 + "' or ident = '" + input2 + "'"
    airport = ()
    cursor = yhteys.cursor()
    cursor.execute(sql_command)
    total = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in total:
            airport += row[0], row[1]
    return airport



while True:
    ICAO1, ICAO2 = input("Anna 1. kentän ICAO: "), input("Anna 2. kentän ICAO: ")
    cordinates = search_ICAO(ICAO1, ICAO2)
    place1 = cordinates[0], cordinates[1]
    place2 = cordinates[2], cordinates[3]
    print(f"Lentokenttien etäisyys on: {geopy.distance(place1,place2):1.2f}km")