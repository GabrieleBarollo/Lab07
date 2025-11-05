from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    def popolo_dd_museo(self):
        risultati = ["Nessun filtro"]
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query = """
        SELECT DISTINCT id_museo
        FROM artefatto
        """
        cursor.execute(query)
        for museo in cursor:
            risultati.append(museo[0])

        cursor.close()
        cnx.close()
        return risultati


    def popolo_dd_epoca(self):
        risultati = ["Nessun filtro"]
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query = """
                SELECT DISTINCT epoca
                FROM artefatto
                """
        cursor.execute(query)
        for epoca in cursor:
            risultati.append(epoca[0])

        cursor.close()
        cnx.close()
        return risultati

    def prima_query(self):
        risultati = []
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query = """
                SELECT *
                FROM artefatto
                """
        cursor.execute(query)
        for artefatto in cursor:
            obj = Artefatto(artefatto[0], artefatto[1], artefatto[2], artefatto[3], artefatto[4])
            risultati.append(obj)

        cursor.close()
        cnx.close()
        return risultati

    def seconda_query(self, m):
        risultati = []
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query = """
                SELECT *
                FROM artefatto
                Where id_museo = %s
                """
        cursor.execute(query, (m,))
        for artefatto in cursor:
            obj = Artefatto(artefatto[0], artefatto[1], artefatto[2], artefatto[3], artefatto[4])
            risultati.append(obj)

        cursor.close()
        cnx.close()
        return risultati

    def terza_query(self, m):
        risultati = []
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query = """
                        SELECT *
                        FROM artefatto
                        Where epoca = %s
                        """
        cursor.execute(query, (m,))
        for artefatto in cursor:
            obj = Artefatto(artefatto[0], artefatto[1], artefatto[2], artefatto[3], artefatto[4])
            risultati.append(obj)

        cursor.close()
        cnx.close()
        return risultati

    def quarta_query(self, m1, m2):
        risultati = []
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query = """
                        SELECT *
                        FROM artefatto
                        Where id_museo = %s AND epoca = %s
                        """
        cursor.execute(query, (m1,m2))
        for artefatto in cursor:
            obj = Artefatto(artefatto[0], artefatto[1], artefatto[2], artefatto[3], artefatto[4])
            risultati.append(obj)

        cursor.close()
        cnx.close()
        return risultati








