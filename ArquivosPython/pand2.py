import pandas as pd

tabela = pd.read_csv('filmes.csv')

for index, row, in tabela.iterrows():
    # print(index)
    # print(row['titulo'])
    # print(row['ano'])

    # row['nota'] = 10
    # print(row['nota'])

    filme = row['titulo']
    nota = float(input(f'Digite a nota (0-10) do filme {filme}: '))

    while nota < 0 or nota > 10:
        nota = float(input(f'Digite a nota (0-10) do filme {filme}: '))


    tabela.at[index, 'nota'] = nota

    # breakpoint()

print(tabela)
tabela.to_csv('filmes2.csv', index=False)
print('Notas adicionadas com sucesso!')