letter = "A"
for y in range(FILAS - 1):
    for _ in range(COLUMNAS):
        print("+--", end="")
    print("+")
    print(f'|{letter}|', end="")
    for x in range(COLUMNAS):
        celda = board[y][x]
        valor_real = celda
        print(f'{valor_real} ', end="")
    letter = chr(ord(letter) + 1)
    print(
        "|",
    )
for _ in range(COLUMNAS + 1):
    print("+--", end="")
print("+")
print("| ", end="")
for x in range(COLUMNAS):
    print(f'|{x + 1} ', end="")
print("|")
for _ in range(COLUMNAS + 1):
    print("+--", end="")
print("+")
print("|", end="")
