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