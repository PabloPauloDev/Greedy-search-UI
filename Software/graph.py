import networkx as nx
import matplotlib.pyplot as plt

class graph:

    def gerar_grafo(self):
        # Criando um grafo direcionado
        G = nx.DiGraph()

        # Adicionando arestas com os pesos
        edges = [
            (1, "Arad", "Zerind", 75),
            (2, "Arad", "Sibiu", 140),
            (3, "Arad", "Timisoara", 118),
            (4, "Zerind", "Oradea", 71),
            (5, "Oradea", "Sibiu", 151),
            (6, "Sibiu", "Fagaras", 99),
            (7, "Sibiu", "Rimnicu", 80),
            (8, "Timisoara", "Lugoj", 111),
            (9, "Lugoj", "Mehadia", 70),
            (10, "Mehadia", "Dobreta", 75),
            (11, "Dobreta", "Craiova", 120),
            (12, "Craiova", "Pitesti", 138),
            (13, "Craiova", "Rimnicu", 146),
            (14, "Rimnicu", "Pitesti", 97),
            (15, "Fagaras", "Bucharest", 211),
            (16, "Pitesti", "Bucharest", 101),
            (17, "Bucharest", "Giurgiu", 90)
        ]

        for edge_id, source, target, weight in edges:
            G.add_edge(source, target, weight=weight)
        
        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels=True, arrows=True, arrowstyle='-')
        plt.title("Explorador de rota")
        plt.show()
