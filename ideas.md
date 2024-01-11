# Ideas sobre el bucle de repetición
- Probablemente un bucle que repita el juego todo el rato. Que pida los inputs del usuario y que imprima las puntuaciones.
- Añadir la suma y la resta de puntuación según lo que haga el usuario
- Hay que pedir dos datos: una letra y un numero. La letra representará el eje x y el número el eje y
- Según lo que pida el usuario se mostrará una cosa u otra.
- Añadir una condición que señala a la persona que ya a usado unos valores antes.
- Añadir una condición que señale a la persona que solo puede usar un valor en letra (las del tablero) y número (del tablero)
- Se puede poner intentos.
- Se puede intentar hacer un modo harcode con disparos limitados. 25 o lo que sea.

# Ideas sobre el algoritmo para comprobar el tablero para jugar.
- Probablemente sea un bucle aninado que itere las listas en horinzontal y vertical.
- Dentro de este mirar si en la posición dada hay un barco o no. Para poner el agua.
- Si se hynde un barco evitar que se use esa posición en el recorrido.
- Poner la condición que rompa el bucle de repetición cuando no hayan barcos.

# Ideas para cambiar los colores del tablero.
- Podríamos usar un match case para los colores.
- Si el barco esta tocado tiene que estar en naranja.
- Si se hunde el barco hay que cambiar todo el color naranja por color rojo.
- Poner de color azul si es agua.

# Ideas para la puntuación.
- Nunca puede bajar a mas de cero. Si la puntuación es cero no quita.
- Ver cuanto de puntuación vamos a dar.
- Segun la cantidad de intentos incrementar lo que quita el agua.
