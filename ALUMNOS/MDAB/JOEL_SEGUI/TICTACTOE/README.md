# Ejercicio de Programación: Tic Tac Toe con PostgreSQL

![Tic Tac Toe](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJd6tIrqyz0C3Quc9ohvlqK6DhvTXO2gJKQA&s)

Este ejercicio consiste en corregir diferentes errores en un juego de Tic Tac Toe que guarda los resultados en una base de datos PostgreSQL. 

El objetivo de este ejercicio, es ir resolviendo problemas para que el juego funcione correctamente.

## Instrucciones

FASE 1: Consigue que el juego funcione correctamente.

Podemos considerar que has conseguido esta fase si:

- El juego se ejecuta correctamente y ves el siguiente mensaje:

```
1 | 2 | 3
-----
4 | 5 | 6
-----
7 | 8 | 9
-----
Enter the number of the cell (1-9): 1
Error: La base de datos no está lista, si estás en Fase 1 no es un problema
```

FASE 2: Pasemos a construir la imagen de Docker

Si has conseguido la fase anterior, ahora toca construir la imagen de Docker. Para ello, debes poder construir la imagen individualmente con el siguiente comando:

```
docker build -t tictactoe .
```

FASE 3: Levantemos Base de datos y PGAdmin

Si has conseguido la fase anterior, ahora toca levantar la base de datos y PGAdmin. Para ello, debes poder levantar los servicios con el siguiente comando:

```
docker-compose up -d
```

Una vez todo esté levantado y puedas acceder a pgAdmin, deberías ejectuar el siguiente commando para arrancar el juego:

```
docker-compose run --rm tictactoe
```

¿Se ha levantado todo correctamente? ¿Se guardan los movimientos en la base de datos? Si es así, ¡enhorabuena! Has completado el ejercicio, si no es así, sigue intentándolo... te has dejado algo por arreglar.



