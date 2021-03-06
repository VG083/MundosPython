# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano):
    """
    -> Essa função retorna se uma determinada pessoa pode votar ou não com base na sua idade
    :param ano: Idade da pessoa em questão
    """
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos não é permitido votar'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos o voto é opcional'
    else:
        return f'Com {idade} anos o voto é obrigatório'

print(voto(2000))