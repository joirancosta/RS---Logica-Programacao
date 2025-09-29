from heapq import *

fila_prioridade = []

heappush(fila_prioridade, (2, "Atender cliente VIP"))
heappush(fila_prioridade, (1, "Situação crítica"))
heappush(fila_prioridade, (3, "Responder e-mail"))
heappush(fila_prioridade, (1, "Apagar incêndio"))

print(fila_prioridade)

while fila_prioridade:
    prioridade, tarefa = heappop(fila_prioridade)
    print(f'Executando: {tarefa} - Prioridade: {prioridade}')

print(fila_prioridade)