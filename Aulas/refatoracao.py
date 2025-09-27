
def calcular_media(nota_a, nota_b):
    return (nota_a + nota_b) / 2

def verificar_aprovacao(media_a):
    # if media_a >= 6:
    #     return 'Aprovado'
    # else:
    #     return 'Reprovado'
    return 'Aprovado' if media_a >= 6 else 'Reprovado'

nota1 = 7
nota2 = 4
# media1 = (nota1 + nota2) / 2
media1 = calcular_media(nota1, nota2)

# if media1 >= 6:
#     print('Aprovado')
# else:
#     print('Reprovado')
# print(verificar_aprovacao(media1))
print(f'Status: {verificar_aprovacao(media1)}. Média: {media1}')


nota3 = 7
nota4 = 6
# media2 = (nota3 - nota4) / 2
# media2 = (nota3 + nota4) / 2
media2 = calcular_media(nota3, nota4)

# if media2 > 6:
# if media2 >= 6:
#     print('Aprovado')
# else:
#     print('Reprovado')
# print(verificar_aprovacao(media2))
print(f'Status: {verificar_aprovacao(media2)}. Média: {media2}')