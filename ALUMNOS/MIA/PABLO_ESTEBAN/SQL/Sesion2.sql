SELECT rating, count(title), avg(rental_rate),
min(rental_rate), max(rental_rate), avg(film.length), min(release_year), max(release_year)
FROM film
GROUP BY rating;


SELECT rating, count(title)
FROM film
GROUP BY rating
HAVING count(title) > 200;

SELECT rating, avg(rental_rate)
FROM film
GROUP BY rating
HAVING avg(rental_rate) > 3;

SELECT rating, avg(film.length) as duracion_media
FROM film
GROUP BY rating
HAVING avg(film.length) > 115;

SELECT t1.title, t2.name
FROM film t1
LEFT JOIN language t2 ON t1.language_id = t2.language_id;

SELECT t1.title, t2.name
FROM film t1
RIGHT JOIN language t2 ON t1.language_id = t2.language_id;

SELECT t1.title, t3.first_name
FROM film t1
INNER JOIN film_actor t2 ON t1.film_id = t2.film_id
INNER JOIN actor t3 ON t2.actor_id = t3.actor_id;

SELECT t1.title, count(t1.title) as num_actores
FROM film t1
INNER JOIN film_actor t2 ON t1.film_id = t2.film_id
GROUP BY t1.title;

SELECT 
	t1.first_name||' '||t1.last_name as name,
	count(t1.first_name) as num_peliculas
FROM actor t1
INNER JOIN film_actor t2 ON t1.actor_id = t2.actor_id
GROUP BY t1.first_name, t1.last_name;

CREATE TABLE IF NOT EXISTS reviews(
	film_id int,
	customer_id int,
	review_date timestamp,
	review_description varchar
);

INSERT INTO reviews (film_id, customer_id, review_date, review_description)
VALUES (4, 7, '10/28/2024', 'La pelicula es un poco aburrida');

SELECT * FROM reviews;
