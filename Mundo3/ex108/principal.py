# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
import moeda

preco = float(input('Digite o preço: '))
taxa = int(input('Digite uma taxa: '))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'Se aumentarmos {moeda.moeda(preco)} em {taxa}%, o resultado será {moeda.moeda(moeda.aumentar(preco, taxa))}')
print(f'Se diminuirmos {moeda.moeda(preco)} em {taxa}%, o resultado será {moeda.moeda(moeda.diminuir(preco, taxa))}')
