import psycopg2
from config import host, user, password, db_name
import csv

sql = '''
    INSERT INTO phone_book VALUES(DEFAULT,%s, %s);
'''

db = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
cursor = db.cursor()

try:
    with open("input.csv", "r") as f:
        data = csv.reader(f, delimiter=',')
        for row in data:
            cursor.execute(sql, row)
except Exception as e:
    print("There is no such csv file, please input the values manually")
    name = input("Input the name:")
    phone = input("Input the names phone number:")
    cursor.execute(sql,(name,phone))

cursor.close()
db.commit()
db.close()