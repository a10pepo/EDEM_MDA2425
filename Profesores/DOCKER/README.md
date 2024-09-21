# Contenedores

Para entregar este ejercicio, debes subir el Código generado a vuestro repositorio remoto de GitHub y realizar una Pull Request poniendo a *Alberto Hernandez (alhercan)* como reviewer.

## Objetivo

Construir una imagen docker que acepte como parámetro dos números e imprima la suma de ambos


## Paso a Paso

1. Construir un script en python que acepte dos números como parámetros e imprima el resultado de la suma
2. Construir una imagen docker que contenga dicho python script
3. Cuando se ejecute el contendor docker, este debe invocar al script pasando como parámetro ambos números. 

## Ejemplo de invocación

Ejemplo de invocación del contenedor Docker

```
docker run pysum 3 4
```

Ejemplo de salida del resultado esperado

```
Sum: 7 
```

## Entregable:

- Script the python 
- dockerfile
- Captura de pantalla donde se muestra la invocación al contenedor docker y el resultado de la ejecución
- (Opcional) Link a la imagen docker generada y subida a Docker Hub


