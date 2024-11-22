# NIKOLAS RODRIGUES MOURA DOS SANTOS – RM 551566
# RODRIGO BRASILEIRO – RM 98952 
# THIAGO JARDIM DE OLIVEIRA – RM 551624

# {“pais”:”Brasil”, “população”: 200000000, “pib”: xxx, “porcentagem de energia eólica”: yyy, …}
# Todos os dados foram pegos dos sites desponibilizados na tarefa, mas vou comentá-los aqui
# Para a população: https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population
# Para o PIB eu peguei somente o conceito do FMI, aqui está: https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita
# Para energia eólica, solar e nuclear utilizei o mesmo que entregava o percentual de todas por país: https://en.wikipedia.org/wiki/List_of_countries_by_electricity_production

#paises = {"pais":"", "população":,
#         "pib":,"energia_eólicaTWH": , "energia_nuclearTWH":,"energia_solarTWH":}

from pprint import pprint
# Nas energias(eólica, solar e nuclear) coloquei TWH que significa Tera Wats hora ao final do nome da chave 
# Dicionário de países e dados
paises = {
    "Brasil": {"população": 203080756, "pib": 10296, "energia_eólicaTWH": 82, "energia_nuclearTWH": 15, "energia_solarTWH": 30}, #
    "França": {"população": 68534000, "pib": 48012, "energia_eólicaTWH": 39, "energia_nuclearTWH": 295, "energia_solarTWH": 20},
    "Portugal": {"população": 10639726, "pib": 29341, "energia_eólicaTWH": 13, "energia_nuclearTWH": 0, "energia_solarTWH": 4},
    "Espanha": {"população": 48946035, "pib": 35789, "energia_eólicaTWH": 62, "energia_nuclearTWH": 59, "energia_solarTWH": 36},
    "Estados Unidos": {"população": 335893238, "pib": 86601, "energia_eólicaTWH": 434, "energia_nuclearTWH": 772, "energia_solarTWH": 205},
    "Índia": {"população": 1404910000, "pib": 2698, "energia_eólicaTWH": 70, "energia_nuclearTWH": 46, "energia_solarTWH": 95},
    "Alemanha": {"população": 84708010, "pib": 55521, "energia_eólicaTWH": 125, "energia_nuclearTWH": 35, "energia_solarTWH": 61},
    "China": {"população": 1409670000, "pib": 12969, "energia_eólicaTWH": 2099, "energia_nuclearTWH": 2640, "energia_solarTWH": 1323},
    "Japão": {"população": 123790000, "pib": 32859, "energia_eólicaTWH": 8, "energia_nuclearTWH": 52, "energia_solarTWH": 102},
    "México": {"população": 129940228, "pib": 13972, "energia_eólicaTWH": 20, "energia_nuclearTWH": 11, "energia_solarTWH": 19},
    "Argentina": {"população": 47067441, "pib": 12814, "energia_eólicaTWH": 14, "energia_nuclearTWH": 7, "energia_solarTWH": 3},
    "Bélgica": {"população": 11846626, "pib": 56129, "energia_eólicaTWH": 12, "energia_nuclearTWH": 44, "energia_solarTWH": 7},
    "Suíça": {"população": 9002763, "pib": 106098, "energia_eólicaTWH": 0.2, "energia_nuclearTWH": 24, "energia_solarTWH": 3},
    "Itália": {"população": 58968499, "pib": 40287, "energia_eólicaTWH": 20, "energia_nuclearTWH": 0, "energia_solarTWH": 28},
    "Coreia do Sul": {"população": 51248233, "pib": 36132, "energia_eólicaTWH": 3, "energia_nuclearTWH": 176, "energia_solarTWH": 27},
    "Canadá": {"população": 41288599, "pib": 53834, "energia_eólicaTWH": 38, "energia_nuclearTWH": 87, "energia_solarTWH": 6},
    "Polônia": {"população": 37543000, "pib": 23563, "energia_eólicaTWH": 20, "energia_nuclearTWH": 0, "energia_solarTWH": 8},
    "África do Sul": {"população": 63015904, "pib": 6377, "energia_eólicaTWH": 10, "energia_nuclearTWH": 10, "energia_solarTWH": 10},
    "Chile": {"população": 20086377, "pib": 16365, "energia_eólicaTWH": 9, "energia_nuclearTWH": 0, "energia_solarTWH": 15},
    "Finlândia": {"população": 5628931, "pib": 54774, "energia_eólicaTWH": 12, "energia_nuclearTWH": 25, "energia_solarTWH": 0.01}
}

