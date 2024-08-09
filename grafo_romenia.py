import matplotlib.pyplot as plt
import networkx as nx


class RomeniaPonderado:
    def __init__(self):
        # Criar um grafo
        self.G = nx.Graph()

        # Adicionar as arestas com pesos (distâncias)
        edges = [
            ("Arad", "Zerind", 75),
            ("Arad", "Sibiu", 140),
            ("Arad", "Timisoara", 118),
            ("Zerind", "Oradea", 71),
            ("Oradea", "Sibiu", 151),
            ("Timisoara", "Lugoj", 111),
            ("Lugoj", "Mehadia", 70),
            ("Mehadia", "Drobeta", 75),
            ("Drobeta", "Craiova", 120),
            ("Sibiu", "Fagaras", 99),
            ("Sibiu", "Rimnicu Vilcea", 80),
            ("Rimnicu Vilcea", "Pitesti", 97),
            ("Rimnicu Vilcea", "Craiova", 146),
            ("Craiova", "Pitesti", 138),
            ("Fagaras", "Bucharest", 211),
            ("Pitesti", "Bucharest", 101),
            ("Giurgiu", "Bucharest", 90),
            ("Bucharest", "Urziceni", 85),
            ("Urziceni", "Hirsova", 98),
            ("Urziceni", "Vaslui", 142),
            ("Vaslui", "Iasi", 92),
            ("Iasi", "Neamt", 87),
            ("Hirsova", "Eforie", 86)
        ]

        # Adicionar as arestas ao grafo
        for edge in edges:
            self.G.add_edge(edge[0], edge[1], weight=edge[2])

    def imprimir(self):
        # Imprimir o grafo com as distâncias
        for u, v, weight in self.G.edges(data=True):
            print(f"De {u} para {v} com distância {weight['weight']} km")

    def plotar(self):
        # Desenhar o grafo
        pos = nx.spring_layout(self.G)  # Gera uma disposição dos nós
        nx.draw(self.G, pos, with_labels=True, node_color='lightblue', edge_color='#909090', node_size=500, font_size=8,
                font_weight='bold')

        # Adicionar rótulos de peso às arestas
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)

        plt.title("Mapa de Cidades da Romênia com Distâncias")
        plt.show()
