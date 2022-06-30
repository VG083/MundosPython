# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#  Ex: n = leiaInt('Digite um n: ')
def leiaInt(mensagem):
    """
    -> Lê se um número é inteiro antes de ler um valor
    :param mensagem: Mensagem de input que vai ser utilizada
    """
    feito = False
    valor = 0
    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            feito = True
        else:
            print('Inválido, digite um número inteiro válido')
        if feito:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar {n}')