###SESION 1

SELECT * from actor WHERE first_name = 'Ed' or first_name = 'Nick';

-- Aqui estamos buscando a Ed o Nick

SELECT * from actor WHERE first_name iLIKE 'n%';

-- El porcentaje detras  nos esta diciendo que empiece con N

SELECT * from actor WHERE first_name iLIKE '%n';

-- El porcentaje delante nos esta diciendo que termine con N

SELECT * from actor WHERE first_name iLIKE '%n%';

--Si esta el porcentaje delante y detras es para que este en cualquier sitio de una palabra

SELECT * from actor WHERE first_name LIKE 'N_%';

--Si ponemos _ es para que busque una persona que tenga N y despues _

SELECT * from actor WHERE last_name is null;

--Si ponemos 'null' es para que busque una persona la columna last_name sea vacia

SELECT count(*) as Numero_de_actores from actor;

--Si ponemos 'SELECT count(*)' que cuente todas las filas de actores.

SELECT count (DISTINCT first_name) as Distintos_nombres from actor;

--Si ponemos 'count(*)' y queremos algo como que cuente solo una cosa, se mete dentro del parentesis del count.

SELECT count (DISTINCT first_name) as Distintos_nombres from actor;

SELECT MIN (first_name) from actor;

SELECT * from film where replacement_cost > 2 and title Like 'A%' and rental_duration >= 3 and rental_duration <= 5 and release_year = 2006
and length > 100;

SELECT title, ceil (replacement_cost / rental_rate) as new_operation from film

SELECT title, ceil (replacement_cost / rental_rate) as new_operation from film ORDER BY new_operation DESC
-- CEIL sirve para redondear un decimal hacia arriba
-- ORDER BY ___ DESC sirve para ordenar de mayor a menor o de la Z a la A
-- Si vemos la columna special_features o full text, para coger la columna que nos haga falta ponemos select special_features[1] o fulltext [3]

select rating, count(title) from film group by (rating)
-- Para agrupar por rating el numero de peliculas

###SESION 2


--Cláusula GROUP BY-- Nos agrupa por algo

SELECT rating, COUNT(title) FROM film GROUP BY (rating)
-- Para obtener por rating el número de películas

SELECT rating, COUNT(title), AVG (rental_rate), MAX (rental_rate), MIN (rental_rate), AVG (length), MAX (release_year) AS Año_de_la_pelicula_mas_antigua, MIN (release_year) FROM film  GROUP BY(rating)


SELECT * FROM film
--Para que me muestre toda la tabla

--PARA CAMBIAR EL NOMBRE DE LAS COLUMNAS 'AS'

--CLAUSULA HAVING-- Nos hace filtros
SELECT rating, COUNT(title), 
AVG (rental_rate), 
MAX (rental_rate), MIN (rental_rate),
AVG (length), 
MAX (release_year) AS Año_de_la_pelicula_mas_antigua, 
MIN (release_year) 
FROM film 
GROUP BY rating 
HAVING count(film_id)>200 --rating con más de 200 peliculas

SELECT
   rating,
   COUNT(title),
   AVG (rental_rate),
   MAX (rental_rate),
   MIN (rental_rate),
   AVG (length),
   MAX (release_year) AS Año_de_la_pelicula_mas_antigua,
   MIN (release_year) 
FROM
   film 
GROUP BY
   rating 
HAVING
   AVG(rental_rate) > 3

--CLAUSULA JOIN-- SELECT colum 1, colum2 FROM tabla a LEFT JOIN or RIGH JOIN on colum1 = colum2 

SELECT language.name, film.title
FROM language  
LEFT JOIN film on language.language_id = film.language_id
--LLEVAR UNA COLUMNA A OTRA TABLA

SELECT * FROM FILM

--RELACIONAR 3 COLUMNAS

SELECT actor.first_name, film.title, film_actor.actor_id--IDENTIFICAR Q COLUMNAS NECESITAS
FROM actor --TABLA PRINCIPAL
LEFT JOIN film_actor on actor.actor_id = film_actor.actor_id --COLUMNAS Q QUIERO VINCULAR CON LA PRINCIPAL
LEFT JOIN film on film_actor.film_id = film.film_id



SELECT first_name, COUNT(title)
FROM (
	SELECT actor.first_name, film.title, film_actor.actor_id
	FROM actor
	LEFT JOIN film_actor on actor.actor_id = film_actor.actor_id
	LEFT JOIN film on film_actor.film_id = film.film_id
) AS num_actors
GROUP BY first_name
HAVING 
	COUNT (title) <28


SELECT title, COUNT(first_name)
FROM (
	SELECT actor.first_name, film.title, film_actor.actor_id
	FROM actor
	LEFT JOIN film_actor on actor.actor_id = film_actor.actor_id
	LEFT JOIN film on film_actor.film_id = film.film_id
) AS num_actors
GROUP BY title
HAVING
COUNT (actor_id) >3
--LAS PELICULAS CON MENOS DE 3 ACTORES

--CREATE TABLE--
CREATE TABLE Opiniones
(	film_id serial4 not null,
	customer_id varchar(50) not null,
	review_date date not null,
	review_description varchar(50) not null
)
SELECT * FROM Opiniones

INSERT INTO Opiniones (film_id, film, review_date, review_description)
VALUES (4, 7, '10-11-2023', 'La pelicula es un poco aburrida')
--Añadi datos

ALTER TABLE reviews
ADD COLUMN review_stars int2
--añadir tabla

ALTER TABLE reviews
RENAME COLUMN review_description
TO review_opinion
--cambiar el nombre de una tabla

CREATE VIEW my_view_of_actor AS
SELECT actor_id, first_name, last_name, last_update FROM public.actor
where first_name IS NOT null
--crear una vista

CREATE VIEW top_tres AS
SELECT customer.customer_id, sum(payment.amount) as total_payment
FROM customer 
LEFT JOIN payment on customer.customer_id = payment.customer_id
GROUP BY customer.customer_id
ORDER BY total_payment DESC
--Vista que junta dos tablas para ordenar de mayor a menor los mejores clientes.

WITH mejores_clientes AS
( 
	SELECT customer_id,
			SUM(amount) AS total_amount
	FROM payment
	GROUP BY customer_id
	HAVING SUM(amount) > 190)
SELECT SUM(total_amount), COUNT(customer_id)
FROM mejores_clientes
