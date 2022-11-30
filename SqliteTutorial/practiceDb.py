from mysql import connector

dataBase = connector.connect(
    user="root",
    password="Mysql0011@",
    host="127.0.0.1",
    database="college",
    # auth_plugin='mysql_native_password',
)

cursor = dataBase.cursor()
cursor.execute('DESC student;')

for value in cursor.fetchall():
    print(value)


cursor.close()
dataBase.close()
