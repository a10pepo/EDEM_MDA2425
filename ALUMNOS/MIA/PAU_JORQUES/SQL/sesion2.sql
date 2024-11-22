-- Numero de películas por rating.

SELECT COUNT(title), rating FROM film GROUP BY rating;

-- Precio medio de alquiler por rating. 

SELECT ROUND(AVG(rental_rate),2), rating FROM film GROUP BY rating;

-- Precio minimo de alquiler por rating.

select ROUND (MIN(rental_rate),2), rating FROM film GROUP BY rating;

-- Precio maximo de alquiler por rating.

select ROUND (MAX(rental_rate),2), rating FROM film GROUP BY rating;

-- Duracion media de las peliculas por rating.

select ROUND (AVG(length),2), rating FROM film GROUP BY rating;

-- Año de la pelicula mas antigua por rating.

select MIN(release_year), rating FROM film GROUP BY rating;

-- Año de la pelicula mas nueva por rating.

select MAX(release_year), rating FROM film GROUP BY rating;

''' 
	Numero de peliculas y quedate unicamente con aquellos rating 
	que tengan mas de 200 peliculas.
'''

SELECT COUNT(title), rating FROM film GROUP BY rating HAVING COUNT(title) > 200;

'''
	Precio medio de alquiler y quedate unicamente con aquellos 
	rating que tenga un precio medio superior a 3.
'''

SELECT ROUND(AVG(rental_rate),2), rating FROM film GROUP BY rating HAVING AVG(rental_rate) > 3;

'''
	Duracion media de las peliculas y quedate con aquellos
	rating que tengan una duracion media mayor a 115 min.
'''

select ROUND (AVG(length),2) AS duracion_media, rating FROM film GROUP BY rating HAVING AVG(length) > 115;

-- CLAUSULA JOIN

SELECT title, language.name FROM film LEFT JOIN language ON language.language_id = film.language_id;

-- CLAUSULA JOIN AVANZADA

SELECT film.title, actor.first_name, actor.last_name FROM film 
LEFT JOIN film_actor ON  film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id;

-- Conteo por pelicula de los actores que participan con cada pelicula

SELECT film.title, COUNT(actor.actor_id) FROM film 
LEFT JOIN film_actor ON  film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
GROUP BY film.film_id
ORDER BY film.film_id;

''' 
	Conteo por pelicula de los actores que participan con cada pelicula
	con mas de 10 actores
'''

SELECT film.title, COUNT(actor.actor_id) FROM film 
LEFT JOIN film_actor ON  film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
GROUP BY film.film_id HAVING COUNT(actor.actor_id) > 10
order by film.film_id;

-- Numero de peliculas que ha hecho cada actor

SELECT COUNT(film.title) AS num_peliculas, actor.first_name, actor.last_name FROM film 
LEFT JOIN film_actor ON  film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id IS NOT NULL
GROUP BY actor.actor_id
ORDER BY num_peliculas DESC;

-- Crear tabla reviews

CREATE TABLE IF NOT EXISTS review_pau (
	film_id varchar(50) NOT NULL,
	customer_id varchar(50) NOT NULL,
	review_date timestamp NOT NULL,
	review_description varchar(500) NOT NULL 
);

-- Insertar en la tabla creada

INSERT INTO review_pau (film_id, customer_id, review_date, review_description)
VALUES ('4','7','2024-10-28','La película es un poco aburrida');