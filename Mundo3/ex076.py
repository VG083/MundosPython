# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tupla = (
    'Notebook', 2400.99,
    'Monitor', 1299.99,
    'Teclado', 100,
    'Mouse', 49.99,
    'Mousepad', 49.99,
    'Mesa', 1499.99,
    'Cadeira', 1199.99,
)

print('Lista de produtos e preços\n')
for i in range(0, len(tupla)):
    if i%2 == 0:
        print(f'{tupla[i]:.<30}', end='')
    else:
        print(f'R$ {tupla[i]}')