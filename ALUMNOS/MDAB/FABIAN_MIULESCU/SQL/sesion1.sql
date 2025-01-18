SELECT actor_id, first_name, last_name, last_update
FROM actor
WHERE first_name LIKE '%N%';

SELECT actor_id, first_name, last_name, last_update
FROM actor
WHERE first_name LIKE 'N%n';

SELECT actor_id, first_name, last_name, last_update
FROM actor
WHERE first_name LIKE '%n';

SELECT actor_id, first_name, last_name, last_update
FROM actor
WHERE first_name LIKE '%n%';

SELECT first_name
FROM actor 
WHERE first_name ILIKE '%n%';

SELECT first_name
FROM actor 
WHERE first_name ILIKE 'N_%';

SELECT first_name, last_name
FROM actor 
WHERE last_name is NULL;

SELECT COUNT(actor) AS total_actors
FROM actor;

SELECT COUNT (DISTINCT first_name)
FROM actor;

SELECT MAX(first_name)
FROM actor;

SELECT *
FROM film
WHERE replacement_cost > 2 AND title ILIKE 'J%' AND rental_duration BETWEEN 3 AND 5 AND release_year = 2006 AND "length" > 100 AND rental_rate > 2;

SELECT title, CEIL(replacement_cost/rental_rate) as Punto_eq
FROM film
ORDER BY Punto_eq DESC;

SELECT special_features[1]
FROM film
WHERE replacement_cost > 2;

SELECT * 
FROM film
WHERE special_features[2] ILIKE 'D%';

