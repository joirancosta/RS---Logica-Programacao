print('Vamos falar sobre programação!')
print('Escolha um assunto abaixo:')
print('-> JAVA')
print('-> HTML')
print('-> CSS')
print('-> JAVASCRIPT')
print('-> TYPESCRIPT')
print('-> C#')

resposta = input('Escolha uma assunto de programação: ')
resposta = resposta.lower()

match resposta:
		case 'java':
				print('Linguagem orientada a objetos muito usada em sistemas corporativos, aplicativos Android (tradicionalmente) e back-end. Conhecida pela portabilidade (“escreva uma vez, execute em qualquer lugar”).')
		case 'html':
				print('Não é uma linguagem de programação, e sim uma linguagem de marcação usada para estruturar páginas web (títulos, textos, imagens, formulários etc.).')
		case 'css':
				print('Também não é linguagem de programação. Serve para estilizar páginas HTML: cores, fontes, espaçamento, animações e layout.')
		case 'python':
				print('Linguagem de sintaxe simples, usada em automação, análise de dados, inteligência artificial, desenvolvimento web e scripts.')
		case 'c#':
				print('Criada pela Microsoft. Muito usada em desenvolvimento de sistemas, APIs, aplicações Windows e jogos com Unity.')
		case 'javascript':
				print('Linguagem principal da interatividade na web. Faz botões funcionarem, atualiza páginas sem recarregar e também é usada no back-end.')
		case 'typescript':
				print('Extensão do JavaScript com tipagem estática. Ajuda a evitar erros em projetos grandes e é bastante usada em aplicações modernas.')
		case _:
			print('Ainda estou aprendendo')