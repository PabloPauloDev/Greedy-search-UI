from database import connections

class Logic:

    def __init__(self):
        con_string = 'DRIVER={SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=GreedySearch;Trusted_Connection=yes;'
        self.banco = connections(con_string)
        self.visited = []
        self.prox = ''
        self.texto = ''

    def busca(self, atual, objetivo):

        self.texto += atual + '\n'
        data = self.banco.connections(atual)
        data = sorted(data, key=lambda data:int(data[1]))

        self.visited.append(atual)
        self.prox = ''

        for i in range(len(data)):
            for j in range(len(data[i])):
                if objetivo == atual:
                    self.texto += 'Voce ja esta no seu destino'
                    return
                if data[i][j] == objetivo:
                    for value in data:
                        self.texto += str(value) + "\n"
                    self.texto += '-------------------------\n'
                    self.texto += "encontrado"
                    return
                
        for i in range(len(data)):
            if data[i][0] not in self.visited:
                for value in data:
                    self.texto += str(value) + "\n"
                self.texto += '-------------------------\n'
                self.prox = data[i][0]
                return self.busca(self.prox, objetivo)
        self.texto += "não encontrado"
