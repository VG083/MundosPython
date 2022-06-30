# Aprimore o desafio anterior, mostrando no final: 
#  A) c.
#  B) A soma dos valores da terceira coluna.
#  C) O maior valor da segunda linha.
matriz = [[0,0,0],  
          [0,0,0],
          [0,0,0]]
somapares = soma3coluna = maior2linha = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'[{linha},{coluna}]: '))
        if((matriz[linha][coluna]%2) == 0):
            somapares += matriz[linha][coluna]
        if(coluna == 2):
            soma3coluna += matriz[linha][coluna]
        if(linha == 1 and matriz[linha][coluna] > maior2linha):
            maior2linha = matriz[linha][coluna]
print(f'\nMatriz:')
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^3}]', end=' ')
    print()
print(f'\nA soma de todos os valores pares digitados é {somapares}')
print(f'A soma dos valores da terceira coluna é {soma3coluna}')
print(f'O maior valor da segunda linha é {maior2linha}')
