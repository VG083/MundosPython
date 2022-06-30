# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#  Ex: n = leiaInt('Digite um n: ')
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

def leiaFloat(msg):
    while True:
        try: 
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO, DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO, ENTRADA DE DADOS INTERROMPIDA PELO USUÁRIO\033[m')
            return 0
        else:
            return n

num = leiaInt('Digite um número: ')
print(f'O valor digitado foi {num}')