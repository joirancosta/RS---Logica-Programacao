"""
Quantos números de 4 dígitos eu posso formar com números de 0 a 9
_  _  _  _
10 10 10 10
Combinatória: 10 * 10 * 10 * 10 = 10000
"""
cont = 0

for n_01 in range(10):
    for n_02 in range(10):
        for n_03 in range(10):
            for n_04 in range(10):
                cont += 1

print(cont)

"""
_  _ _ _
10 9 8 7
Permutação: 10 * 9 * 8 * 7 = 5040
"""
cont = 0

for n_01 in range(10):
    for n_02 in range(10):
        if n_02 == n_01:
            continue
        for n_03 in range(10):
            if n_03 == n_02 or n_03 == n_01:
                continue
            for n_04 in range(10):
                if n_04 == n_03 or n_04 == n_02 or n_04 == n_01:
                    continue
                cont += 1

print(cont)