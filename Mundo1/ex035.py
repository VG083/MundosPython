# Desenvolva um programa que leia o comprimento de 3 retas e diga se elas podem ou não formar um triângulo.
# AB = 16 cm
# CD = 20 cm
# EF = 30 cm
#
# 16 + 20 = 36 > 30
# 16 + 30 = 46 > 20
# 30 + 20 = 50 > 16
#
# --------------------------
#
# AB = Valor X
# CD =  Valor X
# EF = Valor X
#
# AB + CD = VABCD
# AB + EF = VABEF
# EF + CD = VEFCD
#
# VABCD > EF
# VABEF > CD
# VEFCD > AB
print('Formação de triângulo')
print(' ')
print('Esse programa vai medir se é possível formar um triângulo a partir da medida de 3 retas.')
print(' ')
AB = int(input('Insira a medida da primeira reta: '))
CD = int(input('Insira a medida da segunda reta: '))
EF = int(input('Insira a medida da terceira reta: '))
VABCD = AB + CD
VABEF = AB + EF
VEFCD = EF + CD
if VABCD > EF:
    if VABEF > CD:
        if VEFCD > AB:
            print(' ')
            print('É possível formar um triângulo.')
        else:
            print(' ')
            print('Não é possível formar um triângulo.')
    else:
        print(' ')
        print('Não é possível formar um triângulo.')
else:
    print(' ')
    print('Não é possível formar um triângulo.')
