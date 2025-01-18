# Ejercicios Evaluables - Curso Python - EDEM_MDA2324

En este archivo Markdown encontraréis los distintos ejercicios que tendréis que realizar tras cada una de las sesiones del curso de Python.

Estos ejercicios serán evaluables y contarán para las notas finales que recibáis por mi parte.

Los ejercicios estarán basados en aquello que hayamos visto durante las clases y podré ayudaros en caso de necesitarlo ;)

## Modo de entrega

Aprovechando que conocéis GIT, la idea es que entreguéis los distintos ejercicios a través de GIT.

Es decir, en la carpeta del repositorio donde tengáis vuestro usuario, deberéis subir la solución del ejercicioo en cuestión y después realizar una Pull Request cuando esté presentable para que pueda revisarla.

El nombre de las carpetas y ejercicios deben dejar claro la sesión y el número de ejercicio. Por ejemplo:

```
├── Curso de Python
    ├── Sesión 1
        ├── Ejercicio 1
        |   ├── Archivo(s).py
        ├── Ejercicio 2
        |   ├── Archivo(s).py
        └── Ejercicio 3
        |   ├── Archivo(s).py
        ├── Etc.
```

En caso de que tengas problemas con los pasos a seguir, no dudes en ponerte en decírmelo para echarte un cable.

# Sesión 1

## Ejercicio 1
1. Crea un archivo Python que muestre por consola "¡Hola, Mundo!"

## Ejercicio 2
2. Ahora modifícalo para que muestre "¡Hola, [Nombre]" donde el nombre es el valor (str) de una variable



# Sesión 2

## Ejercicio
1. Crea una aplicación de consola que calcule los resultados de una inversión. Debe
	1. Pedir por consola una cantidad (numérica) de Inversión
	2. Pedir el % de interés anual
	3. Pedir el número de años que se va a mantener la inversión
	4. Finalmente, calcular la cantidad generada en los años especificados por el usuario

Debería resultar en algo así vía consola:

## Paso 1

```bash
> Hola. Bienvenido al sistema de cálculo de inversiones.
> ¿Cuánto quieres invertir?
> (EL usuario escribe aquí la cantidad)
```

## Paso 2

```bash
> ¿Cuál es el interés anual?
> (EL usuario escribe aquí el interés anual)
```

## Paso 3

```bash
> ¿Cuántos años vas a mantener la inversión?
> (EL usuario escribe aquí el nº de años)
```

## Paso 4 - Final

```bash
> En [N] años habrás recibido [X]€ de interés
> (Donde [N] debes sustituirlo por el número de años y [X] por la cantidad generada)
```

# Sesión 3

## Ejercicio 1
1. A la aplicación de la calculadora de inversión, deberás añadirle una opción para salir de la consola.

Debería quedar algo parecido a lo siguiente

```bash
> Hola. Bienvenido al sistema de cálculo de inversiones. ¿Qué quieres hacer?
> [1] Calcular una inversión
> [X] Salir
> (Aquí el usuario deberá escribir 1 o X. Ningón otro valor será considerado como válido. Saliendo el mismo mensaje si introduce algo distinto a 1 o X)
```

En caso de escribir 1 --> **Se** deberá proceder al sistema de Cálculo de inversión. En todas las pantallas posteriores, se debe mostrar la opción de [X] Salir

```bash
> En [N] años habrás recibido [X]€ de interés. ¿Qué quieres hacer ahora?
> [1] Calcular una nueva inversión
> [X] Salir
```

En caso de escribir **X** --> La aplicación debe mostrar un mensaje de despedida y cerrarse:

```bash
> ¡Nos vemos!
> (aplicación cerrada con un exit())
```

## Ejercicio 2
2. Crea un programa en Python que sea capaz de calcular y mostrar por consola todos los números primos de [1 - 100](https://es.wikipedia.org/wiki/N%C3%BAmero_primo)

## Ejercicio 3
3. Crea un programa en Python que sea capaz de identificar a partir de una lista de años si un año es bisiesto o no. 


# Sesión 4

## Ejercicio 1
1. A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
	1. Crea una función que reciba un rango de números como parámetro y muestre por consola únicamente los valores primos
	2. Crea una función que pueda evaluar si un número  (pasado por parámetro) es primo o no
	3. Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no.

## Ejercicio 2
2. Crea un proyecto Plantilla de Python que disponga de un archivo requirements.txt y un .venv que pueda ser ejecutado desde Visual Studio Code

## Ejercicio 3
3. Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los apellidos retornados por la API


# Sesión 5

## Ejercicio 1
1. Lee el archivo CSV con Pandas de 'pokemon_data.csv' alojado en la carpeta de datos de este repositorio y realizar las siguientes operaciones
- IMPRIMIR TODOS LOS VALORES
- IMPRIMIR LOS PRIMEROS 5
- IMPRIMIR LOS ÚLTIMOS 5
- OBTENER NOMBRES DE LAS COLUMNAS
- OBTENER TODOS LOS NOMBRES
- OBTENER TODOS LOS NOMBRES Y VELOCIDADES
- LOS PRIMEROS 5 NOMBRES USANDO [::]
- OBTENER TODAS LAS FILAS
- OBTENER UN RANGO DE FILAS
- OBTENER EL NOMBRE DE LA FILA 10
- ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
- POKEMONS DE TIPO 1 == WATER
- ESTADÍSTICAS (usando Describe del DafaFrame)
- ORDENACIÓN POR NOMBRE ASCENDENTE
- CREAR UNA COLUMNA EXTRA CALCULADA
    - La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
    - La columna debe llamarse TOTAL
- ELIMINAR LA COLUMNA TOTAL
- FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
- FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON
- FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
- FILTRAR POKEMONS CON NOMBRE "MEGA"
- FILTRAR POKEMONS SIN NOMBRE "MEGA"
- FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
- RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
- RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
- CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
- (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
- (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
- (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
- (Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
- (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON
- (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
    
    
Nota: 
SI TENEMOS ARCHIVOS ENORMES (1TB) PODEMOS LEERLOS POR PARTES 
Cada fila podría estar acumulando cerca de 20 bytes, por lo que podríamos estar trabajando con cantidades enormes

- LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE  (chunksize=5)
- ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA

## Ejercicio 2
2. Crea una clase Automóvil que disponga de los atributos necesarios y métodos para:
	1. Arrancar
	2. Acelerar
	3. Frenar
	4. Parar

## Ejercicio 3
3. Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:
	1. Coche
	2. Moto
	3. Camión
