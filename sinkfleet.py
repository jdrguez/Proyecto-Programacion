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
PLAYER = input("Introduzca su nombre: ")
size = len(board)
score = 0
item = UNEXPLORED
second_board = [[item for _ in range(size)]for _ in range(size)]
touched_ships = []
letter = "A"
letter_pos = 0
turn = 0

while True:
    turn += 1
    for row in second_board:
        print(f"{letter} ", end=" ")
        if letter == 'J':
            letter = 'A'
            pass
        else:
            letter = chr(ord(letter) % 65 + 66)
        for item in row:
            print(f'[{item:2s}]', end="")
        print()

    print("  ", end="")
    for num in range(1, size + 1):
        print(f' {num:3d} ', end="")
    print()


    print(f'Este es el mar del jugador {PLAYER}')


    print(f'Es necesario que pongas tus coordenadas para disparar {PLAYER}')

    # pedir las coordenadas

    letter_row = input("Ingresa la letra de la fila y como aparece en el tablero: ").upper()
    if len(letter_row) != 1:
        print('ERROR: mas de un elemento')
        continue
    
    order_letter = ord(letter_row) - 65
    
    order_number = int(input("Ingresa el numero: ")) - 1
    if order_number > 10:
        print('ERROR: Numero incorrecto')
        continue
    
    # Validar las posiciones para los colores
        
    if board[order_letter][order_number] == EMPTY:
            advise = "AGUA"
            score -= 1
            second_board[order_letter][order_number] = WATER
    elif board[order_letter][order_number] == UNEXPLORED:
            advise = "AGUA"
            score -= 1
            second_board[order_letter][order_number] = WATER
    elif board[order_letter][order_number] == WATER:
            advise= "Ya habías disparado a esa posición. AGUA"
            score -= 1
    else:
            touched_ships.append(board[order_letter][order_number])
            ship_id = board[order_letter][order_number]
            ship_size = int(ship_id[:-1])
            if touched_ships.count(ship_id) == ship_size:
                advise = f"TOCADO Y HUNDIDO EL BARCO {ship_id}"
                score += 4 * ship_size  
                second_board[order_letter][order_number] = SUNKEN
                touched_ships.remove(ship_id)
            else:
                advise = "TOCADO"
                score += 2 * ship_size
                second_board[order_letter][order_number] = TOUCHED
    
    
    show_board(board)
    print(board)
    print(f'{PLAYER.capitalize()} en su turno número {turn}, ha hecho {advise}. Teniendo un total de {score} puntos')
