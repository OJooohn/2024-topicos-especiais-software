import xml.etree.cElementTree as ET
from xml.dom import minidom

from Tools.scripts.summarize_stats import pretty

tree = ET.parse('filmes.xml')
root = tree.getroot()

def prettify(xml_string):
    """Função para formatar o XML com identação e quebras de linha."""
    parsed = minidom.parseString(xml_string)
    # O minidom adiciona uma linha extra no início, então removemos a primeira linha.
    return '\n'.join(line for line in parsed.toprettyxml(indent="    ").splitlines() if line.strip())

while True:
    quant = 0
    for filme in root:
        quant += 1

    print('[0] Sair')
    print('[1] Adicionar filme')
    opcao = int(input('Digite sua opção: '))

    if opcao == 0:
        break
    elif opcao == 1:
        print('>> ADICIONAR FILME')
        nome_filme = input('Digite o nome do filme: ')
        ano_filme = input('Digite o ano do filme: ')
        nome_diretor = input('Digite o nome do diretor: ')
        arrecadacao = input('Digite a arrecadação do filme: ')

        filme = ET.SubElement(root, 'filme')
        filme.set('id', str(quant + 1))

        filme_tlt = ET.SubElement(filme, 'titulo')
        filme_tlt.text = nome_filme

        filme_year = ET.SubElement(filme, 'ano')
        filme_year.text = ano_filme

        filme_director = ET.SubElement(filme, 'diretor')
        filme_director.text = nome_diretor

        filme_arrecadacion = ET.SubElement(filme, 'arrecadacao')
        filme_arrecadacion.text = arrecadacao

        xml_str = ET.tostring(root, encoding='utf-8', method='xml')
        formatted_xml = prettify(xml_str.decode('utf-8'))

        with open('filmes.xml', 'w', encoding='utf-8') as arquivo:
            arquivo.write(formatted_xml)

    else:
        print('>> Opção inválida! Digite novamente...')