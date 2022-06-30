def aumentar(preco, taxa):
    resposta = preco + (preco * taxa/100)
    return resposta


def diminuir(preco, taxa):
    resposta = preco - (preco * taxa/100)
    return resposta


def dobro(preco):
    resposta = preco * 2
    return resposta


def metade(preco):
    resposta = preco / 2
    return resposta
    