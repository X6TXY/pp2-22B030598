import psycopg2
from config import host, user, password, db_name

from config import data
import psycopg2

sql_select_all_records = '''
    SELECT * FROM phone_book;
'''

sql_select_record_by_id = '''
    SELECT * FROM phone_book WHERE phone_id = %s;
'''

sql_select_record_by_name = '''
    SELECT * FROM phone_book WHERE user_name = %s;
'''

db = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
cursor = db.cursor()

command = input("What kind of query do you want to execute?[all/id/name]:")
if command == 'all':
    cursor.execute(sql_select_all_records)
    print(cursor.fetchall())
elif command == 'id':
    id = input("Input id of the record:")
    cursor.execute(sql_select_record_by_id, (id,))
    print(cursor.fetchone())
elif command == 'name':
    name = input("Input the user name of the record:")
    cursor.execute(sql_select_record_by_name, (name,))
    print(cursor.fetchall())
else:
    print("There is no such command")

cursor.close()
db.close()