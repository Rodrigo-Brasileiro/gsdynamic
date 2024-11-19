
#Função de complexidade O(n)
def conta_letras (palavra):
    conta = {}
    for letra in palavra:
        conta [letra] = 0
    for letra in palavra:
        conta[letra] = conta [letra] + 1
    return conta
palavra = "Salame"
returno = conta_letras(palavra)
print(returno)

#Função de Complexidade O(2n)
def conta_letras_O2n(palavra):
    conta = {}
    #
    for letra in palavra:
        if letra not in conta:
            conta[letra] = 0

    for letra in palavra:
        conta[letra] += 1

    return conta

# Exemplo de uso
print(conta_letras_O2n("Salame"))
