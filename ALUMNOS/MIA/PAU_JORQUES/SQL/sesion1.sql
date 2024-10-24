-- Actores que se llamen Ed o Nick
SELECT actor_id, first_name, last_name  
FROM actor 
WHERE first_name = 'Ed' OR first_name = 'Nick';

-- Actores que empiezan por N
SELECT * FROM actor
WHERE first_name ILIKE'N%';
	
-- Actores que acaban y empiezan por n
SELECT * FROM actor
WHERE last_name ILIKE '%n' AND last_name ILIKE 'n%';

-- Actores que empiezen por n, luego tengan un caracter y luego cualquier cosa
SELECT * FROM actor
WHERE first_name ILIKE 'n_%';

-- Actores que no tengan apellido
SELECT * FROM actor
WHERE last_name LIKE '';

-- Lo mismo que arriba
SELECT * FROM actor
WHERE last_name IS null;

-- Número de actores
SELECT COUNT(actor_id) as numActores FROM actor;

-- Nombres únicos de los actores
SELECT COUNT(DISTINCT(first_name)) FROM actor;

-- Nombre maximo (Muestra el ultimo alfabeticamente)
SELECT MAX(first_name) FROM actor;

-- Vamos a la tabla film
SELECT * FROM film;

/* 
Sacar las peliculas que tengan un replacement cost mayor a dos
y las peliculas empiecen por P
*/
SELECT * FROM film WHERE replacement_cost > 2 AND title ILIKE 'p%'

-- Peliculas que tengan un rental_duration entre 0 y 5
SELECT * FROM film WHERE rental_duration BETWEEN 0 AND 5;

-- Peliculas que tengan un rental_duration entre 0 y 5 y que sean de 2006 y duracion mayor de 100 minutos y rental_rate mayor de dos euros
SELECT * FROM film WHERE rental_duration BETWEEN 0 AND 5 AND release_year = 2006 AND length > 100 AND rental_rate > 2;

-- Cuantas veces tengo que alquilar una peli para que me salga rentable
SELECT title, ceil(replacement_cost/rental_rate) as break_even FROM film 
ORDER BY break_even DESC;


