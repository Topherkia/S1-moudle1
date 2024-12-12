import mysql.connector
from mysql.connector import connection
import geopy
from geopy import distance


def get_airport_data(icao_code):
    sql = f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{icao_code}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            coords = (row[0], row[1])

    return coords


connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='course_db',
        user='user',
        password='pass',
        autocommit=True,
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
    )

icao_code = input("Enter First ICAO code: ")
coords1 = get_airport_data(icao_code)
icao_code = input("Enter Second ICAO code: ")
coords2 = get_airport_data(icao_code)

distance = (geopy.distance.geodesic(coords1, coords2).km)

print(f"The distance between the airports is {distance.__round__()} kilometers.")