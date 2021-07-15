# Desafio 036: Aprovando empréstimo
# 	Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# 	da casa, o salário do comprador e em quantos anos ele vai pagar.
# 	Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
# 	negado
print('Aprovando empréstimo')
print(' ')
print('Para realizar o empréstimo da sua casa própria, precisaremos fazer algumas perguntas: ')
vc = float(input('Quanto custa a casa? R$ '))
sc = float(input('Quanto é o salário mensal do comprador? R$ '))
te = int(input('Em quantos anos será pago o empréstimo? '))
p = vc / (te * 12)
min = sc * 30 / 100
if p <= min:
    print(' ')
    print('O empréstimo foi aprovado!')
    print('Previsão do fim do empréstimo: {} anos'.format(te))
    print('Valor das parcelas: R$ {:.2f}'.format(p))
elif p >= min:
    print('Seu empréstimo foi negado!')