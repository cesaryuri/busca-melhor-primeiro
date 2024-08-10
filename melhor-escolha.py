from grafo_romenia import RomeniaPonderado

def busca_custo_uniforme(grafo, inicio, meta):
    fronteira = [(0, inicio, [])]  # Inicialmente, a fronteira tem apenas o ponto de partida com custo 0
    visitados = {}

    while fronteira:
        # Encontra o índice do elemento com o menor custo
        menor_custo_index = 0
        for i in range(len(fronteira)):
            if fronteira[i][0] < fronteira[menor_custo_index][0]:
                menor_custo_index = i

        # Remove o elemento com o menor custo da fronteira
        custo_atual, nó_atual, caminho = fronteira.pop(menor_custo_index)
        caminho = caminho + [nó_atual]

        if nó_atual == meta:
            return caminho, custo_atual

        if nó_atual in visitados and visitados[nó_atual] <= custo_atual:
            continue

        visitados[nó_atual] = custo_atual

        for vizinho, dados in grafo.G[nó_atual].items():
            custo = dados['weight']
            novo_custo = custo_atual + custo
            fronteira.append((novo_custo, vizinho, caminho))

    return None, float('inf')  # Retorna None se não encontrar caminho

# Exemplo de uso
if __name__ == "__main__":
    romenia = RomeniaPonderado()
    romenia.imprimir()

    # Realizar a busca
    caminho, custo = busca_custo_uniforme(romenia, "Arad", "Bucharest")

    if caminho:
        print(f"Caminho encontrado: {' -> '.join(caminho)} com custo total de {custo} km")
    else:
        print("Nenhum caminho encontrado")

    # Plotar o grafo
    romenia.plotar()
