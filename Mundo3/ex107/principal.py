# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

p = float(input('Digite o preço: '))
print(f'O dobro de {p} é {moeda.dobro(p)}')