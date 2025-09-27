notas = [9, 9.5, 10, 9.8]

print(notas)

media = 0
qt_notas = len(notas)

for nota in notas:
    media += nota

media /= t_notas

print(f'A média é: {media}')