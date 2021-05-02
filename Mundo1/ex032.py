# Faça um programa que leia um ano qualquer e mostre se ele é ano bissexto.
print('Ano bissexto')
print(' ')
a = int(input('Digite um ano: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é bissexto'.format(a))
else:
    print('O ano {} é normal'.format(a))