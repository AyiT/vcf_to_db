import psycopg2
import record
class Conn():
    def __init__(self, dbname, host, port, user, pwd):
        self.dbname = dbname
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd

    def connect(self):

        try:
            command = "dbname='"+self.dbname+"' user='"+self.user+"' host='"+self.host+"' port='"+self.port+"' password='"+self.pwd+"'"
            conn = psycopg2.connect(command)
            print('Connected')
            return conn
        except:
            print ("Connection not possible")
