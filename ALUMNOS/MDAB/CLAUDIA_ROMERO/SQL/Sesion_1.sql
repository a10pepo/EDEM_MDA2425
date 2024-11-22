SELECT * FROM actor WHERE first_name LIKE 'N%';

SELECT * FROM actor WHERE first_name LIKE '%n%';

SELECT * FROM actor WHERE first_name LIKE '%n';

SELECT * FROM actor WHERE last_name IS NULL;

SELECT COUNT(*) AS total_actores FROM actor;

SELECT COUNT(DISTINCT first_name) FROM actor;

SELECT MAX(first_name) FROM actor;

SELECT first_name FROM actor ORDER BY first_name DESC;

SELECT first_name FROM actor ORDER BY first_name ASC;

SELECT title FROM film WHERE replacement_cost > 2 AND title LIKE 'C%';

SELECT rental_duration FROM film WHERE rental_duration BETWEEN 0 AND 5;

SELECT title FROM film WHERE release_year = 2006;

SELECT title FROM film WHERE length > 100;

SELECT title FROM film WHERE rental_rate > 2;

SELECT title, CEIL(replacement_cost / rental_rate) AS rental_break_even FROM film;

SELECT title, CEIL(replacement_cost / rental_rate) AS rental_break_even FROM film ORDER BY rental_break_even DESC;