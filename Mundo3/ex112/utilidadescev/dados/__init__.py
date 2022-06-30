def leiaDinheiro(mensagem):
    valido = False
    while not valido:
        entrada = str(input(mensagem)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO! >{entrada}< É UM PREÇO INVÁLIDO')
        else:
            valido = True
            return float(entrada)


def leiaTaxa(mensagem):
    valido = False
    while not valido:
        entrada = str(input(mensagem))
        if entrada.isalpha():
            print(f'ERRO! >{entrada}< É UMA TAXA INVÁLIDA')
        else:
            valido = True
            return int(entrada)
