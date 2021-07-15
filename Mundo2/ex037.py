# Desafio 037: Conversor de bases númericas
# 	Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
# (Assistir aula de conversão no curso em vídeo)
print('Conversor de decimais')
print(' ')
n = int(input('Digite um número decimal: '))
print('Escolha uma base de conversão:')
print('1. Converter para binário')
print('2. Converter para octal')
print('3. Converter para hexadecimal')
op = int(input('Sua opção de conversão: '))
if op == 1:
    print(' ')
    print('{} convertido para binário é {}'.format(n, bin(n)[2:]))
elif op == 2:
    print(' ')
    print('{} convertido para octal é {}'.format(n, oct(n)[2:]))
elif op == 3:
    print(' ')
    print('{} convertido para hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print(' ')
    print('ERROR')