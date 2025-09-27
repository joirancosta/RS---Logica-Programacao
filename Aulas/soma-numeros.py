soma = 0
numero = 1
total = 0

while numero <= 10:
    soma = soma + numero
    print(f'Soma: {soma}')
    print(f'numero: {numero}')
    numero = numero + 1

for index in range(1,11):
    total += index

resultado = sum([i for i in range (1,11)])

print(f'A soma dos número de 1 a 10 é: {soma}')
print(f'A total dos número de 1 a 10 é: {total}')
print(f'A resultado dos número de 1 a 10 é: {resultado}')