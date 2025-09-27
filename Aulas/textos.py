frase = ' O curso de Lógica de Programação é supimpa! '
# print(f'Primeira letra: {frase[0]}')
# print(f'Útima letra: {frase[-1]}')
# print(f'Tamanho da frase: {len(frase)} caracteres')
# print(f'Maiúsculas: {frase.upper()}')
# print(f'Minúscula: {frase.lower()}')
# print(f'Fatiando: {frase.split()}')
# print(f'Fatiando: {frase.split('a')}')
# print(f'Limpando: {frase.strip()}')

def analisador_de_texto(texto):
    palavras = texto.split()
    numero_de_palavras = len(palavras)
    numero_de_caracteres = len(texto)
    numero_de_caracteres_sem_espacos = numero_de_caracteres - texto.count(' ')
    return numero_de_palavras, numero_de_caracteres, numero_de_caracteres_sem_espacos

numero_palavra, numero_caractere, numero_caractere_sem_espaco = analisador_de_texto(frase)

print(f'N°. palavras: {numero_palavra}')
print(f'N°. caracteres: {numero_caractere}')
print(f'N°. caracteres sem espaços: {numero_caractere_sem_espaco}')