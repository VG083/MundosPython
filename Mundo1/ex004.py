# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(n))
print('O valor é alfanumérico?', n.isalnum())
print('O valor é numérico?', n.isnumeric())
print('O valor é alfabético?', n.isalpha())
print('O valor está em letras minusculas?', n.islower())
print('O valor está em letras maiusculas?', n.isupper())