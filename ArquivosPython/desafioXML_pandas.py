import pandas as pd

tabela = pd.read_xml('filmes.xml', parser='etree')
print(tabela)

for index, row in tabela.iterrows():
    titulo_filme = row['titulo']
    nota = float(input(f'Digita a nota do filme {titulo_filme}: '))

    while nota < 0 or nota > 10:
        nota = float(input(f'Digite a nota (0-10) do filme {titulo_filme}: '))

    tabela.at[index, 'nota'] = nota

print(tabela)
tabela.to_xml('filmes2.xml', parser='etree')
print('Notas adicionadas com sucesso!')