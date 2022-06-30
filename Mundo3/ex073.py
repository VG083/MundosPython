# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#  a) Os 5 primeiros times.
#  b) Os últimos 4 colocados.
#  c) Times em ordem alfabética. 
#  d) Em que posição está o time da Chapecoense.
tupla = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print('- Os 5 primeiros colocados: {}, {}, {}, {}, {}\n'.format(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4]))
print('- Os últimos 4  colocados: {}, {}, {}, {}\n'.format(tupla[-1], tupla[-2], tupla[-3], tupla[-4]))
lista_alfabetica = sorted(tupla)
# print('- Times em ordem alfabética: {}\n'.format(lista_alfabetica))
print('- Times em ordem alfabética: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n'.format(lista_alfabetica[0], lista_alfabetica[1], lista_alfabetica[2], lista_alfabetica[3], lista_alfabetica[4], lista_alfabetica[5], lista_alfabetica[6], lista_alfabetica[7], lista_alfabetica[8], lista_alfabetica[9], lista_alfabetica[10], lista_alfabetica[11], lista_alfabetica[12], lista_alfabetica[13], lista_alfabetica[14], lista_alfabetica[15], lista_alfabetica[16], lista_alfabetica[17], lista_alfabetica[18], lista_alfabetica[19]))
print('- A Chapecoense está em {}º lugar na tabela\n'.format(tupla.index('Chapecoense')+1))
