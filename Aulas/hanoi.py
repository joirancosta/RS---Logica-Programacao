def hanoi(numero_discos, origem, destino, auxiliar):
    if numero_discos == 1:
        print(f'Mover disco 1 da {origem} para o {destino}')
    else:
        hanoi(numero_discos - 1, origem, auxiliar, destino)
        print(f'Mover disco {numero_discos} da {origem} para o {destino}')
        hanoi(numero_discos - 1, auxiliar, destino, origem)

hanoi(1, 'Torre 1', 'Torre 3', 'Torre 2')