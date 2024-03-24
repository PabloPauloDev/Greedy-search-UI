import pyodbc


class connections:
    def __init__(self, conString):
        self.cnxn = pyodbc.connect(conString)
    def connections(self, city):
        cursor = self.cnxn.cursor()
        cursor.execute('SELECT cidade, cidadeSec, distancia FROM conexões WHERE cidade = ? OR cidadeSec = ?', (city, city))
        results = cursor.fetchall()
        return results


