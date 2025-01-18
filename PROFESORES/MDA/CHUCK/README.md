![Chuck Norris Logo](https://api.chucknorris.io/img/chucknorris_logo_coloured_small@2x.png)

Ha llegado el momento de sacar la artillería pesada para este ejercicio. Chuck Norris es el único que puede hacer que un hola mundo sea un hola mundo.

Para este ejericio tenemos que conseguir hacer feliz a Chuck norris y para ello debemos de saber exactamente que es lo que le hace feliz. Para ello, debemos de hacer una petición a la API de Chuck Norris y obtener un chiste aleatorio y saber cuáles son las palabras que más le hacen gracia.

Fase 1: NIFI

Para ello, vamos a utilizar Nifi para hacer una petición a la API de Chuck Norris y obtener un chiste aleatorio. Para ello, vamos a utilizar el siguiente endpoint:

https://api.chucknorris.io/jokes/random

Con el resultado debemos navegar al chiste. Este chiste se deben guardar en una base de NOSQL que debemos crear para este ejercicio.

````
{
  "categories": [],
  "created_at": "2020-01-05 13:42:18.823766",
  "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
  "id": "x5whniztqdancooc9w-ggg",
  "updated_at": "2020-01-05 13:42:18.823766",
  "url": "https://api.chucknorris.io/jokes/x5whniztqdancooc9w-ggg",
  "value": "Chuck Norris invented the bolt-action rifle, liquor, sexual intercourse, and football-- in that order."
}
````

FASE 2: PROCESADO EN NIFI con un Script de python

Una vez los datos están en NOSQL, debemos generar una ETL que lea el json y lo guarde en una base de datos SQL donde cada palabra sea una fila y actualicemos el número de apariciones por palabra.

FASE 3: DEBEZIUM

Si hemos llegado hasta aquí, es que hemos conseguido hacer feliz a Chuck Norris. Pero ahora, Chuck Norris quiere que esos datos se repliquen de manera automática en otra base de datos distinta.

- Pregunta: ¿Podemos llegar a las bases de datos de vuestros compañeros?

FASE 4: DASHBOARDS

Chuck Norris quiere que le hagamos un dashboard donde pueda ver en tiempo real las palabras que más le hacen gracia. Para ello, debemos de hacer un dashboard en la herramienta que queramos donde se muestre en tiempo real las palabras que más le hacen gracia.