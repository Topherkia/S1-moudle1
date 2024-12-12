import mysql.connector
from mysql.connector import connection


def get_airport_data(area_code):
    sql = f"SELECT name, type FROM airports WHERE iso_country = '{area_code}' ORDER BY type"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[0]} is of the type {row[1]}.")


connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='airport_db',
        user='dbuser',
        password='password',
        autocommit=True,
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
    )

area_code = input("Enter the country area code: ")
get_airport_data(area_code)