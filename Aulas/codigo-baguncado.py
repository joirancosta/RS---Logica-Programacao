'''
def a(x, y, z): r=[]; s=0
for t in x:
 if t>y:s+=t
 r.append(t*z)
print('soma', s)
print('lista', r)
'''
def somar_maiores(lista, limite):
    return sum(elemento for elemento in lista if elemento > limite)

def multiplicar_lista(lista, multiplicador):
    return [elemento * multiplicador for elemento in lista]

def exibir_valores(lista, limite, multiplicador):
    # resultado = []
    # soma_maiores = 0
    # for elemento in lista:
        # if elemento > limite:
        #     soma_maiores += elemento
        # resultado.append(elemento * multiplicador)

    resultado = multiplicar_lista(lista, multiplicador)
    soma_maiores = somar_maiores(lista, limite)

    print('Soma: ', soma_maiores)
    print('Lista: ', resultado)

exibir_valores([10, 20, 30, 40, 50], 35, 2)