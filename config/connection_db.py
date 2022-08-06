import mysql.connector

class ConnectionDB:

    def __init__(self):
        pass

    def conn(self):
        db = mysql.connector.connect(
            host="db-artificialis.cij039qweohb.us-east-1.rds.amazonaws.com",
            user="admin",
            password="12345678",
            database="artificialisDB"
        )
        cursor = db.cursor()
        return db, cursor