
def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 6:
        return 'Aprovado'
    else:
        return 'Reprovado'