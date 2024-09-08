from grafo_romenia import RomeniaPonderado

def busca_custo_uniforme(grafo, inicio, meta):
    
    fronteira = [[inicio, 0, [inicio]]]
    visitados = {}
    interacoes = 0

    while fronteira:
        interacoes += 1
        
        menor_custo_index = 0
        for i in range(len(fronteira)):
            if fronteira[i][1] < fronteira[menor_custo_index][1]:
                menor_custo_index = i

        
        no_atual, custo_atual, caminho = fronteira[menor_custo_index]
        fronteira.pop(menor_custo_index)

        if no_atual == meta:
            return caminho, custo_atual, interacoes  

        visitados[no_atual] = custo_atual

        
        for vizinho, dados in grafo.G[no_atual].items():
            novo_custo = custo_atual + dados['weight']
            if vizinho not in visitados or novo_custo < visitados[vizinho]:
                novo_caminho = caminho + [vizinho]
                fronteira.append([vizinho, novo_custo, novo_caminho])

    return None, float('inf'), interacoes  

# Como usar
if __name__ == "__main__":
    romenia = RomeniaPonderado()

    caminho, custo, interacoes = busca_custo_uniforme(romenia, "Arad", "Bucharest")

    if caminho:
        print("Caminho encontrado:")
        for cidade in caminho:
            print(cidade)
        print(f"Custo total: {custo} km")
        print(f"Interações necessárias: {interacoes}")  
    else:
        print("Nenhum caminho encontrado")
        print(f"Interações realizadas: {interacoes}")