# Função de inserção naD árvore binária
def insere(arvore, chave, pais):
    if arvore == {}:
        arvore['raiz'] = chave
        arvore['pais'] = pais
        arvore['esquerda'] = {}
        arvore['direita'] = {}
        return

    if chave == arvore['raiz']:
        return  # se a raiz já existe, ela não é adicionada novamente 

    if chave < arvore['raiz']:
        if arvore['esquerda'] == {}:
            arvore['esquerda'] = {'raiz': chave, 'pais': pais, 'esquerda': {}, 'direita': {}}
        else:
            insere(arvore['esquerda'], chave, pais)

    elif chave > arvore['raiz']:
        if arvore['direita'] == {}:
            arvore['direita'] = {'raiz': chave, 'pais': pais, 'esquerda': {}, 'direita': {}}
        else:
            insere(arvore['direita'], chave, pais)

# Função para criar a árvore binária 
def criar_arvore(paises, criterio):
    arvore = {}
    for pais, dados in paises.items():
        chave = dados[criterio]
        insere(arvore, chave, pais)
    return arvore

# Função de busca na árvore binária
def busca(arvore, chave):
    if arvore == {}:
        return None  

    if chave == arvore['raiz']:
        return arvore['pais']  

    if chave < arvore['raiz']:
        return busca(arvore['esquerda'], chave)  

    else:  # chave > arvore['raiz']
        return busca(arvore['direita'], chave)  
    
# Criando árvores diferentes com base em parâmetros diferentes, usei de todas para ter mais abrangência  
arvore_por_pib = criar_arvore(paises, "pib") # envia como parâmetro dicionário escolhido e o o que deseja no dicinário
arvore_por_populacao = criar_arvore(paises, "população")
arvore_por_eolica = criar_arvore(paises, "energia_eólicaTWH")
arvore_por_solar = criar_arvore(paises, "energia_solarTWH")
arvore_por_nuclear = criar_arvore(paises, "energia_nuclearTWH")


#Exemplo de inserções em árvores já criadas
def inserir(arvore, chave, pais):
    insere(arvore, chave, pais)
    pprint(arvore)

novo_pais = "Noruega"
dados_noruega = {"população": 5421240, "pib": 75382, "energia_eólicaTWH": 20, "energia_nuclearTWH": 0, "energia_solarTWH": 0.5}

# Insere a nova entrada na árvore de energia eólica
inserir(arvore_por_eolica, dados_noruega["energia_eólicaTWH"], novo_pais) # para inserir o dado na árvore, basta colocar os parâmetros nessa ordem: ->
# -> (arvore a qual a variável vai ser adicionada, o dado do novo que está sendo de parâmetro nessa árvore(nesse caso a energia eólica), variavel que armazena o nome do novo pais)


#Exemplo de busca em árvores
def buscar_e_printar(arvore, chave):
    pais = busca(arvore, chave)
    if pais is not None:
        print(f"O item com chave '{chave}' foi encontrado e corresponde ao país: {pais}.")
    else:
        print(f"O item com chave '{chave}' não foi encontrado na árvore.")

# Exemplo de busca na árvore de energia eólica de um exemplo que existe, nesse caso o Brasil 
chave_existente = 82 
buscar_e_printar(arvore_por_eolica, chave_existente)

# Exemplo de busca na árvore de energia eólica de um exemplo que não existe
chave_inexistente = 999  
buscar_e_printar(arvore_por_eolica, chave_inexistente)




# Exemplos de algumas árvores criadas nas variáveis acima
print("Árvore por energia eólica:")
pprint(arvore_por_eolica)

#print("\nÁrvore por energia solar:")
#pprint(arvore_por_solar)

#print("\nÁrvore por energia nuclear:")
#pprint(arvore_por_nuclear)





