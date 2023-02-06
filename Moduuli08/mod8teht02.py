"""
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien
lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että
pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
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

def get_airports(input):
    small = 0
    medium = 0
    large = 0
    heli = 0
    closed = 0


    query = f"select airport.type from airport where iso_country = '{input}'"
    cursor = connection.cursor()
    cursor.execute(query)
    total = cursor.fetchall()
    #result = cursor.fetchone()  #fetchall tuo kaikki monikkona... [] on lista ja () on dictionary tai setti
    if cursor.rowcount > 0:
       for row in total:
           if "small_airport" == row[0]:
               small += 1
           elif "medium_airport" == row[0]:
               medium += 1
           elif "large_airport" == row[0]:
               large += 1
           elif "heliport" == row[0]:
               heli += 1
           else:
                closed += 1
       print(f"Lentokenttien kokonaismäärä: {small+medium+large+heli+closed}"
            f"\nIsoja kenttiä: {large}, keskikokoisia: {medium}, pieniä: {small}, "
            f"kopterikenttiä: {heli} ja kiinni olevia: {closed}.")

while True:
    get_airports(input("Anna maakoodi: "))





#kenttien määrän voi laittaa jo sql koodissa count-funktiolla tai sitte tuoda kaikki ja python koodissa vasta laskea ne

"""
#esimerkkikoodia SQL:ssä mitä käyttää
select name, type from airport where iso_country='fi';
select count(name) from airport where iso_country='fi' and type='small'
select count(), name from airport where iso_country='fi' and type='small'
count ja group by komennot SQL:ssä
"""