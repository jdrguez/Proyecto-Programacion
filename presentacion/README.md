<center><h1> Hundir la flota. </h1></center>
<h2>Introducción y normas.</h2>
<p>Hundir la flota (Battleship) es un popular juego de mesa en el que dos jugadores posicionan sus barcos en un tablero de coordenadas y el rival debe adivinar la posicion de los barcos y acabar con ellos. Nuestro objetivo en este proyecto es recrear este juego con Python y hacerlo jugable a traves de la terminal del ordenador, en este caso tu rival es la propia terminal y debes hundir sus barcos.
<p>
Para ello hemos aplicado las normas del juego original mas algun añadido que explicaremos mas adelante para hacerlo mas interesante ;) .
</p>
<p>Comencemos explicando los distintos tipos de naves que existen:</p>
<h3>Tipos de barcos.</h3>
<p>
<ul>
<li>1 portaaviones que ocupa 5 casillas.</li>
<li>1 acorazado que ocupa 4 casillas.</li>
<li>2 submarinos que ocupan 3 casillas.</li>
<li>1 destructor que ocupa 2 casillas.</li>
</ul>
En este caso los barcos serán colocados aleatoriamente en el tablero de nuestro rival.
</p>
<h2>Desarrollo del juego</h2>

<p>Antes de comenzar el enfrentamiento debemos preparar unos ajustes para que la batalla se adapte mas a las necesidades de cada jugador.
</p>
<p>Primero debemos seleccionar entre dos modos de juego:</p>

<h4><li>Modo Clásico:</li></h4>

<h4><li>Modo Hardcore:</li></h4>

<p>Una vez seleccionado el modo seleccionaremos la personalidad que mas nos defina entre los siguientes personajes. Ten encuenta que cada personaje añade una característica distinta al modo de juego.</p>
<h3>Personajes</h3>
<h4>Usurpador:</h4>
<p><img src="https://64.media.tumblr.com/0144277060397fe1037c9ac5934a4bb2/2d3e6da05b03f234-a6/s1280x1920/dd144a6feaaeaca6f544a4810ca74c5c4a43f54f.pnj" width="150" height="150" align="left"/>
Famoso contrabandista del Pacífico Sur especializado en robos de alta mar. La agilidad y su sangre fría son la clave del éxito en sus trabajos, aunque a veces peca de ser impulsivo.</p>
<p>Este personaje te dará el doble de puntuación al tocar un barco, pero al hundirlo se te restaran 10 puntos.</p>

<h4>Aventurero:</h4>
<img src="https://64.media.tumblr.com/97b0cbf7a853e36da4a414fd13d49f3f/76e32b6121a8fc41-ac/s1280x1920/e8375494980127a8e65b1066ea1bb74585652164.pnj" width="200" height="200"align="left"/>
<p>Joven aventurero que surcó los mares en busca de aventuras y nuevos horizontes. Su inteligencia le ha salvado de todos los contratiempos que el océano le ha puesto delante.</p>
<p>El aventurero corresponde al modo de juego normal</p>

<h4><li>Asesino:</li></h4>
<img src="https://64.media.tumblr.com/ecc9e9dbfe09843f7d2f8e71e7046bce/f3e571e6c141ace6-f8/s1280x1920/e692b9407b02e5f935f05ca3c52e9149666fb6dd.pnj" width="200" height="200"align="left"/>
Robot mitad ladron, mitad asesinó a sangre fría, le gusta rebanar cabezas a los que se le cruzan en su camino hacia su botín.
<p>Si hundes un barco o lo tocas, se te recompensará con el doble de puntos correspondientes. Pero si fallas, se te quitará el doble también.
</p>



<h2>Explicación del código:</h2>
<img src="images/Selección_001.png">
En este fragmento del codigo es donde esta representada la elección de la dificultad cuando inicias la partida

---

<img src="images/Selección_002.png">
En este fragmento de codigo es donde se consigue crear el menu de eleccion de personalidad donde cada una personalizara la partida de diversas formas

---

<img src="images/Selección_003.png">

En este pequeño fragmento de codigo tenemos un EASTER EGG dedicado a la palabra favorita de nuestro profe Sergio, el cual se introducira en la seleccion de personalidades poniendo 'matraca' se mostrara un tablero con las posiciones de los barcos.

---

<img src="images/Selección_004.png">

En este fragmento de codigo esta representado un añadido a la idea original que sergio nos dio del juego hundir la flota, un modo hardcore el cual seria tener una cantidad limitada de disparos para hundir los barcos, si se acabaran los intentos saltaria la pantalla de derrota

---

<img src="images/Selección_005.png">

En este fragmento de codigo esta representado laforma de pedir las cordenadas que el jugador ponga, tambien hay una forma de salir del juego en caso de que no quisiera continuar, pulsando la Q

---

<img src="images/Selección_006.png">
<img src="images/Selección_007.png">

En estre fragmento de codigo esta representada la forma de validar las posiciones de los colores, sumar o restar los puntos, asi como un aviso por si decides disparar a la misma casilla, se le dara un mensaje al jugador de que esa casilla ya ha sido disparada

---

<img src="images/Selección_008.png">
 
 Por último en este fragmento de codigo se representa la forma de igualar a 0 los puntos si estos baja por debajo de cero

---

Ademas, añadimos imagenes al juego para hacerlo mas colorido, como texto en ascci para que se viera mejor  

