import pyodbc


class connections:
    def __init__(self, con_string):
        self.cnxn = pyodbc.connect(con_string)
    def connections(self, city):
        cursor = self.cnxn.cursor()
        cursor.execute('SELECT cidade, cidadeSec, distancia FROM conexões WHERE cidade = ? OR cidadeSec = ?', (city, city))
        results = cursor.fetchall()
        return results


