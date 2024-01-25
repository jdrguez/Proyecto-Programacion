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
TOTAL_SHIPS = 5
HARCORE = False
DEFAULT = True
HARCORE_TURNS = 25
END_GAME_FAILED = False
board = generate_board()
PLAYER = input("Introduzca su nombre: ")
SIZE = len(board)
score = 0
item = UNEXPLORED
second_board = [[item for _ in range(SIZE)] for _ in range(SIZE)]
touched_ships = []
letter = "A"
letter_pos = 0
turn = 0

end_game = True

print(
    r''' 
██╗░░██╗██╗░░░██╗███╗░░██╗██████╗░██╗██████╗░  ██╗░░░░░░█████╗░  ███████╗██╗░░░░░░█████╗░████████╗░█████╗░
██║░░██║██║░░░██║████╗░██║██╔══██╗██║██╔══██╗  ██║░░░░░██╔══██╗  ██╔════╝██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗
███████║██║░░░██║██╔██╗██║██║░░██║██║██████╔╝  ██║░░░░░███████║  █████╗░░██║░░░░░██║░░██║░░░██║░░░███████║
██╔══██║██║░░░██║██║╚████║██║░░██║██║██╔══██╗  ██║░░░░░██╔══██║  ██╔══╝░░██║░░░░░██║░░██║░░░██║░░░██╔══██║
██║░░██║╚██████╔╝██║░╚███║██████╔╝██║██║░░██║  ███████╗██║░░██║  ██║░░░░░███████╗╚█████╔╝░░░██║░░░██║░░██║
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝  ╚═╝░░░░░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝'''
)


difficulty_decision = int(
    input(
        '''Antes de empezar tu aventura, debes decidir que modo de juego tomar.
          Te doy las siguientes opciones:
          1. Modo Fácil
          2. Modo Harcore
          Dime cual será tu tortura:   '''
    )
)

match difficulty_decision:
    case 1:
        DEFAULT
        print('Te gusta disfrutar de una aventura sencilla y que tengas el control')
    case 2:
        HARCORE = True
        print('Ah sí, eres valiente. Recuerda el cementerio está lleno de valientes')
    case _:
        input('Introduzca un número válido')


print()
while end_game:
    turn += 1
    for row in second_board:
        print(f"{letter}|", end=" ")
        if letter == 'J':
            letter = 'A'
            pass
        else:
            letter = chr(ord(letter) % 65 + 66)
        for item in row:
            print(f'{item:2s}', end="")
        print()

    print("  ", end="")
    for num in range(1, SIZE + 1):
        print(f' {num} ', end="")
    print()

    if HARCORE:
        if turn > HARCORE_TURNS:
            END_GAME_FAILED = True
            break

    print(f'Este es el mar del jugador {PLAYER}')

    print(f'Es necesario que pongas tus coordenadas para disparar {PLAYER}')

    # pedir las coordenadas
    player_option = input(
        'Ingresa tus coordenadas (A1,C3,etc...)(Si quieres abandonar pulsa Q): '
    ).upper()
    if player_option == 'Q':
        print(f'Has abandonado. Tu puntuación ha sido de {score}')
        break
    if len(player_option) < 2:
        print('Te falta una coordenadas')
        player_option = input('Ingresa tus coordenadas (A1,C3,etc...): ').upper()

    if len(player_option) > 2:
        print('ERROR: mas de un elemento')
        player_option = input('Ingresa tus coordenadas (A1,C3,etc...): ').upper()

    letter_row = player_option[:1]
    order_number = int(player_option[1:]) - 1

    if order_number > 10:
        print('ERROR: Numero incorrecto')
        player_option = input('Ingresa tus coordenadas (A1,C3,etc...): ').upper()

    order_letter = ord(letter_row) - 65

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
        advise = "Ya habías disparado a esa posición. AGUA"
        score -= 1
    else:
        ship_id = board[order_letter][order_number]
        touched_ships.append(ship_id)
        ship_size = int(ship_id[:-1])
        if touched_ships.count(ship_id) == ship_size:
            TOTAL_SHIPS -= 1
            for i_pos, i in enumerate(second_board):
                for j_pos, j in enumerate(i):
                    if j == TOUCHED and ship_id in board[i_pos][j_pos]:
                        advise = f"TOCADO Y HUNDIDO EL BARCO {ship_id}"
                        score += 4 * ship_size
                        second_board[i_pos][j_pos] = SUNKEN
                        second_board[order_letter][order_number] = SUNKEN
                        touched_ships.remove(ship_id)

        else:
            advise = "TOCADO"
            score += 2 * ship_size
            second_board[order_letter][order_number] = TOUCHED

    # Validar si el score baja igualarlo a 0
    if score < 0:
        score = 0

    print(
        f'''{PLAYER.capitalize()} en su turno número {turn}, ha hecho {advise}. Teniendo un total 
        de {score} puntos'''
    )
    if TOTAL_SHIPS == 0:
        end_game = False

if not end_game:
    for row in second_board:
        print(f"{letter}|", end=" ")
        if letter == 'J':
            letter = 'A'
            pass
        else:
            letter = chr(ord(letter) % 65 + 66)
        for item in row:
            print(f'{item:2s}', end="")
        print()

    print("  ", end="")
    for num in range(1, SIZE + 1):
        print(f' {num} ', end="")
    print()
    print(
        r'''
██╗░░██╗░█████╗░░██████╗  ░██████╗░░█████╗░███╗░░██╗░█████╗░██████╗░░█████╗░
██║░░██║██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗
███████║███████║╚█████╗░  ██║░░██╗░███████║██╔██╗██║███████║██║░░██║██║░░██║
██╔══██║██╔══██║░╚═══██╗  ██║░░╚██╗██╔══██║██║╚████║██╔══██║██║░░██║██║░░██║
██║░░██║██║░░██║██████╔╝  ╚██████╔╝██║░░██║██║░╚███║██║░░██║██████╔╝╚█████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░╚════╝░'''
    )


if END_GAME_FAILED:
    print('Tus intentos han acabado, lo siento.')

    print(
        r''' 
██╗░░██╗░█████╗░░██████╗  ██████╗░███████╗██████╗░██████╗░██╗██████╗░░█████╗░
██║░░██║██╔══██╗██╔════╝  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗
███████║███████║╚█████╗░  ██████╔╝█████╗░░██████╔╝██║░░██║██║██║░░██║██║░░██║
██╔══██║██╔══██║░╚═══██╗  ██╔═══╝░██╔══╝░░██╔══██╗██║░░██║██║██║░░██║██║░░██║
██║░░██║██║░░██║██████╔╝  ██║░░░░░███████╗██║░░██║██████╔╝██║██████╔╝╚█████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░░╚════╝░'''
    )
