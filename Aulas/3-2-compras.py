import os

os.system("cls")

produto = 'Arroz'
preco_unitario = 5.79
quantidade = 3

valor_total = preco_unitario * quantidade

if quantidade > 2:
    valor_total *= 0.9

print(f'Produto: {produto}')
print(f'Quantidade: {quantidade}')
print(f'Valor total: {valor_total:.2f}')