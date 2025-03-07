--- sesion 1
SELECT actor_id, first_name, last_name, last_update
FROM actor
WHERE first_name = 'Ed' or first_name='Nick';

SELECT actor_id, first_name, last_name, last_update
FROM actor
WHERE first_name LIKE 'N%'; -- QUE EMPIEZAN POR N

SELECT actor_id, first_name, last_name, last_update
FROM actor
WHERE first_name LIKE '%n'; -- QUE TERMINAN POR N

SELECT actor_id, first_name, last_name, last_update
FROM actor
WHERE first_name ILIKE '%n%'; -- QUE CONTENGA UNA N sea minúscula o mayúscula, en la palabra

SELECT actor_id, first_name, last_name, last_update
FROM actor
WHERE first_name ILIKE 'N_%'; -- QUE EMPIECE POR UNA N y luego cualquier caracter

SELECT actor_id, first_name, last_name, last_update 
FROM actor
WHERE last_name is null; -- (LIKE '') QUE no tenga apellido

SELECT actor_id, first_name, last_name, last_update 
FROM actor
WHERE first_name ILIKE 'N_%'; -- QUE EMPIECE POR UNA N y luego cualquier caracter

SELECT count (last_name)
FROM ACTOR; -- conteo APELLIDOS DE ACTORES

SELECT count (last_name) as l
FROM actor; -- CONTEO APELLIDOS DE ACTORES (cambia COUNT por l)

SELECT distinct (first_name) 
FROM actor; -- NOMBRES DISTINTOS DE ACTORES (no repetidos)

SELECT *
from film; -- toda la info de film

SELECT title
FROM film
WHERE replacement_cost < 2; -- peliculas que costo de reemplazo de la película) sea menor a 2

SELECT title
FROM film
WHERE replacement_cost > 2
AND title LIKE 'L%'; -- peliculas que costo de reemplazo de la película) sea menor a 2 y empiecen por L

SELECT title
FROM film
WHERE replacement_cost > 2
AND title LIKE 'L%'
AND rental_duration BETWEEN 0 and 5; -- peliculas que costo de reemplazo de la película) sea menor a 2, empiecen por L y la duracion del alquiler sea entre 0 y 5 días 

SELECT title
FROM film
WHERE replacement_cost > 2
AND title LIKE 'L%'
AND rental_duration BETWEEN 0 and 5
AND length > 100; -- peliculas que costo de reemplazo de la película) sea menor a 2, empiecen por L, la duracion del alquiler sea entre 0 y 5 días y dure mas de 100 minutos

SELECT title, 
ceil(replacement_cost / rental_rate) as break_even_point
FROM film; -- UMBRAL DE RENTABILIDAD (VECES QUE HAY QUE ALQUILAR PARA CUBRIR COSTES)

SELECT title, 
CEIL(replacement_cost / rental_rate) AS break_even_point
FROM film
ORDER BY break_even_point ASC; -- UMBRAL DE RENTABILIDAD, DE MENOS ALQUILERES A MAS

SELECT title, 
CEIL(replacement_cost / rental_rate) AS break_even_point
FROM film
ORDER BY break_even_point DESC; -- UMBRAL DE RENTABILIDAD, DE MAS ALQUILERES A MENOS

SELECT *
FROM FILM
WHERE special_features[2] ilike 'D%'; -- segunda palabra special_features empieza por d

SELECT *
FROM FILM; -- ver todo el apartado FILM