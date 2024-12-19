# database.py (separate file for database connection)
import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='pharmacy_management'
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()