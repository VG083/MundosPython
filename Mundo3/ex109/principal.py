# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda

preco = float(input('Digite o preço: '))
taxa = int(input('Digite uma taxa: '))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'Se aumentarmos {moeda.moeda(preco)} em {taxa}%, o resultado será {moeda.aumentar(preco, taxa, True)}')
print(f'Se diminuirmos {moeda.moeda(preco)} em {taxa}%, o resultado será {moeda.diminuir(preco, taxa, True)}')
