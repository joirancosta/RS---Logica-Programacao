# lista = [1, 2, 3, 4]
# tuplas = (1, 2, 3, 4)

import os

tarefas = []

def adiciona_tarefa(tarefa):
    nova_tarefa = (tarefa, 'pendente')
    tarefas.append(nova_tarefa)

def exibe_tarefas():
    if not tarefas:
        print('A lista está vazia')
        return
    for tarefa in tarefas:
        print(f'{tarefa[0]} - Status: {tarefa[1]}')

def concluir_tarefa(tarefa):
    global tarefas
    # nova_lista = []
    # for t in tarefas:
    #     # if t[0] == tarefa:
    #     #     # t[1] = 'concluída'
    #     #     nova_lista.append((tarefa, 'concluída'))
    #     # else:
    #     #     nova_lista.append(t)
    #     nova_lista.append(t if t[0] != tarefa else (tarefa, 'concluída'))    
    # tarefas = nova_lista
    tarefas = [ (t[0], 'concluída') if t[0] == tarefa else t for t in tarefas ]

def remover_tarefa(tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t[0] != tarefa ]
    
def buscar_tarefa(tarefa):
    # for t in tarefas:
    #     if t[0] == tarefa:
    #         print(f'Tarefa encontrada: {t[0]} - Status: {t[1]}')
    #         return
    # print(f'Não achei: {tarefa}')
    resultado = [ t for t in tarefas if t[0].lower() == tarefa.lower() ]
    # if len(resultado) > 0:
    if resultado:
        for titulo, status in resultado:
            print(f'Encontrada: {titulo} - Status: {status} ')
    else:
        print(f'Tarefa não encontrada: {tarefa}')

# adiciona_tarefa('Lavar a louça')
# adiciona_tarefa('Arrumar a cama')
# exibe_tarefas()
# print('Agora vou concluir...')
# concluir_tarefa('Arrumar a cama')
# exibe_tarefas()
# print('Agora removendo...')
# remover_tarefa('Arrumar a cama')
# exibe_tarefas()
# buscar_tarefa('Lavar a louça')

while True:
    os.system('cls')

    print('Bem vindos ao gerenciador de listas de tarefas')
    print()
    print('O que queres fazer agora?')
    print('1 - Listar tarefas')
    print('2 - Adicionar tarefa')
    print('3 - Remover tarefa')
    print('4 - Marcar tarefa como concluída')
    print('5 - Buscar tarefa')
    print('0 - Sair')
    opcao = int(input('Digite uma opção: '))

    match opcao:
        case 1:
            exibe_tarefas()
        case 2:
            tarefa = input('Digite a tarefa: ')
            adiciona_tarefa(tarefa)
        case 3:
            tarefa = input('Digite a tarefa: ')
            remover_tarefa(tarefa)
        case 4:
            tarefa = input('Digite a tarefa: ')
            concluir_tarefa(tarefa)
        case 5:
            tarefa = input('Digite a tarefa: ')
            buscar_tarefa(tarefa)
        case 0:
            break
        case _:
            print('Opcao inválida!')
    print()
    input('Pressione ENTER para continuar...')