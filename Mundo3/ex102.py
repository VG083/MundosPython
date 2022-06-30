# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    -> Essa função retorna uma fatorial
    :param n: Número para calcular fatorial
    :param show: Mostra a resolução da fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c>1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f

print(fatorial(5, show=True))