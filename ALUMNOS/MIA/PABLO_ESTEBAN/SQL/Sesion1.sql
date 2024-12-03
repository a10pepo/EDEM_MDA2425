	SELECT *
	FROM actor
	WHERE first_name = 'Ed' OR first_name = 'Nick';

	-- Actores que contengan una 'n'
	SELECT *
	FROM actor
	WHERE first_name ilike  '%n%';

	-- Actores que empiecen por n, luego un caracter y despues cualquier otra casa
	SELECT * FROM actor
	WHERE first_name ilike  'N_%';

	-- Actores sin apellido
	SELECT * FROM actor
	WHERE last_name is null;

	-- Cuantos actores hay en la base de datos
	SELECT count(*) FROM actor;

	-- Cambiar alias columna actores
	SELECT first_name as nombre
	FROM actor
	WHERE first_name = 'Nick';

	-- Numero unico de actores que tengo en mi base de datos
	-- SELECT count(first_name) FROM actor
	-- WHERE 

	-- Replacement ...
	SELECT * -- SELECT count(*)
	FROM film
	WHERE
		replacement_cost > 2
		AND title ILIKE 'p%'
		AND rental_duration BETWEEN 0 AND 5
		AND release_year = 2006
		AND "length" > 100
		AND rental_rate > 2;



	SELECT
		title AS Titulo,
		CEIL(replacement_cost / rental_rate) AS break_event
	FROM
		film
	ORDER BY break_event DESC;


	SELECT *
	FROM film
