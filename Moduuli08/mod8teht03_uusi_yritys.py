"""
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin
koordinaatteihin. Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie asennus loppuun.
"""
import mysql.connector
import math

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

def distance(lat1, lon1, lat2, lon2):
    r = 6371  # Radius of the Earth in kilometers

        # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    matka = r * c
    return matka

while True:
    ICAO1, ICAO2 = input("Anna 1. kentän ICAO: "), input("Anna 2. kentän ICAO: ")
    cordinates = search_ICAO(ICAO1, ICAO2)
    distance(cordinates[0], cordinates[1], cordinates[2], cordinates[3])
    print(distance(cordinates[0], cordinates[1], cordinates[2], cordinates[3]))
    etäisyys = distance(cordinates[0], cordinates[1], cordinates[2], cordinates[3])
    print(f"Lentokenttien etäisyys on: {etäisyys:4.2f} km")