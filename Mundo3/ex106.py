# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
cores = (
    '\033[m', #0 = Sem cores
    '\033[0;30;41m', #1 = Vermelho
    '\033[0;30;42m', #2 = Verde
    '\033[0;30;43m', #3 = Amarelo
    '\033[0;30;44m', #4 = Azul
    '\033[0;30;45m', #5 = Roxo
    '\033[0;30m', #6 = Branco
)

def pesquisar(comando):
    """
    -> Essa função pode pesquisa pela docstring de um método passado no seu parâmetro
    :param comando: Recebe o método que deve pesquisar
    """
    titulo(f'Acessando docstring de {comando}', cor=5)
    help(comando)

def titulo(mensagem, cor=0):
    """
    -> Essa funçã exibe um texto em formato de título:
    :param mensagem: Recebe o texto a  exibir
    :param cor: Recebe a cor de fundo
    """
    tamanho = len(mensagem)
    print(cores[cor], end='')
    print('-' * tamanho)
    print(mensagem)
    print('-' * tamanho)
    print(cores[0], end='')

comando = ''
titulo(' SISTEMA DE HELP ', cor=2)
while True:
    comando = str(input('Função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        pesquisar(comando)
titulo(' FIM DO PROGRAMA ', cor=1)