# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#  A) Quantas vezes apareceu o valor 9.
#  B) Em que posição foi digitado o primeiro valor 3.
#  C) Quais foram os números pares.

tupla = (int(input('Digite o primeiro número: ')),
        int(input('Digite o segundo número: ')),
        int(input('Digite o terceiro número: ')),
        int(input('Digite o quarto número: '))
)

print(f'\nNúmeros digitados: {tupla}\n')
print(f'O número 9 foi digitado {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 foi digitado na posição: {tupla.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print('Os números pares digitados foram: ', end='')
for i in tupla:
    if i%2 == 0:
        print(i, end=' ')
