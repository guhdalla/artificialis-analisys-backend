from asyncio.log import logger
from config.connection_db import ConnectionDB
from logging import getLogger

logger = getLogger()

class ComandosSql():

    def __init__(self):
        self.db, self.cursor = ConnectionDB().conn()

    def listar(self, query, obj):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            ls_obj = []
            for row in result:
                ls_obj.append(obj.builder(row).json())
            return ls_obj
        except Exception as e:
            logger.error(e)
            return e
    
    def consultar(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result[0]
        except Exception as e:
            logger.error(e)
            return e

    def salvar(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.db.commit()
        except Exception as e:
            logger.error(e)
            return e

    def salvar_varios(self, query, params):
        try:
            self.cursor.executemany(query, params)
            self.db.commit()
        except Exception as e:
            logger.error(e)
            return e