questoes = [
    ['Quanto é 5 + 8?', 5 + 8],
    ['Quanto é 10 - 7?', 10 - 7],
    ['Quanto é 9 * 3?', 9 * 3],
    ['Quanto é 81 / 9?', 81 / 9],
    ['Quanto é (2 + 2) / 2?', (2 + 2) / 2],
    ['Quanto é (56 - 46) / (5 * 2)?', (56 - 46) / (5 * 2)]
]

pontos = 0

for questao in questoes:
    resposta = int(input(f'{questao[0]} '))
    if resposta == questao[1]:
        pontos += 1

print(f'Pontuação: {pontos}')
