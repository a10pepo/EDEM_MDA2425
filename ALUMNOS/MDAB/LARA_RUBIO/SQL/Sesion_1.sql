SELECT first_name, last_name, actor_id, last_update FROM actor

WHERE first_name = 'Ed' or first_name = 'Nick';

SELECT * FROM actor WHERE first_name LIKE 'N%' OR first_name LIKE '%n' OR first_name LIKE '%n%';

SELECT * FROM actor
WHERE first_name ilike '%n%';

SELECT * FROM actor WHERE first_name LIKE 'N_%';
SELECT * FROM actor WHERE last_name IS null;

SELECT count (*) AS total_actores FROM actor;

SELECT COUNT (DISTINCT first_name) FROM actor;

SELECT * FROM film WHERE special_features[2] LIKE 'D%';

SELECT max(first_name)FROM actor;


SELECT title FROM film WHERE replacement_cost >2 AND title ILIKE 'L%';

SELECT * FROM film WHERE rental_duration BETWEEN 0 AND 5;

SELECT * FROM film WHERE release_year=2006;

SELECT * FROM film WHERE length>100;

SELECT * FROM film WHERE rental_rate>2;

SELECT  title, ceil(replacement_cost / rental_rate) AS rental_break_even FROM film ORDER BY rental_break_even DESC;
	



