# Função de complexidade O(n)
def conta_letras(palavra):
    conta = {}
    for letra in palavra:
        conta[letra] = 0
    for letra in palavra:
        conta[letra] += 1
    return conta

# Função de complexidade O(n²)
def conta_letras2(palavra):
    conta = {}
    for i in range(len(palavra)):
        letra = palavra[i]
        if letra not in conta:
            frequencia = 0
            for j in range(len(palavra)):
                if palavra[j] == letra:
                    frequencia += 1
            conta[letra] = frequencia
    return conta

# Exemplo de entrada:
palavra = "R" * 1000  # Uma string com 1000 caracteres 'R'.

retorno_linear = conta_letras(palavra)
retorno_quadratico = conta_letras2(palavra)


# Proporção entre os consumos energéticos com entrada de tamanho 1000:
# - A função O(n) realiza aproximadamente 2000 operações.
# - A função O(n²) realiza aproximadamente 1.000.000 operações.
# - Proporção: o consumo energético da função O(n²) é 500 vezes maior que o da função O(n).

# Qual função terá maior consumo energético com listas de tamanho 1000?
# - A função conta_letras2 consome mais energia,
#   pois executa significativamente mais operações do que conta_letras.
