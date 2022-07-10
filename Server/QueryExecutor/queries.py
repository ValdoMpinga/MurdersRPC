import pandas as pd
import psycopg2
from psycopg2 import Error


class QueriesExecutor:
    def listNumberOfSolvedMurderers(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="0",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="xqueryTest")

            cursor = connection.cursor()

            query = pd.read_sql(
                """SELECT xpath('count(//crimeSolved[text()="Yes"])',"xmlFile") from "XMLFILES" where "fileName" ='p'; """,
                connection)
            print(query)
            stringifiedQuery = str(query)
            return stringifiedQuery
        except (Exception, Error) as error:
            print("Error: ", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()

    def listMurdersBetweenAges(self, firstAge, secoundAge):

        try:
            connection = psycopg2.connect(user="postgres",
                                          password="0",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="xqueryTest")

            cursor = connection.cursor()

            query = pd.read_sql(
                """SELECT xpath('count(//victimAge[text()>%s and text()<%s])',"xmlFile") from "XMLFILES"  where "fileName" ='p'; """ % (
                    firstAge, secoundAge),
                connection)
            print(query)
            stringifiedQuery = str(query)
            return stringifiedQuery
        except (Exception, Error) as error:
            return error
            print("Error: ", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def listMurderersThroughSexAndRace(self, sex, race):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="0",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="xqueryTest")
            cursor = connection.cursor()

            query = pd.read_sql(
                """SELECT xpath('//VictimData[./victimSex="%s" and victimRace="%s"]',"xmlFile") from "XMLFILES"  where "fileName" ='p'; """ % (
                    sex, race),
                connection)
            stringifiedQuery = str(query)
            return stringifiedQuery

        except (Exception, Error) as error:
            print("Erro: ", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()

    def listCrimeThroughMonths(self, month, year):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="0",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="xqueryTest")
            cursor = connection.cursor()

            query = pd.read_sql(
                """SELECT xpath('//crimeOccurence[./month = "%s" and year="%s"]',"xmlFile") from "XMLFILES" where "fileName" ='p'; """ % (
                    month, year),
                connection)

            stringifiedQuery = str(query)
            return stringifiedQuery
        except (Exception, Error) as error:
            print("Erro: ", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def listCrimesThroughGuns(self, gun):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="0",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="xqueryTest")
            cursor = connection.cursor()

            query = pd.read_sql(
                """SELECT xpath('//perpetratorData[./weapon="%s"]',"xmlFile") from "XMLFILES" where "fileName" ='p'; """ % (
                    gun),
                connection)

            stringifiedQuery = str(query)
            return stringifiedQuery
        except (Exception, Error) as error:
            print("Erro: L", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def sendParsedXMLToDB(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="0",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="xqueryTest")
            cursor = connection.cursor()

            with open('C:\\Users\\Valdo\\Desktop\\School\\3rd_Year\\Semestre_I\\IS\\TrabalhosPraticos\\Server\\CsvToXml\\murders.xml', 'r') as file:
                productionFile = file.read()

            cursor.execute("""INSERT INTO public."XMLFILES"("xmlFile","importDate","fileName")values('%s','%s','%s');""" % (productionFile,'2021-11-27','productionFile'))
            connection.commit()

            return 'ficheiro inserido com sucesso!'
        except (Exception, Error) as error:
            print("Erro: ", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def softDeleteInsert(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="0",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="xqueryTest")
            cursor = connection.cursor()
            #
            # query ="""INSERT INTO "XMLFILES" (xmlFile,importDate,fileName) VALUES (%s,%s,%s)"""
            # insertData=('<lorem>ipsum</lorem>','2020-02-02','fileToDelete')
            # cursor.execute(query,insertData)

            cursor.execute(
                """ INSERT INTO public."XMLFILES"("xmlFile","importDate","fileName") values ('%s','%s','%s');""" %
                ("crime", "2021-11-27","fileToDelete",)
            )
            connection.commit()

            return "ficheiro inserido com sucesso!!!"

        except (Exception, Error) as error:
            print("Erro: ", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def softDeleteDelete(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="0",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="xqueryTest")
            cursor = connection.cursor()

            cursor.execute("""DELETE FROM public."XMLFILES" WHERE "fileName"='fileToDelete';""")

            connection.commit()

            return "ficheiro apaagdo com sucesso!!!"

        except (Exception, Error) as error:
            print("Erro: ", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def deletedDataSelect(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="0",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="xqueryTest")
            cursor = connection.cursor()
            query = pd.read_sql(
                """SELECT *FROM "DeletedByUser" where "importDate"='2021-11-27'""",
                connection)

            stringifiedQuery = str(query)

            print(stringifiedQuery)
            return stringifiedQuery

        except (Exception, Error) as error:
            print("Erro: ", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
