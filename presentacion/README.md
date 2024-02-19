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
<h4><li>Usurpador:</li></h4>
Famoso contrabandista del Pacífico Sur especializado en robos de alta mar. La agilidad y su sangre fría son la clave del éxito en sus trabajos, aunque a veces peca de ser impulsivo.
<p>Este personaje te dará el doble de puntuación al tocar un barco, pero al hundirlo se te restaran 10 puntos.</p>

<h4><li>Aventurero:</li></h4>
Joven aventurero que surcó los mares en busca de aventuras y nuevos horizontes. Su inteligencia le ha salvado de todos los contratiempos que el océano le ha puesto delante.
<p>El aventurero corresponde al modo de juego normal, ni se restan ni se suman puntos extras.</p>

<h4><li>Asesino:</li></h4>
Robot mitad ladron, mitad asesinó a sangre fría, le gusta rebanar cabezas a los que se le cruzan en su camino hacia su botín.
<p>Si hundes un barco o lo tocas, se te recompensará con el doble de puntos correspondientes. Pero si fallas, se te quitará el doble también.
</p>