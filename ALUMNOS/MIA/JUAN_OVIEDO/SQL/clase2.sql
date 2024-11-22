--Ordenar por rating numero de peliculas--
SELECT rating, COUNT (title)
FROM film
GROUP BY rating;
--Ordenar por rating precio medio de alquiler--
SELECT rating, ROUND(AVG(rental_rate), 2)
FROM film
GROUP BY rating;
--Ordenar por precio minimo de alquiler--
SELECT rating, MIN(rental_rate)
FROM film
GROUP BY rating;
--Ordenar por precio máximo de alquiler--
SELECT rating, MAX(rental_rate)
FROM film
GROUP BY rating;
-- Ordenar duración media de las películas --
SELECT rating, ROUND(AVG(length),2)
FROM film
GROUP BY rating;
-- Ordenar año de la película más antigua --
SELECT rating, year(MAX(release_year))
FROM film
GROUP BY rating;
-- Ordenar año de la película más nueva --
SELECT rating, year(MIN(release_year))
FROM film
GROUP BY rating;
-- CLAUSULA HAVING  NUMERO DE PELICULAS ---
SELECT rating, COUNT (title)
FROM film
GROUP BY rating
HAVING COUNT (title) > 200;
----- CLAUSULA HAVING PRECIOS MEDIOS SUPERIOR A 3 --------
SELECT rating, ROUND(AVG(rental_rate), 2)
FROM film
GROUP BY rating
HAVING COUNT (rental_rate) > 3;
-- CLAUSULA HAVING DURACION MEDIA DE PELICULAS--
SELECT rating, ROUND(AVG(length),2)
FROM film
GROUP BY rating
HAVING ROUND(AVG(length), 2) > 115;
-- UTILIZAR JOIN --
SELECT a.title, b.language_id
FROM film a
RIGHT JOIN language b ON a.language_id = b.language_id;
-- UTILIZAR JOIN BUSCANDO NÚMERO DE PELICULAS QUE ACTUAN ACTORES ENTRE TABLAS --
SELECT c.first_name, COUNT(a.title) as numero_peliculas
FROM film a
LEFT JOIN film_actor b ON a.film_id=b.film_id
LEFT JOIN actor c ON b.actor_id=c.actor_id
GROUP BY first_name;
--- CREAR TABLA ---
CREATE TABLE IF NOT EXISTS reviews_JO(
film_id serial4 NOT NULL,
customer_id varchar (50) NOT NULL,
review_date date NOT NULL,
review_description varchar(50) NOT NULL
);
--INSERTAR DATOS--
INSERT INTO reviews_jo(film_id,customer_id,review_description,review_date)
VALUES('4', '7','La película es un poco aburrida','10-11-2023');

