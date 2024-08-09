import heapq
from grafo_romenia import RomeniaPonderado

def busca_melhor_escolha(grafo, inicio, meta, funcao_avaliacao):
    fronteira = []
    heapq.heappush(fronteira, (funcao_avaliacao(inicio), 0, inicio, []))
    visitados = {}

    while fronteira:
        f_valor, custo_atual, nó_atual, caminho = heapq.heappop(fronteira)
        caminho = caminho + [nó_atual]

        if nó_atual == meta:
            return caminho, custo_atual

        if nó_atual in visitados and visitados[nó_atual] <= custo_atual:
            continue

        visitados[nó_atual] = custo_atual

        for vizinho, dados in grafo.G[nó_atual].items():
            custo = dados['weight']
            novo_custo = custo_atual + custo
            heapq.heappush(fronteira, (funcao_avaliacao(vizinho) + novo_custo, novo_custo, vizinho, caminho))

    return None, float('inf')  # Retorna None se não encontrar caminho

# Exemplo de uso
if __name__ == "__main__":
    romenia = RomeniaPonderado()
    romenia.imprimir()

    # Função de avaliação simples (busca de custo uniforme)
    funcao_avaliacao = lambda no: 0  # ou uma função heurística para A*

    # Realizar a busca
    caminho, custo = busca_melhor_escolha(romenia, "Arad", "Bucharest", funcao_avaliacao)

    if caminho:
        print(f"Caminho encontrado: {' -> '.join(caminho)} com custo total de {custo} km")
    else:
        print("Nenhum caminho encontrado")

    # Plotar o grafo
    romenia.plotar()
