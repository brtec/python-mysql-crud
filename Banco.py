#importa biblioteca
import pymysql

class Banco:

    def __init__(self):
        self.connection = pymysql.connect(
                            host='',
                            user='',
                            password='',                             
                            db='',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor
                             )
        
    def select(self, sql):
        self.cursor = self.connection.cursor()   
        retorno = []
        try:
            self.cursor.execute(sql)
            retorno = self.cursor.fetchall()
            return(retorno);
               
        finally:
            # fecha conexao.
            self.connection.close()
    
    def delete(self, sql):
        self.cursor = self.connection.cursor()   
        retorno = []
        try:
            self.cursor.execute(sql)
            retorno = self.cursor.fetchall()
            return(retorno);
               
        finally:
            # fecha conexao.
            self.connection.close()
        
        
    def fecha(self, fecha):
        self.connection.close()
        
        