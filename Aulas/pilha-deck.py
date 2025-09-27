
from collections import deque

def cria_pilha():
    return deque()

def insere_na_pilha(pilha, elemento):
    pilha.append(elemento)

def remove_da_pilha(pilha):
    return pilha.pop()

pilha = cria_pilha()

print(pilha)
insere_na_pilha(pilha, 5)
insere_na_pilha(pilha, 6)
insere_na_pilha(pilha, 7)
insere_na_pilha(pilha, 8)
insere_na_pilha(pilha, 9)
insere_na_pilha(pilha, 10)
print(pilha)
print(f'Removendo: {remove_da_pilha(pilha)}')
print(f'Removendo: {remove_da_pilha(pilha)}')
print(pilha)