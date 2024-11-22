# O mapa metroviário escolhido foi a linha 1 azul do metrô, partindo do Tucuruvi, as 10 estações escolhidas são as seguintes:
# Tucuruvi: 0, Parada Inglesa: 1, Jardim São Paulo: 2, Santana: 3, Carandiru: 4, Portuguesa–Tietê: 5, Armênia: 6, Tiradentes: 7, Luz: 8 e São Bento: 9
# Elas são interligadas continuamente, como mostra na matriz abaixo:

linha_azul = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Tucuruvi
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # Parada Inglesa
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Jardim São Paulo
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],  # Santana
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # Carandiru
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],  # Portuguesa–Tietê
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # Armênia
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],  # Tiradentes
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # Luz
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # São Bento
]

# Simule o algoritmo de cálculo de distâncias visto em sala, a partir de um dos vértices, e mostre uma lista 
# correspondente, contendo todos os vértices visitados, e a ordem de visitação (20 pontos)

# Para realizar essa calculo, vou utilizar o alcançáveis v3 visto em sala de aula:
# Matriz de adjacências para as 10 primeiras estações da Linha Azul do Metrô de São Paulo

def cria_fila_nova():
    return {"proximo": 0, "lista": []}

def insere_na_fila(fila, elemento):
    fila["lista"].append(elemento)

def remove_da_fila(fila):
    posicao = fila["proximo"]
    elemento = fila["lista"][posicao]
    fila["proximo"] += 1
    return elemento

def verifica_fila_vazia(fila):
    return fila["proximo"] >= len(fila["lista"])

def alcancaveis(arestas, V):
    num_vertices = len(arestas)
    fila = cria_fila_nova()
    distancias = {V: 0}
    insere_na_fila(fila, V)
    
    passo = 1  # Contador de passos para exibição
    print(f"Passo {passo}:")
    print(f"Vértice inicial: {V}")
    print(f"Fila: {fila['lista']}")
    print(f"Distâncias: {distancias}")
    print("-" * 40)
    
    while not verifica_fila_vazia(fila):
        vertice = remove_da_fila(fila)
        passo += 1
        print(f"Passo {passo}:")
        print(f"Processando vértice: {vertice}")
        print(f"Fila antes de processar: {fila['lista'][fila['proximo']:]}")
        
        for j in range(num_vertices):
            if arestas[vertice][j] == 1 and j not in distancias:
                distancias[j] = distancias[vertice] + 1
                insere_na_fila(fila, j)
                print(f"  Encontrou vértice {j}, distância atualizada para {distancias[j]}")
        
        print(f"Fila após processar: {fila['lista'][fila['proximo']:]}")
        print(f"Distâncias: {distancias}")
        print("-" * 40)
    
    return distancias


resultado = alcancaveis(linha_azul, 0)  # Partindo de Tucuruvi (índice 0)
print("Distâncias calculadas:", resultado)


