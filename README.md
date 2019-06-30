# <img src="https://img.icons8.com/clouds/100/000000/place-marker.png"> G30LOC - Script de geolocalización

### <img src="https://img.icons8.com/flat_round/54/000000/presentation.png">EN DESARROLLO<img src="https://img.icons8.com/color/48/000000/gear.png">

## De qué va esto <img src="https://img.icons8.com/clouds/100/000000/window-settings.png">

Ante la *preocupación* de un posible robo, hurto, extravío, etc. de mi portátil, me vi en la tesitura personal de dar solución a este problema.

« ¿Cómo puedo saber en qué ubicación se encuentra mi portátil sin necesidad de acceder directamente a google map, y por supuesto, dando por hecho que no estaré presente una vez se haya *perdido* mi portátil? » - me pregunté

La idea es *relativamente* sencilla. Supongamos que alguien enciende mi portátil tras haberse extraviado. Ese alguien, como persona cívica, lo primero que haría, o debería hacer, es comunicarselo a la policia. Sin embargo, podemos encontrarnos en la situación de que esto no ocurra.

Lo normal que hará dicha persona, persona que desde este momento llamaremos *Rodrigo* (un nombre cualquiera), será querer acceder al contenido del ordenador.

Sin embargo, se puede dar el caso, como puede ser bastante frecuente, es que exista uno o varios usuarios con contraseña para logearnos. Entiendo que sea lo razonable como medida básica de seguridad. En caso contrario, la tarea será aun mas sencilla pues, dándose el caso de no haber ningun usuario sin contraseña, para el procedimiento deberemos crear una cuenta, llámese *Invitado*, *Casa*, *Sara*, etc.; que no tenga contraseña, de forma que Rodrigo pueda acceder al ordenador sin ningún tipo de dificultad.

​	-  «Pero... ¿Qué sentido tiene darle facilidad a Rodrigo para que pueda entrar a nuestro ordenador?»

​	Sencillo, Rodrigo posee actualmente nuestro ordenador, de igual modo se lo apropiará. Si no le damos facilidad para acceder, lo único que podría pensar es en formatearlo y entonces ahí ya no tendriamos nada que hacer para encontrarlo...

Con la idea clara de que hay que permitir que Rodrigo acceda sin ningún problema, nuestro *usuario sin contraseña* le estará esperando, al inicio de la sesión, con algún tipo de programa o script que geolocalice el portátil y envíe automáticamente un email a alguna cuenta de correo con la ubicación actual. De ahi que sea esencial que no formatee el ordenador y acceda sin problemas.

A groso modo, esta es la idea. Idea que desarrollaremos a continuación.

## Objetivos 🚀

<img src="https://img.icons8.com/color/30/000000/checked-2.png"> Geolocalizar ubicación del portátil.

<img src="https://img.icons8.com/color/30/000000/checked-2.png"> Afinar precisión de ubicación. Ahora ubica con un error de 20 m.

<img src="https://img.icons8.com/color/30/000000/checked-2.png"> Parametrizar variables en un archivo yml (API key, url, etc.).

<img src="https://img.icons8.com/material-outlined/30/000000/unchecked-checkbox.png"> Versionar para Windows.

<img src="https://img.icons8.com/material-outlined/30/000000/unchecked-checkbox.png"> Compilar en un .exe para Windows, de esta forma no se tendria la necesidad de tener instalado python previamente.

<img src="https://img.icons8.com/material-outlined/30/000000/unchecked-checkbox.png"> Configurar que se ejecute al inicio de sesión.

<img src="https://img.icons8.com/material-outlined/30/000000/unchecked-checkbox.png"> Configurar para que envíe un email con fecha, hora y el enlace de la ubicación.

## Autores ✒️

_Se agradece la reseña o cita del autor, de su trabajo y del propio repositorio en los trabajos a los que haya aportado algo de luz y conocimiento._

**Rafael Fernández Ortiz**.- 	:briefcase: [*LinkedIn*](https://www.linkedin.com/in/rafael-fern%C3%A1ndez-ortiz-7a1684171/) - ​<img src="https://img.icons8.com/color/20/000000/open-envelope.png">​ ​[Gmail](mailto:rafaelfernandezortiz@gmail.com) - ​<img src="https://img.icons8.com/color/20/000000/cardboard-box.png">​ [GitHub](https://github.com/rafafrdz) - :bookmark_tabs: [Cv](https://rafafrdz.github.io/) 

## Expresiones de gratitud  y/o sugerencias <img src="https://img.icons8.com/color/48/000000/beer.png">

Siempre es interesante tratar un tema mientras te tomas una cerveza <img src="https://img.icons8.com/color/28/000000/beer.png">