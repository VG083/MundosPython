# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#  Ex: 
#  escreva('Olá, Mundo!')
#  Saída:
#  ~~~~~~~~~
#   Olá, Mundo!
#  ~~~~~~~~~
def escreva(texto):
    print('-'*len(texto))
    print(texto)
    print('-'*len(texto))

texto = str(input('Digite um texto: '))

print()
escreva(texto)