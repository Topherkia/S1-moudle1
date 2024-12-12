from multiprocessing import connection
import mysql.connector

connect_it = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='101188',
    charset='utf8mb4',
    collation='utf8mb4_general_ci',
    autocommit=True
)

def get_airport_by_ident(icao):
    sql = f"Select airport.name, airport.municipality from airport where ident = {icao}"
    cursor = connect_it.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return (result)
    # print(result)
    # print(result['name'], result['municipality'])

code = input('Type ICAO code: ')
airport = get_airport_by_ident(code)
if airport is not None:
    print(f'{airport} is located')
    # print(f'{airport["name"]} is located in {airport["municipality"]} in {airport["iso_country"]}')
else:
    print('airport not found')

connect_it.close()