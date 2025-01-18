-- Todo en la misma tabla
SELECT rating, count(*), ROUND(AVG(rental_rate),2), MIN(rental_rate), MAX(rental_rate), ROUND(AVG(length),2), MAX(release_year), MIN(release_year)
FROM film
--WHERE = mismo resultado que poner HAVING después // más eficiente que el HAVING
GROUP BY rating
/*HAVING solo funciona con el GROUP BY. 
Recomendable filtrar primero con el WHERE y usar HAVING solo con condiciones relacionadas con los grupos*/
HAVING count(*)>200;

SELECT rating, count(*), ROUND(AVG(rental_rate),2), MIN(rental_rate), MAX(rental_rate), ROUND(AVG(length),2), MAX(release_year), MIN(release_year)
FROM film
GROUP BY rating
HAVING ROUND(AVG(rental_rate),2) > 3;

SELECT rating, count(*), ROUND(AVG(rental_rate),2), MIN(rental_rate), MAX(rental_rate), ROUND(AVG(length),2), MAX(release_year), MIN(release_year)
FROM film
GROUP BY rating
HAVING ROUND(AVG(length),2) > 115;

-- JOIN
-- Ejemplo: film & language // language_id
SELECT title, name FROM film
LEFT JOIN language on film.language_id = language.language_id;

SELECT title, name FROM film
RIGHT JOIN language on film.language_id = language.language_id;

-- Relacionar 3 tablas
-- Lístame todas las películas donde sale cada actor 
SELECT title, first_name, last_name
FROM film f
INNER JOIN film_actor fa on f.film_id = fa.film_id
INNER JOIN actor a on fa.actor_id = a.actor_id;

-- Conteo de las películas por actor
SELECT first_name, last_name, count(f.title) -- recomendable poner el alias en todas las columnas
FROM film f
INNER JOIN film_actor fa on f.film_id = fa.film_id
INNER JOIN actor a on fa.actor_id = a.actor_id
GROUP BY a.first_name, a.last_name
HAVING count(f.title) > 30

-- Conteo de actores por película
SELECT title, count(a.first_name)
FROM film f
INNER JOIN film_actor fa on f.film_id = fa.film_id
INNER JOIN actor a on fa.actor_id = a.actor_id
GROUP BY f.title
HAVING count(a.first_name) > 4;

/* Si no se pone alias, no hace falta ponerlo
SELECT title, count(first_name)
FROM film
INNER JOIN film_actor on film.film_id = film_actor.film_id
INNER JOIN actor on film_actor.actor_id = actor.actor_id
GROUP BY title
*/

-- Create table (Ejercicio 10)
CREATE TABLE IF NOT EXISTS reviews_twc (
film_id int2 NOT NULL,
customer_id int2 NOT NULL,
review_date date NOT NULL,
review_description varchar(50) NOT NULL
);
-- Inserción de registros en una tabla
INSERT INTO reviews_twc (film_id, customer_id, review_date, review_description)
VALUES ('4',  '7','10-11-2023', 'La película es un poco aburrida');

SELECT * FROM reviews_twc
