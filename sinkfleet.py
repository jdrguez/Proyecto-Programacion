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
HARCORE_TURNS = 35
END_GAME_FAILED = False
board = generate_board()
PLAYER = input("Introduzca su nombre: ")
SIZE = len(board)
RULES = (f'''
Reglas:
- El jugador tiene una cuadrícula de 10x10 en la que, de manera aleatoria, se colocan barcos de diferentes longitudes sin que se superpongan ni toquen los bordes.
- El jugador tiene que intentar adivinar la ubicación de los barcos diciendo las coordenadas de un punto en la cuadrícula.
- Si el punto no contiene ningun barco, se marcará con un icono de {WATER} en la cuadrícula.
- Si el punto adivinado contiene una parte de un barco del oponente, se marcará ese punto en su cuadrícula con un icono {TOUCHED} .
- Si todas las partes de un barco han sido alcanzadas, se mostrará hundio con un icono {SUNKEN}.
- El juego continúa hasta que todos los barcos hayan sido hundidos.
- El jugador cuando haya hundido todos los barcos gana la partida.
''')

#Pasivas de los personajes
USURPER = 2
ADVENTURE = 0
ASSASIN = 2


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

print(r'''
      
░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░░░░░░░░╠▓░░░░░░░░░░░░░░░▀▄▀░░░░░░░
░░░░▄▀▀▄█▄░▀▄░░▓╬▓▓▓░░░░░░░░▓╬▓▓▓░░░░░░▀▄▀░░░░░░░░░░░░░░
░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░░░░░░▓▓╬▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░
░░░░░░▐▌░░░░▀▀███████▀░░░▀▀███████▀░░░░░░░░░░░░░░░░░░░░░
▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
'''
)

print(RULES)

wild_card= input('Pulsa cualquier botón para continuar tu aventura:')

# Decisión de dificultad
while True:
    difficulty_decision = input(
        '''Antes de empezar tu aventura, debes decidir que modo de juego tomar.
            Te doy las siguientes opciones:
            1. Modo Fácil.
            2. Modo Harcore.
            Dime cual será tu tortura:   '''
    )
    print()
    match difficulty_decision:
        case '1':
            DEFAULT
            print('Te gusta disfrutar de una aventura sencilla y tener el control.')
            break
        case '2':
            HARCORE = True
            print('Ah sí, eres valiente. Recuerda el cementerio está lleno de valientes.')
            break
        case _:
            print('Introduzca un número válido:  ')

print()
print('Ya has decidio como jugar, ahora te falta que personalidad vas a tener,')
print('Las personalidades son las siguientes: ')
print()
print(
    r'''
▒▒▒▒▒▒▐███████▌
▒▒▒▒▒▒▐░▀░▀░▀░▌
▒▒▒▒▒▒▐▄▄▄▄▄▄▄▌
▄▀▀▀█▒▐░▀▀▄▀▀░▌▒█▀▀▀▄
▌▌▌▌▐▒▄▌░▄▄▄░▐▄▒▌▐▐▐▐

Usurpador:
Famoso contrabandista del Pacífico Sur especializado en robos de alta mar. La agilidad y su sangre fría son la clave del éxito en sus trabajos, aunque a veces peca de ser impulsivo. 
Pasiva:
Se te dará el doble de puntos por tocar a un barco, pero al hundir el barco se te quitarán 10 puntos.
'''
)

input('Pulsa cualquier botón para mostrar la siguiente personalidad: ')

print(
    r'''
░░░▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄░░░
░░░█▒▒░░░░░░░░░▒▒█░░░
────█░░█░░░░░█░░█░░░░
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█

Aventurero:
Joven aventurero que surcó los mares en busca de aventuras y nuevos horizontes. Su inteligencia le ha salvado de todos los contratiempos que el océano le ha puesto delante.
Pasiva: 
No se te quitarán nunca puntos, pero tampoco se te darán puntos extras.
'''
)

input('Pulsa cualquier botón para mostrar la siguiente personalidad: ')

print(
    r'''
░░░░░░░▄█▄▄▄█▄░░░░
▄▀░░░░▄▌─▄─▄─▐▄░░░░▀▄
█▄▄█░░▀▌─▀─▀─▐▀░░█▄▄█
░▐▌░░░░▀▀███▀▀░░░░▐▌
████░▄█████████▄░████

Asesino:
Mitad robot ladron, mitad asesinó a sangre fría, le gusta rebanar cabezas a los que se le cruzan en su camino hacia su botín.
Pasiva: 
Si hundes un barco o lo tocas, se te recompensará con el doble de puntos correspondientes. Pero si fallas, se te quitará el doble también.
'''
)

wild_card

while True:
    print()
    personality = input('Elige tu personalidad entre estas leyendas del mar: ').lower()

    match personality:
        case 'usurpador':
            recomend = 'tener sagre fría y agilidad.'
            break
        case 'aventurero':
            recomend = 'tener buena orientación y buena suerte.'
            break
        case 'asesino':
            recomend = 'tener sed de sangre y bueno en combate.'
            break
        case _:
            print('ERROR: No has elegido personalidad')

