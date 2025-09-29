nomes = [
    'João',
    'Antonio',
    'Maria',
    'Emengarda',
    'Ana',
    'Anacleto',
    'Bianca',
    'José',
    'Adão',
    'Josi',
]

tabela = {}

for nome in nomes:
    qtd = len(nome)
    if qtd not in tabela:
        tabela[qtd] = []
    tabela[qtd].append(nome)

print(tabela)