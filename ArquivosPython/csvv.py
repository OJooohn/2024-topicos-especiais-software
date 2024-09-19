import csv

from xml2 import filme

with open('filmes.csv', mode='r', newline='') as arquivo_csv:
    filmes = csv.reader(arquivo_csv)

    header = next(filmes)
    print('  |', ' | '.join(header), '|')

    for linha in filmes:
        print(' | '.join(linha))

with open('filmes.csv', mode='r', newline='') as arquivo_csv:
    filmes = csv.DictReader(arquivo_csv)

    for linha in filmes:
        print(linha)

with open('filmes.csv', mode='a', newline='') as arquivo_csv:
    filmes = csv.writer(arquivo_csv)

    filmes.writerow([1, 'Nome', 2010, 'outro', 1000])