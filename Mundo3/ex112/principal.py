# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
from utilidadescev import moeda
from utilidadescev import dados

preco = dados.leiaDinheiro('Digite um preço: ')
taxa = dados.leiaTaxa('Digite uma taxa: ')
print(moeda.resumo(preco, taxa))
