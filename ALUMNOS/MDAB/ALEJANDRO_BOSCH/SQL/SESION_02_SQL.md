
SELECT COUNT(*) AS n_peliculas
FROM film
GROUP BY rating; --rating y total peliculas

SELECT ROUND(AVG(rental_rate), 2) as precio_medio_alquiler
FROM film 
GROUP BY rating; --precio medio alquiler por rating


SELECT ROUND(MIN(rental_rate), 2) as precio_min_alquiler
FROM film
GROUP BY rating; --precio minimo alquiler por rating


SELECT ROUND(MAX(rental_rate), 2) as precio_max_alquiler
FROM film
GROUP BY rating; --precio maximo alquiler por rating


SELECT ROUND(AVG(length), 2)  as duracion_media_pelis
FROM film
GROUP BY rating; --duracion media peliculas por rating


SELECT MAX(release_year) as peli_mas_antigua
FROM film 
GROUP BY rating; --pelicula más antigua por rating



SELECT MIN(release_year) as peli_mas_antigua
FROM film 
GROUP BY rating; --pelicula más antigua por rating


-- HAVING ES EL WHERE DE LOS GRUPOS; FUNCIONA IGUAL, SOLO QUE EN GRUPOS
-- Sin group by no hay having

--------------------------------

--Ejercicios clausula HAVING

SELECT COUNT(*) AS n_peliculas
FROM film GROUP BY rating
HAVING COUNT(film) > 200; --ordena el total de peliculas, hace una agrupacion por rating y luego de la columna film,hace un having donde cuenta las films basada en rating mayores de 200   


SELECT ROUND(AVG(rental_rate), 2) as precio_medio_alquiler
FROM film 
GROUP BY rating --precio medio alquiler por rating
HAVING AVG (rental_rate) > 3;


SELECT ROUND(AVG(length), 2)  as duracion_media_pelis
FROM film
GROUP BY rating --duracion media peliculas por rating y que tenga duracion mayor 115
HAVING AVG(length) > 115;


---------

SELECT *
FROM film a
LEFT JOIN language b on a.film_id = b.language_id;

SELECT *
FROM film a
LEFT JOIN language b on a.film_id = b.language_id;


SELECT title, name
FROM film a
LEFT JOIN language b on a.film_id = b.language_id;
--- Para seleccionar, en select pongo a.column1, b.column2


SELECT title, name
FROM film a
RIGHT JOIN language b on a.film_id = b.language_id; 


SELECT a.first_name, a.last_name, f.title
FROM film f
LEFT JOIN film_actor fa on f.film_id = fa.film_id
LEFT JOIN actor a on a.actor_id = fa.actor_id;

---CONTEO POR PELICULAS DE LOS ACTORES QUE PARTICIPAN EN LAS PELICULAS
SELECT f.title, COUNT(a.actor_id) as Total_actores
FROM film f
LEFT JOIN film_actor fa on f.film_id = fa.film_id
LEFT JOIN actor a on a.actor_id = fa.actor_id
GROUP BY title;


---PELICULAS CON > 30 ACTORES
SELECT f.title, COUNT(a.actor_id) as Total_actores
FROM film f
LEFT JOIN film_actor fa on f.film_id = fa.film_id
LEFT JOIN actor a on a.actor_id = fa.actor_id
GROUP BY title
HAVING COUNT(a.actor_id) > 30;

--- Actor, numero peliculas
SELECT a.first_name, a.last_name, COUNT(f.film_id) as Total_peliculas
FROM film f
LEFT JOIN film_actor fa on f.film_id = fa.film_id
LEFT JOIN actor a on a.actor_id = fa.actor_id
GROUP BY a.actor_id;

-----

-- INNER JOIN, para ir moviendose por las tablas hasta llegar a la que queremos
-- LIMIT, sirve para que de la tabla solo salga rows o columns, depende de lo que digamos, junto al numero correspondiente


CREATE TABLE reviews_ab(
film_id int NOT NULL,
customer_id int NOT NULL,
reviewer_date date NOT NULL,
review_description varchar(100)
);

INSERT INTO reviews_ab(film_id, customer_id, reviewer_date, review_description)
VALUES(5, 7, '10-28-2024', 'La pelicula es buena');

SELECT *
FROM reviews_ab; --REVISO QUE ESTA TODO BIEN