import mysql.connector
from mysql.connector import errorcode

configuration = {
    'user': 'root',
    'password': 'Mysql0011@',
    'host': '127.0.0.1',
    'database': 'MyEmployees'
}

# Establishing a new connection with MySql server
try:
    connection = mysql.connector.connect(**configuration)
    print("Database connection successful.")
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something wrong with your user name and password.")
    elif error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(error)

connection.close()
