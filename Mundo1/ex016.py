# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
# Exemplo:
# Digite um número: "6.127"
import math
n = float(input('Digite um valor quebrado: '))
# math.floor é um módulo que arredonda um número quebrado para baixo, mostrando assim seu valor inteiro
v = math.trunc(n)
print('O valor digitado foi {} e seu valor inteiro é {}'.format(n, v))
