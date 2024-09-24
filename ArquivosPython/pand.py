import pandas as pd

tabela = pd.read_csv('filmes.csv')
print(tabela)

tabela = tabela.sort_values(by='arrecadacao', ascending=False)

# top 3 filmes com maior arrecadacao
top3 = tabela.head(3)

print('-'*70)
print(top3)

print('-'*70)
print(top3[['titulo', 'diretor', 'arrecadacao']])

print('-'*70)
print(top3[['titulo', 'arrecadacao']])

num = int(input('Quantidade filmes: '))
topFilmes = tabela.head(num)

print(f'TOP {num} FILMES')
print('-'*70)
print(topFilmes[['titulo', 'arrecadacao']])
print('-'*70)
