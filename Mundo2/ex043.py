# Desafio 043: Calcular índice de massa corporal
# 	Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
# 	a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc <= 18.5:
    print(' ')
    print('De acordo com seu índice IMC, você está abaixo do peso')
elif imc <= 25:
    print(' ')
    print('De acordo com seu índice IMC, você está no peso ideal')
elif imc <= 30:
    print(' ')
    print('De acordo com seu índice IMC, você está com sobrepeso')
elif imc <= 40:
    print(' ')
    print('De acordo com seu índice IMC, você está com obesidade')
elif imc > 40:
    print(' ')
    print('De acordo com seu índice IMC, você está com obesidade mórbida')
