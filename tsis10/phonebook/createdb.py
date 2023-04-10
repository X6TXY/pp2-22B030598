import psycopg2
from config import host, user, password, db_name
import csv

try:
    #connection to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    #the cursor for performing database operetions
    cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE phonebook(
            phone_id SERIAL PRIMARY KEY,
            user_name varchar(32) ,
            phone_number varchar(32) );"""
        )


except Exception as _ex:
    print("Error while working with PostgreSQL")
    
finally:
    if connection:
        connection.close()
        print("PostgreSQL connection closed")
    