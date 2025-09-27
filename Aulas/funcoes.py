def ola_mundo():
    print('Olá, mundo!')

def ola_pessoal(nome):
    print(f'Olá, {nome}')

def dobro(numero):
    return numero * 2

def multiplica_dois_numeros(a, b = 0):
    """ Multiplica 2 números """
    return a * b

x = 5 # Variável global
def soma():
    x = 10 # Variável local
    print(x)
    return x + 1

soma()
print(x)

ola_mundo()
ola_pessoal('Fulano')
print(dobro(5) + 2)
print(multiplica_dois_numeros(5, 8))
print(multiplica_dois_numeros(5))