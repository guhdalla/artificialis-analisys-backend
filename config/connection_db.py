import mysql.connector
import os

class ConnectionDB:

    def __init__(self):
        pass

    def conn(self):
        db = mysql.connector.connect(
            host=os.environ.get("DB_HOST", None),
            user=os.environ.get("DB_USER" ,None),
            password=os.environ.get("DB_PASS", None),
            database=os.environ.get("DB_NAME", None)
        )
        cursor = db.cursor()
        return db, cursor