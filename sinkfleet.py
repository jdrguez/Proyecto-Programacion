import random
import string

EMPTY = ''

UNEXPLORED = '⬛'
WATER = '🟦'
TOUCHED = '🟧'
SUNKEN = '🟥'


def generate_board(
    size: int = 10,
    ships: tuple[tuple[int, int]] = ((5, 1), (4, 1), (3, 2), (2, 1)),
) -> list[list[str]]:
    board = [[EMPTY for _ in range(size)] for _ in range(size)]
    for sheep_size, num_ships in ships:
        placed_ships = 0
        while placed_ships < num_ships:
            sheep_id = f'{sheep_size}{string.ascii_uppercase[placed_ships]}'
            row, col = random.randint(0, size), random.randint(0, size)
            step = random.choice((-1, 1))
            row_step, col_step = (step, 0) if random.randint(0, 1) else (0, step)
            breadcrumbs = []
            for _ in range(sheep_size):
                try:
                    if not (0 <= row < size and 0 <= col < size):
                        raise IndexError()
                    if board[row][col] == EMPTY:
                        board[row][col] = sheep_id
                        breadcrumbs.append((row, col))
                    else:
                        raise IndexError()
                    row += row_step
                    col += col_step
                except IndexError:
                    # reset board
                    for bc in breadcrumbs:
                        board[bc[0]][bc[1]] = EMPTY
                    break
            else:
                placed_ships += 1

    return board


def show_board(board: list[list[str]]) -> None:
    for row in board:
        for item in row:
            print(f'[{item:2s}]', end='')
        print()


# TU CÓDIGO DESDE AQUÍ HACIA ABAJO
# ↓↓↓↓↓↓↓↓↓

board = generate_board()



FILAS = 10
COLUMNAS = 10
JUGADOR = input("Introduzca su nombre")

#Imprimir el tablero
board = board
letter = "A"

for row in range(FILAS):
    print(f"{letter} ", end=" ")
    letter = chr(ord(letter)+1)
    for colum in range(COLUMNAS):
        board[row].append(UNEXPLORED)
        print(f'[{UNEXPLORED:2s}]', end="")
    print()

print("  ", end="")
for num in range(1, COLUMNAS + 1):
    print(f' {num:3d} ', end="")
print()



print(f'Este es el mar del jugador {JUGADOR}')


print(f'Es necesario que pongas tus coordenadas para disparar {JUGADOR}')

# Este es el ciclo infinito para pedir las coordenadas
limits_board = colum >= 0 and colum <= COLUMNAS - 1 and row >= 0 and row <= FILAS - 1


while True:
    letter_row = input("Ingresa la letra de la fila y como aparece en el tablero: ").upper()
    y = letter_row
    if len(letter_row) != 1:
        print("Debes ingresar únicamente una letra")
        continue
    y = ord(letter_row) - 65
    if colum >= 0 and colum <= COLUMNAS - 1 and row >= 0 and row <= FILAS - 1:
        break
    else:
        print("Fila inválida")

while True:
    letter_colum = int(input("Ingresa el numero de la columna: "))
    x = letter_colum
    if x >= 0 and x <= COLUMNAS - 1 and y >= 0 and y <= FILAS - 1:
        x = x - 1
        break
    else:
        print("Columna inválida")

