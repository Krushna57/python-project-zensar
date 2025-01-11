import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "port": 3307, 
    "user": "root",
    "password": "root",
    "database": "customer_feedback"
}

class Connection:
    @staticmethod
    def get_db_connection():

        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            if connection.is_connected():
                print("Status : OK")
            return connection
        except Error as e:
            print(f"Error while connecting to the database: {e}")
            return None
