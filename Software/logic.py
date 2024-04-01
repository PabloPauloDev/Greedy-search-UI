from database import connections

class Logic:

    def __init__(self):
        con_string = 'DRIVER={SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=GreedySearch;Trusted_Connection=yes;'
        self.banco = connections(con_string)
        self.visited = []

    def busca(self, atual, objetivo):
        print(atual)
        self.visited.append(atual)
        data = self.banco.connections(atual)  # Usar self.banco para acessar o atributo na instância
        
        for i in range(len(data)):
            for j in range(2):
                if data[i][j] != atual:
                    self.visited.append(data[i][j])
        if objetivo in self.visited:
            print('Encontrado')
            self.visited.clear()
        else:
            for i in range(len(data)):
                if i == 0:
                    reg = data[i][2]
                    prox = data[i][i]
                else:
                    if reg > data[i][2]:
                        reg = data[i][2]
                        prox = data[i][0]
            self.busca(prox, objetivo)  # Chamar recursivamente usando self.busca()
