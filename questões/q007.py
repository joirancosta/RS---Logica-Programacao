numero_certo = 44
tentativas = 1

while True:
    chute = int(input('Adivinhe um número de 1 a 50: '))
    if chute == numero_certo:
        break
    tentativas += 1

print(f'Parabens, acertou o número em {tentativas} tentativas')