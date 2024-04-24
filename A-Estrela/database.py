import pandas as pd

class Connections:
    def __init__(self, directory):
        self.directory = directory

    def get_connections(self, cidade):
        results = pd.read_csv(self.directory, header=0, sep=",")
        results = results[results['cidade1'] == cidade]
        results = results.sort_values(by='distancia')
        return results

objeto_conexoes = Connections("Database\Database.csv")

print(objeto_conexoes.get_connections("Arad"))
