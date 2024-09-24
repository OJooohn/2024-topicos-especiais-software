import csv

with open('filmes_disney.csv', mode='r', newline='') as arquivo:
    filmes = csv.reader(arquivo)

    filmes_lidos = []

    header = next(filmes)
    for linha in arquivo:
        id, titulo, ano, diretor, arrecadacao = linha.split(',')

        filmes_lidos.append( (int(id), titulo, int(ano), diretor, float(arrecadacao) ))

    filmes_lidos.sort(key=lambda filme: filme[4], reverse=True)

    print(f'{"ID":<3}{"Título":^30}{"Ano":<7}{"Diretor":^30}{"Arrecadação":<8}')
    print('-' * 85)
    for filme in filmes_lidos[:3]:
        id, titulo, ano, diretor, arrecadacao = filme
        print(f'{id:<3}{titulo:^30}{ano:<7}{diretor:^30}{arrecadacao:<8}')

    # print(filmes_lidos[:3])
