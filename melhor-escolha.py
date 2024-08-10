from grafo_romenia import RomeniaPonderado

def busca_custo_uniforme(grafo, inicio, meta):
    fronteira = [[inicio, 0, [inicio]]]
    visitados = {}

    while len(fronteira) > 0:
        menor_custo_index = 0
        for i in range(len(fronteira)):
            if fronteira[i][1] < fronteira[menor_custo_index][1]:
                menor_custo_index = i

        no_atual, custo_atual, caminho = fronteira[menor_custo_index]
        fronteira.pop(menor_custo_index)

        if no_atual == meta:
            return caminho, custo_atual

        visitados[no_atual] = custo_atual

        # Itera sobre os vizinhos do nó atual
        for vizinho in grafo.G[no_atual]:
            novo_custo = custo_atual + grafo.G[no_atual][vizinho]['weight']
            if vizinho not in visitados or novo_custo < visitados[vizinho]:
                # Adiciona o vizinho à fronteira com o novo custo e o caminho atualizado
                novo_caminho = caminho + [vizinho]
                fronteira.append([vizinho, novo_custo, novo_caminho])

    return None, float('inf')  


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