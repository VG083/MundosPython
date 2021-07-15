# Desafio 041: Classificando atletas
# 	A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# 	categoria de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER
idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    print(' ')
    print('Seu atleta pertence a Categoria Mirim')
elif idade <= 14:
    print(' ')
    print('Seu atleta pertence a Categoria Infantil')
elif idade <= 19:
    print(' ')
    print('Seu atleta pertence a Categoria Junior')
elif idade <= 20:
    print(' ')
    print('Seu atleta pertence a Categoria Senior')
elif idade > 20:
    print(' ')
    print('Seu atleta pertence a Categoria Master')