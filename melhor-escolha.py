from grafo_romenia import RomeniaPonderado

def busca_custo_uniforme(grafo, inicio, meta):
    
    fronteira = [[inicio, 0, [inicio]]]
    visitados = {}

    while fronteira:
        # Encontra o índice do elemento com o menor custo
        menor_custo_index = 0
        for i in range(len(fronteira)):
            if fronteira[i][1] < fronteira[menor_custo_index][1]:
                menor_custo_index = i

        # Remove o elemento com o menor custo da fronteira
        no_atual, custo_atual, caminho = fronteira[menor_custo_index]
        fronteira.pop(menor_custo_index)

        if no_atual == meta:
            return caminho, custo_atual

        visitados[no_atual] = custo_atual

        # Itera sobre os vizinhos do nó atual
        for vizinho, dados in grafo.G[no_atual].items():
            novo_custo = custo_atual + dados['weight']
            if vizinho not in visitados or novo_custo < visitados[vizinho]:
                novo_caminho = caminho + [vizinho]
                fronteira.append([vizinho, novo_custo, novo_caminho])

    return None, float('inf')

# Como usar
if __name__ == "__main__":
    romenia = RomeniaPonderado()

    caminho, custo = busca_custo_uniforme(romenia, "Arad", "Bucharest")

    if caminho:
        print("Caminho encontrado:")
        for cidade in caminho:
            print(cidade)
        print(f"Custo total: {custo} km")
    else:
        print("Nenhum caminho encontrado")
