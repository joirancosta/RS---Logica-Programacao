
from collections import deque

def cria_fila():
    return deque()

def insere_na_fila(fila, elemento):
    fila.append(elemento)

def remove_da_fila(fila):
    return fila.popleft()

fila = cria_fila()

print(fila)
insere_na_fila(fila, 5)
insere_na_fila(fila, 6)
insere_na_fila(fila, 7)
insere_na_fila(fila, 8)
insere_na_fila(fila, 9)
insere_na_fila(fila, 10)
print(fila)
print(f'Removendo: {remove_da_fila(fila)}')
print(f'Removendo: {remove_da_fila(fila)}')
print(fila)