# AHORCADO

## Descripción

Todos habréis jugado alguna vez al ahorcado con papel y lápiz. En este caso, vamos a hacer una versión digital del juego. El juego consiste en adivinar una palabra, letra a letra. Si se falla una letra, se dibuja una parte del cuerpo del ahorcado. Si se adivina la palabra antes de que se complete el dibujo, se gana. Si se completa el dibujo, se pierde.

Para darle algo de emoción vamos a elegir una serie de palabras para todos que nos servirán para comparar nuestros resultados. A continuación, se muestra una lista de palabras que se pueden utilizar:

**Lista de palabras:**

- MURCIELAGO
- VIAJE
- EVADIR
- ZAPATO
- CIELO
- RECREO
- PIZARRA
- MATEMATICAS
- PROGRAMACION
- ORDENADOR

Y a continuación las normás del juego:

- El juego debe funcionar de manera autónoma, es decir, no se puede pedir al usuario que introduzca las letras, ni la siguiente palabra a adivinar.
- No se tendrán en cuenta las tildes.
- El juego no contará con el concepto de vidas, es decir debe continuar hasta adivinar la palabra contando el número de intentos.
- El juego debe mostrar el número de intentos utilizado en cada palabra y una suma total de los intentos utilizados en todas las palabras.

## Requisitos

El objetivo de este juego es servir de resumen de los conocimientos adquiridos en el curso. Por tanto, se deben utilizar todos los conceptos aprendidos en el curso. En concreto, se deben utilizar los siguientes conceptos que organizaremos como fases:

1. **Fase 1: Codificación**

Durante esta fase el objetivo es codificar la lógica del juego. Por lo que utilizaremos los conocimientos adquiridos de python. El objetivo de esta fase es conseguir un algoritmo que por fuerza bruta (es decir, probando todas las letras, en el orden del abecedario) adivine las palabras.

En esta fase también crearemos la rama de trabajo en el repositorio de github para entregar el código. Esta rama se llamará `e2e-ahorcado-XXXX` siendo XXX vuestro id de usuario en github.

Al finalizar esta fase, deberéis tener un programa con las siguientes características:

- Lea las palabras de un fichero de texto, una por línea
- Busque cada palabra y retorne los intentos necesarios para adivinarla
- Se pueda ejecutar con el siguiente comando: `python ahorcado.py palabras.txt`

Si has completado esta fase podemos decir que Github y Python son tus amigos.

2. **Fase 2: Automatización**

Si habéis completado la fase anterior ahora toca automatizar el proceso usando docker. Para ello, debéis crear un `Dockerfile` que contenga todo lo necesario para ejecutar el programa. 

Al finalizar esta fase, deberéis tener un programa con las siguientes características:

- Se pueda construir la imagen de docker con el siguiente comando: `docker build -t ahorcado .`
- Se pueda ejecutar el contenedor con el siguiente comando: `docker run ahorcado`

Si has completado esta fase podemos decir que Docker es tu amigo.

**EXTRA**: ¿Podrías hacer que palabras.txt sea un parámetro del contenedor?

3. **Fase 3: Almacenaje**

Si has completado la fase anterior ahora toca almacenar el resultado en una base de datos. Para ello, debéis crear un `docker-compose.yml` que contenga un servicio de base de datos y otro con el servicio de la aplicación.

El objetivo de esa fase es que alimentéis una tabla de la base de datos con los intentos necesarios para adivinar las palabras. La tabla debe tener la siguiente estructura:

- palabra: palabra a adivinar
- letras_acertadas: letras utilizadas para adivinar la palabra
- letras_falladas: letras falladas en el intento
- intentos: número de intentos necesarios para adivinar la palabra
- tiempo: tiempo actual

El resultado final debe ser similar a la siguiente tabla:

| palabra | letras_acertadas | letras_falladas | intentos | tiempo |
|---------|------------------|-----------------|----------|--------|
| MURCIELAGO | A |  | 1 | 2021-01-01 12:00:00 |
| MURCIELAGO | A | B | 2 | 2021-01-01 12:01:00 |
| MURCIELAGO | AC | B | 3 | 2021-01-01 12:02:00 |
| MURCIELAGO | AC | BD | 4 | 2021-01-01 12:04:00 |
| MURCIELAGO | ACE | BD | 5 | 2021-01-01 12:05:00 |

Al finalizar esta fase, deberéis tener un programa con las siguientes características:

- Se pueda construir la imagen de docker con el siguiente comando: `docker-compose up -d`
- Al arrancar el contenedor se cree la tabla en la base de datos
- Se alimente la tabla con los intentos necesarios para adivinar las palabras

Si has completado esta fase podemos decir que Docker y MySQL son tus amigos.

4. **Fase 4: Optimización**

Si has completado la fase anterior ahora toca optimizar el proceso. Para ello debéis probar otras estraegias para adivinar las palabras. 

Por ejemplo, 

- ¿Podrías ordenar el array de letras de una manera que adivines la palabra en menos intentos?
- ¿Podrías predecir si todas las letras son igual de probables basándose en lo que ya sabes?
