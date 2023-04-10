from config import host, user, password, db_name
import psycopg2

sql_delete_by_phone = '''
    DELETE FROM phone_book WHERE phone_number = %s;
'''

sql_delete_by_name = '''
    DELETE FROM phone_book WHERE user_name = %s;
'''

db = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
cursor = db.cursor()

command = input("By what value you want to delete the record?[phone/name]:")
if command == 'phone':
    phone_number = input("Input the phone number of the record to delete:")
    cursor.execute(sql_delete_by_name, (phone_number,))
elif command == 'name':
    name = input("Input the name of the record to delete:")
    cursor.execute(sql_delete_by_name, (name,))
else:
    print("There is no such command")

cursor.close()
db.commit()
db.close()