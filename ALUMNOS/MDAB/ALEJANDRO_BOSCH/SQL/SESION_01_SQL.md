
2024-10-24 15:16

# SESION 1 SQL 

SELECT first_name
FROM actor
WHERE first_name LIKE 'N%';  --para encontrar los nombres que empiezan por N y que acaben en n

SELECT first_name
FROM actor
WHERE first_name LIKE '%n';

SELECT first_name
FROM actor 
WHERE first_name ILIKE '%n%'; --puede contener algo o no, es como un or

SELECT *
FROM actor 
WHERE first_name ILIKE 'N_%'; --EMPIEZA EN N Y LO SIGUIENTE ES UN CARACTER, NO VALE ESPACIO

SELECT *
FROM actor
WHERE last_name is null; --saber si hay datos faltantes;

SELECT COUNT(*) AS n_actores
FROM actor; --CONTAR EL NUMERO DE NOMBRES EN LA COLUMNA


SELECT MAX(first_name)
FROM actor;

SELECT *
FROM film
WHERE replacement_cost > 2 AND title ILIKE 'A%' AND rental_duration BETWEEN 1 AND 7 AND release_year = 2006 AND length > 100 AND rental_rate > 2;

SELECT title, CEIL(replacement_cost / rental_rate) as punto_equilibrio
FROM film --CEIL SIRVE PARA REDONDEAR HACIA EL SIGUIENTE NUMERO
ORDER BY punto_equilibrio DESC;


SELECT special_features[1] --esto convierte de formato json, a formato texto
FROM film
WHERE replacement_cost > 2;

SELECT special_features[1] --para buscar las que empiezan por t
FROM film
WHERE special_features[1] ILIKE 'T%'

