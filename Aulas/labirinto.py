import random

def criar_labirinto(tamanho):
    labirinto = [ [ random.randint(0, 1) for _ in range(tamanho) ] for _ in range(tamanho) ]
    labirinto[0][0] = 8
    labirinto[tamanho - 1][tamanho - 1] = 9
    return labirinto

def exibir_labirinto(labirinto):
    for linha in labirinto:
        print(linha)

def nao_pode_seguir(labirinto, linha, coluna):
    if (
        linha >= len(labirinto) or
        coluna >= len(labirinto) or
        linha < 0 or
        coluna < 0 or
        labirinto[linha][coluna] == 2 or
        labirinto[linha][coluna] == 1
    ):
        return True

def explorar(labirinto, linha, coluna):
    print(f'Explorando ({linha}, {coluna})')
    if nao_pode_seguir(labirinto, linha, coluna):
        print(f'Não pode seguir ({linha}, {coluna})')
        return False
    if labirinto[linha][coluna] == 9:
        print('Chegou ao final')
        return True
    
    labirinto[linha][coluna] = 2

    return (
        explorar(labirinto, linha, coluna + 1) or
        explorar(labirinto, linha, coluna - 1) or
        explorar(labirinto, linha + 1, coluna) or
        explorar(labirinto, linha - 1, coluna)
    )

lab = criar_labirinto(5)
exibir_labirinto(lab)

explorar(lab, 0, 0)
exibir_labirinto(lab)