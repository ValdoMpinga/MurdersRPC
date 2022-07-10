import psycopg2
from psycopg2 import Error
from psycopg2._psycopg import cursor


class ConnectionHandler:


    def connectionCreator(self, user, password, host, port, dataBase):
        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          dataBase=self.dataBase)
            print(connection)
            return connection
        except (Exception, Error) as error:
            print("Ocorreu alguns erros: ", error)
