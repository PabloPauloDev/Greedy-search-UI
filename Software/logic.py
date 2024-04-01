from database import connections

class Logic:

    def __init__(self):
        con_string = 'DRIVER={SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=GreedySearch;Trusted_Connection=yes;'
        self.banco = connections(con_string)
        self.visited = []
        self.prox = ''

    def busca(self, atual, objetivo):

        print(atual)
        data = self.banco.connections(atual)
        data = sorted(data, key=lambda data:int(data[1]))

        self.visited.append(atual)
        self.prox = ''

        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == objetivo:
                    print(data)
                    return print("encontrado")
                if data[i][0] not in self.visited:
                    print(data)
                    self.prox = data[i][0]
                    return self.busca(self.prox, objetivo)
        return print("não encontrado")
            

        print(data)
class teste:
    testando = Logic()
    testando.busca("Craiova", "Giurgiu")