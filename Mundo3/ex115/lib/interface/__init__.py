def leiaInt(msg):
    while True:
        try: 
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO, DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO, ENTRADA DE DADOS INTERROMPIDA PELO USUÁRIO\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-'*tam


def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('\033[33mSua opção: \033[m')
    return opcao