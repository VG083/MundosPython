# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.
print('Aumento salarial')
print(' ')
s = int(input('Digite o valor atual do salário que deseja aumentar: '))
if s <= 1250:
    sf = s * 1.15
    print('O salário aumentado será R${}'.format(sf))
else:
    sff = s * 1.10
    print('O salário aumentado será R${}'.format(sff))