print()
print(f'Has elegido {personality.capitalize()}. Buena decisión, esta se basa en {recomend}')
print()
print(r'''
██████╗░██╗░░░██╗███████╗███╗░░██╗░█████╗░  ░██████╗██╗░░░██╗███████╗██████╗░████████╗███████╗  ██╗██╗
██╔══██╗██║░░░██║██╔════╝████╗░██║██╔══██╗  ██╔════╝██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝  ██║██║
██████╦╝██║░░░██║█████╗░░██╔██╗██║███████║  ╚█████╗░██║░░░██║█████╗░░██████╔╝░░░██║░░░█████╗░░  ██║██║
██╔══██╗██║░░░██║██╔══╝░░██║╚████║██╔══██║  ░╚═══██╗██║░░░██║██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░  ╚═╝╚═╝
██████╦╝╚██████╔╝███████╗██║░╚███║██║░░██║  ██████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░███████╗  ██╗██╗
╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝  ╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝╚═╝
''')

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

    
    # pedir las coordenadas
    while True:
        player_option = input(
        'Ingresa tus coordenadas (A1,C3,etc...)(Si quieres abandonar pulsa Q): '
        ).upper()
        
        print()

        if player_option == 'Q':
            print(f'Has abandonado. Tu puntuación ha sido de {score}')
            break
        elif len(player_option) < 1:
            print('Te falta una coordenadas')
        elif len(player_option) > 3:
            print('ERROR: mas de un elemento')
        else:
            if player_option[1:].isalpha():
                print('ERROR: Has introducido dos letras')
            else:
                letter_row = player_option[:1]
                order_number = int(player_option[1:]) - 1
                break

    if player_option == 'Q':
        break

    order_letter = ord(letter_row) - 65

    # Validar las posiciones para los colores

    if board[order_letter][order_number] == EMPTY:
        advise = "AGUA"
        if personality == 'aventurero':
            score -= ADVENTURE
        elif personality == 'asesino':
            score -= 10 * ASSASIN
        else:
            score -= 10
        second_board[order_letter][order_number] = WATER
    elif board[order_letter][order_number] == UNEXPLORED:
        advise = "AGUA"
        if personality == 'aventurero':
            score -= ADVENTURE
        else:
            score -= 10
        second_board[order_letter][order_number] = WATER
    elif board[order_letter][order_number] == WATER:
        advise = "Ya habías disparado a esa posición. AGUA"
        if personality == 'aventurero':
            score -= ADVENTURE
        elif personality == 'asesino':
            score -= 10 * ASSASIN
        else:
            score -= 10
    elif second_board[order_letter][order_number] == TOUCHED:
        advise = 'Ya has disparado ahí'
        if personality == 'aventurero':
            score -= ADVENTURE
        elif personality == 'asesino':
            score -= 20 * ASSASIN
        else:
            score -= 20
    elif second_board[order_letter][order_number] == SUNKEN:
        advise = 'El barco ya esta hundido'
        if personality == 'aventurero':
            score -= ADVENTURE
        elif personality == 'asesino':
            score -= 40 * ASSASIN
        else:
            score -= 40
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
                        if personality == 'asesino':
                            score += 4 * ship_size * ASSASIN
                        elif personality == 'usurpador':
                            score += 4 * ship_size - 10
                        else:
                            score += 4 * ship_size
                        second_board[i_pos][j_pos] = SUNKEN
                        second_board[order_letter][order_number] = SUNKEN
                        touched_ships.remove(ship_id)

        else:
            advise = "TOCADO"
            if personality == 'usurpador':
                score += 2 * ship_size * USURPER
            elif personality == 'asesino':
                score += 2 * ship_size *  ASSASIN
            else:
                score += 2 * ship_size
            second_board[order_letter][order_number] = TOUCHED

    # Validar si el score baja igualarlo a 0
    if score < 0:
        score = 0

    print(f'''{PLAYER.capitalize()} en su turno número {turn}, ha hecho {advise}. ''')
    print(f'Teniendo un total de {score} puntos.')
   

    if TOTAL_SHIPS == 0:
        end_game = False

    print(f'''Te quedan {TOTAL_SHIPS} barcos por hundir. Continua tu búsqueda ''')
    print()


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
    print(r'''_________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________________
            _____________ ¶¶¶________________¶¶¶_______________
            ___________¶¶______________________¶¶¶¶___________
            _________¶¶¶__________________________¶¶¶_________
            _______¶¶¶___________________¶¶¶¶_______¶¶________
            _¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__
            __¶¶¶¶____¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶___
            ___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶____
            __¶___¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶__¶__
            _¶¶___¶¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶__¶¶__
            ¶______¶¶¶¶¶¶¶¶_____¶¶¶___¶¶¶¶¶¶¶¶¶___¶¶¶¶¶____¶__
            ¶__________¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶__¶______¶¶
            ¶_______________________________________________¶¶
            ¶________¶¶_____________________________________¶¶
            ¶______¶¶¶¶_________________________¶¶¶¶________¶¶
            ¶_____¶__¶¶_________________________¶¶¶¶________¶¶
            ¶_________¶¶¶______________________¶¶___________¶¶
            ¶___________¶¶¶__________________¶¶¶____________¶¶
            ¶¶____________¶¶¶¶____________¶¶¶¶_____________¶__
            _¶¶______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________¶__
            __¶___________________________________________¶¶__
            ___¶¶________________________________________¶¶___
            ____¶¶______________________________________¶¶____
            _____¶¶___________________________________¶¶______
            _______¶¶_______________________________¶¶¶_______
            _________¶¶___________________________¶¶¶_________
            __________¶¶¶¶_____________________¶¶_____________
            ______________¶¶¶¶_____________¶¶¶¶¶______________
            ___________________¶¶¶¶¶¶¶¶¶¶¶¶___________________
''')


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

    print(
        r'''
        ▄██████████████▄▐█▄▄▄▄█▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ██████▌▄▌▄▐▐▌███▌▀▀██▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ████▄█▌▄▌▄▐▐▌▀███▄▄█▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ▄▄▄▄▄██████████████▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
'''
    )
