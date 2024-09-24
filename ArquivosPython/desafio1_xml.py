import xml.etree.cElementTree as ET

tree = ET.parse('filmes.xml')
root = tree.getroot()

diretor_filtro = input('Digite o nome de um diretor: ')

for filme in root:
    for item in filme:
        if item.tag == 'diretor' and item.text == diretor_filtro:
            # print(f'{item.tag.capitalize()}: {item.text}')
            print('Título: ' + filme.find('titulo').text)
            print('Ano: ' + filme.find('ano').text)
            print('Arrecadação: ' + filme.find('arrecadacao').text)