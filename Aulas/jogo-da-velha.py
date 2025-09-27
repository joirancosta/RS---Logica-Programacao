# tabuleiro = [ [' ' for _ in range(3) ] for _ in range(3) ]

tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

def exibe_tabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

def jogada(linha, coluna):
    # global jogador
    if (
        tabuleiro[linha][coluna] != ' ' or 
        not 0 <= linha <= 2 or 
        not 0 <= coluna <= 2
    ):
        print('Jogada inválida!')
        return jogador

    tabuleiro[linha][coluna] = jogador
    """
    if jogador == "X":
        # jogador = 'O'
        return 'O'
    else:
        # jogador = 'X'
        return 'X'
    """
    return 'O' if jogador == "X" else "X"

def tem_ganhador():
    for linha in range(3):
        if (
            tabuleiro[linha][0] != ' ' and
            tabuleiro[linha][0] == tabuleiro[linha][1] and
            tabuleiro[linha][0] == tabuleiro[linha][2]
        ):
            print(f'{tabuleiro[linha][0]} GANHOU')
            return True
    for coluna in range(3):
        if (
            tabuleiro[0][coluna] != ' ' and
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and
            tabuleiro[0][coluna] == tabuleiro[2][coluna]
        ):
            print(f'{tabuleiro[0][coluna]} GANHOU')
            return True
    if (
        tabuleiro[1][1] != ' ' and
        (
            (
            tabuleiro[0][0] == tabuleiro[1][1] and
            tabuleiro[0][0] == tabuleiro[1][1]
            ) or
            (
                tabuleiro[0][2] == tabuleiro[1][1] and
                tabuleiro[0][0] == tabuleiro[2][1]
            )
        )
    ):
        print(f'{tabuleiro[linha][0]} - GANHOU')
        return True
    return False

def tem_empate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                return False
    print('Acabou empatado!')
    return True

jogador = 'X'

while True:
    print(f'Jogador da vez: {jogador}')
    # jogador = jogada(1, 1)
    # jogador = jogada(1, 2)
    
    try:
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        jogador = jogada(linha, coluna)
    # except (ValueError, IndexError):
    except ValueError:
        print('Digite valores númericos entre 0 e 2.')
    except IndexError:
        print('Digite valores númericos entre 0 e 2.')
    
    exibe_tabuleiro()
    
    if tem_ganhador() or tem_empate():
        break