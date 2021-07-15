# Desafio 042: Analisando triângulo v2.0
# 	Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo')
    if r1 == r2 == r3:
        print('O triângulo será equilátero')
    elif r1 != r2 != r3 != r1:
        print('O triângulo será escaleno')
    else:
        print('O triângulo será isósceles')
else:
    print('Os segmentos acima não podem formar um triângulo')