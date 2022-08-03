import mysql.connector

class ConnectionDB:

    def __init__(self):
        pass

    def conn(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="artificialisDB"
        )
        cursor = db.cursor()
        return db, cursor