-- ¿Cuántos actores tiene cada pelicula?
SELECT film.title, count(film_actor.actor_id) FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id
GROUP BY film.film_id
ORDER BY film.title DESC;

-- ¿Cuáles son las películas que tienen más de 2 actores?
SELECT film.title, count(film_actor.actor_id) FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id
GROUP BY film.film_id
HAVING COUNT(film_actor.actor_id) > 2
ORDER BY film.title DESC;

-- ¿Que pelicula es la que más actores tiene?
SELECT film.title, count(film_actor.actor_id) as actores FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
GROUP BY film.title
ORDER BY actores DESC
LIMIT 1;

-- Añadir una columna con el tipo review_pau
ALTER TABLE review_pau 
ADD COLUMN review_stars int2;

-- Renombrar la columa review_description
ALTER TABLE review_pau
RENAME COLUMN review_description TO review_opinion;


-- ¿Cuántos actores tiene cada pelicula?
SELECT film.title, ARRAY_AGG(actor.first_name || ' ' || actor.last_name) actors
FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor_id ON film_actor.actor_id = actor.actor_id
GROUP BY film.film_id
ORDER BY film.title DESC;

-- Creación de vistas
CREATE VIEW my_view_of_actor AS
SELECT actor_id, first_name, last_name, last_update
FROM public.actor
where first_name IS NOT null;

-- La creación de mi vista
CREATE VIEW vista_pau AS
SELECT film.title, count(film_actor.actor_id) as actores FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
GROUP BY film.title
ORDER BY actores DESC
LIMIT 1;

-- Vista con los tres mejores clientes
CREATE VIEW tres_mejores_clientes AS
SELECT customer.first_name,customer.last_name, sum(payment.amount) as cantidad_dinero FROM payment
JOIN customer ON customer.customer_id = payment.customer_id
GROUP BY customer.first_name, customer.last_name
ORDER BY cantidad_dinero DESC
LIMIT 3;

-- Vista con los tres peores clientes
CREATE VIEW tres_peores_clientes AS
SELECT customer.first_name,customer.last_name, sum(payment.amount) as cantidad_dinero FROM payment
JOIN customer ON customer.customer_id = payment.customer_id
GROUP BY customer.first_name, customer.last_name
ORDER BY cantidad_dinero
LIMIT 3;


-- Subconsultas
-- Peliculas que empiecen por C y dar nombres de los actores
SELECT actor.actor_id, actor.first_name, actor.last_name, film.title
FROM public.actor
JOIN film_actor ON film_actor.actor_id = actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE film.title IN
	(SELECT film.title FROM public.film WHERE film.title ILIKE 'C%' );
	
-- Peliculas que estan en ingles
SELECT film.title FROM film
WHERE film.language_id in 
    (SELECT language.language_id FROM public.language WHERE language.name = 'English');
	
-- Todos aquellos clientes que viven en una dirección que empiece por 1
SELECT customer.first_name FROM customer
WHERE customer.address_id IN 
    (SELECT address.address_id FROM address WHERE address.address ILIKE '1%');
	
-- Clientes que han pagado más de 190$
WITH gasto_por_cliente as (
	SELECT customer.first_name, sum(payment.amount) as cantidad
	FROM public.customer
	JOIN payment ON payment.customer_id = customer.customer_id
	GROUP BY customer.first_name
)
SELECT * FROM gasto_por_cliente where cantidad > 190

-- Número de clientes que han pagado más de 190$
WITH gasto_por_cliente as (
	SELECT customer.first_name, sum(payment.amount) as cantidad
	FROM public.customer
	JOIN payment ON payment.customer_id = customer.customer_id
	GROUP BY customer.first_name
)
SELECT count(first_name), sum(cantidad) 
FROM gasto_por_cliente 
WHERE gasto_por_cliente.cantidad > 190;