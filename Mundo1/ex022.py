# Desafio 022: Analisador de texto
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas.
# - O nome com todas as letras minúsculas.
# - Quantas letras tem sem considerar espaços
# - Quantas letras tem o primeiro nome.
nome = input('Digite seu nome completo: ')
print('Seu nome com todas as letras maiúsculas é: ', nome.upper())
print('Seu nome com todas as letras minúsculas é: ', nome.lower())
nome2 = nome.count(' ')
nome3 = len(nome)
print('O número de letras no seu nome completo é: ', nome3-nome2)
nome4 = nome.split()
nome5 = nome4[0]
nome6 = len(nome5)
print('O número de letras no seu primeiro nome é: ', nome6)
