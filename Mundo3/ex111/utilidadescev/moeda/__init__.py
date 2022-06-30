def aumentar(preco = 0, taxa = 0, formato=False):
    resposta = preco + (preco * taxa/100)
    return resposta if formato is False else moeda(resposta)


def diminuir(preco = 0, taxa = 0, formato=False):
    resposta = preco - (preco * taxa/100)
    return resposta if formato is False else moeda(resposta)


def dobro(preco = 0, formato=False):
    resposta = preco * 2
    return resposta if formato is False else moeda(resposta)


def metade(preco = 0, formato=False):
    resposta = preco / 2
    return resposta if formato is False else moeda(resposta)
    

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')

def resumo(preco=100, taxa=10):
    print('-' * 30)
    print('Resumo do Valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Aumento de {taxa}%: \t{aumentar(preco, taxa, True)}')
    print(f'Desconto de {taxa}%: \t{diminuir(preco, taxa, True)}')
    print('-' * 30)
