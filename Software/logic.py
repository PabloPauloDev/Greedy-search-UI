from database import connections

class logic:

    def __init__(self):
        con_string = 'DRIVER={SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=GreedySearch;Trusted_Connection=yes;'
        self.banco = connections(con_string)

    def busca(self, atual, objetivo):
        data = self.banco.connections(atual)  # Usar self.banco para acessar o atributo na instância
        visited = []
        
        for i in range(len(data)):
            for j in range(2):
                if data[i][j] != atual:
                    visited.append(data[i][j])
        if objetivo in visited:
            print('Encontrado')
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

class testando:
# Instanciar a classe logic
    Teste = logic()
# Chamar o método busca
    Teste.busca('Sibiu', 'Oradea')
