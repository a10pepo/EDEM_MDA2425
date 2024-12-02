SELECT COUNT(film) AS total_film
FROM film
GROUP BY rating;

SELECT ROUND(AVG(rental_rate), 2) AS price_avg
FROM film
GROUP BY rating;

SELECT MIN(rental_rate) AS max_rental
FROM film
GROUP BY rating;

SELECT MAX(rental_rate) AS max_rental
FROM film
GROUP BY rating;

SELECT ROUND(AVG(film.length)) AS duration_avg
FROM film
GROUP BY rating;

SELECT MIN(film.release_year) AS old_film
FROM film
GROUP BY rating;

SELECT MAX(film.release_year) AS new_film
FROM film
GROUP BY rating;

SELECT rating, COUNT(film) AS total_film
FROM film
GROUP BY rating
HAVING COUNT(film) > 200;

SELECT ROUND(AVG(rental_rate), 2) AS price_avg
FROM film
GROUP BY rating
HAVING AVG(rental_rate) > 3;

SELECT ROUND(AVG(film.length),2) AS duration_avg
FROM film
GROUP BY rating
HAVING AVG(film.length) > 115;

SELECT a.title , b.name
FROM film a
LEFT JOIN language b on a.language_id = b.language_id;

SELECT a.title, c.first_name, c.last_name
FROM film a
LEFT JOIN film_actor b on a.film_id = b.film_id
LEFT JOIN actor c on b.actor_id = c.actor_id

SELECT a.title, COUNT(c.actor_id) AS total_actores
FROM film a
LEFT JOIN film_actor b ON a.film_id = b.film_id
LEFT JOIN actor c ON b.actor_id = c.actor_id
GROUP BY a.title;

SELECT c.first_name, c.last_name, COUNT(a.film_id) AS total_pelis
FROM film a
LEFT JOIN film_actor b ON a.film_id = b.film_id
LEFT JOIN actor c ON b.actor_id = c.actor_id
GROUP BY c.actor_id;

CREATE TABLE reviews_js(
film_id varchar(50) NOT NULL,
customer_id INT NOT NULL,
review_date DATE NOT NULL,
review_description varchar(250)
);

INSERT INTO reviews_js (film_id, customer_id, review_date, review_description)
VALUES('as54f234f', 15, '28-10-2024', 'Muy_mala');
SELECT*
FROM reviews_js;