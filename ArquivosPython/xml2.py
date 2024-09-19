import xml.etree.cElementTree as ET

tree = ET.parse('filmes.xml')
root = tree.getroot()
print(tree)

for filme in root:
    # print(filme.attrib['id'])

    for item in filme:
        if item.tag == 'diretor' and item.text == 'Roger Allers':
            print(f'{item.tag.capitalize()}: {item.text}')
            print(filme.find('titulo').text)
            filme.find('arrecadacao').text = 10000

tree.write('filmesAtualizado.xml')