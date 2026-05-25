import random
import os

def exibe_mapa():
  for linha in mapa_tesouro:
    print('|'.join(linha))
    print('-' * 7)

mapa_tesouro = [
  [' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' '],
]

linha_tesouro = random.randint(0, 3)
coluna_tesouro = random.randint(0, 3)
tentativas = 0

while True:
  try:
    if tentativas >= 5:
      os.system("clear")
      print('Game Over, você perdeu!')
      mapa_tesouro[linha_tesouro][coluna_tesouro] = '🌟'
      print("O tesouro estava aqui:")
      exibe_mapa()
      break

    print('Tente achar o tesouro no mapa!')
    print(f"Tentativa {tentativas}")
    exibe_mapa()

    linha = int(input('Digite a linha: '))
    coluna = int(input('Digite a coluna: '))

    if mapa_tesouro[linha][coluna] == 'X':
      print('Posição já jogada!')
      continue
    elif (
        mapa_tesouro[linha][coluna] != ' ' or 
        not 0 <= linha <= 3 or 
        not 0 <= coluna <= 3
      ):
      print('Jogada inválida!')
      continue
    elif linha == linha_tesouro and coluna == coluna_tesouro:
      os.system("clear")
      print('Parabéns, você venceu! Achou o tesouro!')
      mapa_tesouro[linha][coluna] = '🌟'
      exibe_mapa()
      break
    else:
      mapa_tesouro[linha][coluna] = 'X'
      tentativas += 1
    
    os.system("clear")
  except ValueError:
    print('Digite valores númericos entre 0 e 2.')
  except IndexError:
    print('Digite valores númericos entre 0 e 2.')
