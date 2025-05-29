La BD que he elegido es sobre LEGO ya que lo encontré en una web y me pareció curioso e interesante sacar datos acerca de ello. Dentro de Resources, encontraras un archivo jpg con las diferentes conexiones de los csv.


Mi objetivo es encontrar el top 5 tematicas de LEGO con más piezas distintas. Los pasos que he seguido son los siguientes:

1. Filter a los inventarios para eliminar las piezas que sean repuestos.

2. Join de la info de las piezas con sets y temas.

3. GroupBy por tema para contar piezas distintas.

4. Ordenar y mostrar el top 5.

Como después de hacer este experimento me faltaba por utilizar todavía el withColumn, decidí crear una categoria basada en el numero de piezas por set:
    "Pequeño" -> Menos de 100 piezas
    "Mediano" -> Entre 100 y 500 piezas
    "Grande" -> Mas de 500 piezas

5. Para ello usamos withColumn en setsDF para agregar la columna "set_category" categorizando los sets según el número de piezas.

6. Traemos el nombre del tema de cada set (fullSetsDF).

7. GroupBy a los sets por "set_category" para contar cuántos sets hay en cada categoría.

8. Mostramos los resultados con .show().