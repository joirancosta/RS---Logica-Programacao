def contar_caminhos(numero_pedras):
    if numero_pedras <= 1:
        return 1
    return contar_caminhos(numero_pedras - 1) + contar_caminhos(numero_pedras - 2)
    
print(contar_caminhos(2))