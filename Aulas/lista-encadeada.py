
lista = None

# lista = {
#     'valor': 5,
#     'proximo': None,
# }

# print(lista)

# novo = {
#     'valor': 8,
#     'proximo': None,
# }

# lista['proximo'] = novo

# print(lista)

def exibe_lista():
    if not lista:
        print('Lista vazia.')
        return
    elemento = lista
    while elemento != None:
        # print(f'{elemento['valor']} -', end = ' ')
        print(elemento['valor'], end = ' ')
        elemento = elemento['proximo']
    print('.')

def adiciona_no_fim(elemento):
    global lista
    if not lista:
        lista = {
            'valor': elemento,
            'proximo': None,
        }
        return
    atual = lista
    while atual['proximo']:
        atual = atual['proximo']
    atual['proximo'] = {
        'valor': elemento,
        'proximo': None,
    }

exibe_lista()
adiciona_no_fim(5)
exibe_lista()
adiciona_no_fim(8)
exibe_lista()
adiciona_no_fim(13)
exibe_lista()