-- ***********************************
-- ***         CLASE 1             ***
-- ***********************************

SELECT actor_id, first_name, last_name, last_update FROM public.actor;

SELECT AVG(rental_rate) FROM film;

SELECT 
    AVG(rental_rate) AS promedio_rental_rate, 
    MIN(rental_rate) AS minimo_rental_rate, 
    MAX(rental_rate) AS maximo_rental_rate 
FROM film;

SELECT 
    title, 
    rental_rate, 
    replacement_cost, 
    ROUND(rental_rate / replacement_cost, 2) AS proporcion 
FROM public.film;

SELECT 
    title, 
    FLOOR(replacement_cost / rental_rate) AS veces_para_recuperar_costo 
FROM public.film;

SELECT 
    title, 
    replacement_cost / rental_rate AS calculo_bruto, 
    CEIL(replacement_cost / rental_rate) AS veces_alquilar 
FROM film;

SELECT * FROM film WHERE rental_rate BETWEEN 2 AND 3 AND title LIKE 'A%' AND title LIKE '%s';

-- ===== EJERCICIO 3 =====

SELECT nombre_cliente FROM cliente WHERE calle_cliente IS NULL;

SELECT first_name FROM actor WHERE first_name LIKE 'A%';

SELECT title FROM film WHERE rental_rate > 10;
SELECT title FROM film WHERE rental_rate BETWEEN 5 AND 10;

SELECT rental_rate 
FROM film 
WHERE title = 'Giant Troopers' AND 'Gilbert Pelican';

SELECT title, rating, rental_duration 
FROM film 
WHERE title LIKE 'Ali Forever';

-- ===== EJERCICIO 4 =====

SELECT title, length FROM film ORDER BY length ASC;
SELECT title, length FROM film ORDER BY length ASC LIMIT 5;

SELECT f.length FROM film AS f;

SELECT rental_rate, COUNT(*) FROM film GROUP BY rental_rate;
SELECT rental_rate, COUNT(*) FROM film GROUP BY 1;

-- ===== EJERCICIO 6 =====

SELECT rating, COUNT(title) FROM film GROUP BY rating;
SELECT rating, AVG(rental_rate) FROM film GROUP BY rating;
SELECT rating, MIN(rental_rate) FROM film GROUP BY rating;
SELECT rating, MAX(rental_rate) FROM film GROUP BY rating;
SELECT rating, AVG(length) FROM film GROUP BY rating;
SELECT rating, MIN(release_year) FROM film GROUP BY rating;
SELECT rating, MAX(release_year) FROM film GROUP BY rating;

SELECT 
    rating, 
    COUNT(title), 
    AVG(rental_rate), 
    MIN(rental_rate), 
    MAX(rental_rate), 
    AVG(length), 
    MIN(release_year), 
    MAX(release_year) 
FROM film 
GROUP BY rating 
HAVING AVG(length) > 120;

SELECT rating, AVG(length) FROM film GROUP BY rating HAVING AVG(length) > 120;

-- ===== EJERCICIO 7 =====

SELECT rating, COUNT(title) FROM film GROUP BY 1 HAVING COUNT(title) > 200;
SELECT rating, AVG(rental_rate) FROM film GROUP BY 1 HAVING AVG(rental_rate) > 3;
SELECT rating, AVG(length) FROM film GROUP BY 1 HAVING AVG(length) > 115;

SELECT rating, COUNT(title), AVG(rental_rate), AVG(length) 
FROM film 
GROUP BY 1 
HAVING COUNT(title) > 200 AND AVG(rental_rate) > 3 AND AVG(length) > 115;

-- ***********************************
-- ***         CLASE 2             ***
-- ***********************************

-- ===== EJERCICIO 8 =====

SELECT customer.first_name, customer.last_name, address.address 
FROM customer 
LEFT JOIN address ON customer.address_id = address.address_id;

SELECT 
    customer.first_name, 
    customer.last_name, 
    address.address, 
    city.city, 
    country.country 
FROM customer 
LEFT JOIN address ON customer.address_id = address.address_id
LEFT JOIN city ON address.city_id = city.city_id
LEFT JOIN country ON city.country_id = country.country_id;

-- ===== EJERCICIO 9 =====

SELECT film.title 
FROM film 
LEFT JOIN film_actor ON film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.last_name LIKE 'C%'
GROUP BY film.title 
HAVING COUNT(actor.last_name) = 1;

SELECT film.title, COUNT(actor.actor_id) 
FROM film 
LEFT JOIN film_actor ON film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id 
GROUP BY film.title;

SELECT film.title 
FROM film 
LEFT JOIN film_actor ON film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id 
GROUP BY film.title 
HAVING COUNT(actor.actor_id) > 2;

SELECT film.title, COUNT(actor.actor_id) AS total_actores 
FROM film 
LEFT JOIN film_actor ON film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id 
GROUP BY film.title 
ORDER BY total_actores DESC 
LIMIT 1;

-- ***********************************
-- ***         CLASE 3             ***
-- ***********************************

CREATE TABLE public.reviews_iv (
    film_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    review_date TIMESTAMP NOT NULL DEFAULT NOW(),
    review_description VARCHAR(100),
    CONSTRAINT reviews_iv_pkey PRIMARY KEY (customer_id, film_id)
);

INSERT INTO public.reviews_iv (film_id, customer_id, review_description)
VALUES (1234, 1222, 'Buena película');

UPDATE public.reviews_iv
SET review_description = 'Me gusta'
WHERE customer_id = 1222 AND film_id = 1234;

DELETE FROM public.reviews_iv
WHERE review_description = 'Me gusta';

DROP TABLE public.reviews_iv;
