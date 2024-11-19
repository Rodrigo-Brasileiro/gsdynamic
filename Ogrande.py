#Função de complexidade O(n)
def conta_letras (palavra):
    conta = {}
    for letra in palavra:
        conta [letra] = 0
    for letra in palavra:
        conta[letra] = conta [letra] + 1
    return conta
palavra = "Salame" * 1000
returno = conta_letras(palavra)
print(returno)

#Função de Complexidade O(2n)
def conta_letras_O2n(palavra):
    conta = {}
    for letra in palavra:
        if letra not in conta:
            conta[letra] = 0
    for letra in palavra:
        conta[letra] += 1
    return conta

palavra2 = "R" * 1000
returno2 = conta_letras(palavra2)
print(returno2)


# Se implementada, a a função O(n) deverá ter um consumo energético menor que a função de complexidade O(2n), uma vez que
# para uma lista de 1000 elementos, a função de complexidade O(n) realiza 1000 operações para chegar ao fim da lista, enquanto a função O(2n)
# realiza 2000 operações até chegar ao final da mesma lista, resultando em um consumo energético maior, visto que ela levará
# o dobro do tempo para ser concluída. Logo, a proporção delas 1:2.