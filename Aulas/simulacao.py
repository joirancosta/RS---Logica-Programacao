# Se eu jogar dois dados 1000 vezes, quantas vezes dará a soma 7?

import random

numero_de_vezes = 0

for _ in range(1000):
    dado_01 = random.randint(1, 6)
    dado_02 = random.randint(1, 6)
    soma = dado_01 + dado_02
    if soma == 7:
        numero_de_vezes += 1

print(f'A soma dos dados deu 7 {numero_de_vezes} vezes')