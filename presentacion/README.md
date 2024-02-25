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
<img src="https://64.media.tumblr.com/0144277060397fe1037c9ac5934a4bb2/2d3e6da05b03f234-a6/s1280x1920/dd144a6feaaeaca6f544a4810ca74c5c4a43f54f.pnj" width="480" height="380"/>
<h4><li>Aventurero:</li></h4>
Joven aventurero que surcó los mares en busca de aventuras y nuevos horizontes. Su inteligencia le ha salvado de todos los contratiempos que el océano le ha puesto delante.
<p>El aventurero corresponde al modo de juego normal</p>
<img src="https://64.media.tumblr.com/97b0cbf7a853e36da4a414fd13d49f3f/76e32b6121a8fc41-ac/s1280x1920/e8375494980127a8e65b1066ea1bb74585652164.pnj" width="480" height="380"/>
<h4><li>Asesino:</li></h4>
Robot mitad ladron, mitad asesinó a sangre fría, le gusta rebanar cabezas a los que se le cruzan en su camino hacia su botín.
<p>Si hundes un barco o lo tocas, se te recompensará con el doble de puntos correspondientes. Pero si fallas, se te quitará el doble también.
</p>
