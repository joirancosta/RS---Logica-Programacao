texto = 'As drosófilas são pequenos insetos pertencentes ao gênero Drosophila, sendo a espécie mais conhecida a Drosophila melanogaster. Elas são amplamente encontradas em ambientes onde há frutas em decomposição, pois se alimentam de leveduras e outros microrganismos presentes nesses locais. Seu ciclo de vida é curto, com duração média de 10 a 14 dias, o que facilita sua reprodução rápida e grande abundância.\
\
\Esses insetos ganharam destaque no meio científico por serem amplamente utilizados como organismos modelo em pesquisas genéticas e biológicas. A Drosophila melanogaster foi um dos primeiros organismos a ter seu genoma completamente sequenciado. Sua genética relativamente simples, combinada com uma grande quantidade de descendentes e facilidade de manejo em laboratório, faz dela uma excelente ferramenta para estudos sobre hereditariedade, mutações e desenvolvimento.\
\
\Além da genética, as drosófilas também são estudadas em áreas como neurociência, biologia do comportamento, e até mesmo pesquisas sobre envelhecimento e doenças humanas. Muitos genes da drosófila têm equivalentes em humanos, o que permite que experimentos com esses insetos ofereçam insights importantes sobre processos biológicos conservados entre as espécies.\
\
\Do ponto de vista ecológico, as drosófilas têm um papel importante na decomposição de matéria orgânica, contribuindo para o equilíbrio dos ecossistemas. Elas também servem de alimento para vários predadores, como aranhas, sapos e pássaros, sendo parte relevante da cadeia alimentar. Apesar disso, podem ser consideradas pragas em ambientes domésticos e em estabelecimentos que armazenam frutas e vegetais.\
\
Por fim, o estudo das drosófilas continua a fornecer contribuições valiosas para a ciência moderna. Muitas descobertas fundamentais sobre cromossomos, genes e herança foram feitas com base em experimentos com esses pequenos insetos. Sua importância vai muito além do que seu tamanho sugere, tornando-a uma das criaturas mais estudadas e úteis na história da biologia.'

palavras = texto.split()

tabela = {}

for palavra in palavras:
    indice = palavra[0]#.upper()
    if indice not in tabela:
        tabela[indice] = []
    tabela[indice].append(palavra)

for chave, valor in tabela.items():
    # print(f'{chave}: {len(valor)}')
    print(f'{chave}: {valor}')

print(len(texto.split()))

