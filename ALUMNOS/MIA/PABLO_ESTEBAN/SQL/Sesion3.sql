-- Contar actores por película
SELECT f.title AS film_title, COUNT(fa.actor_id) AS total_actors
FROM film f
INNER JOIN film_actor fa ON f.film_id = fa.film_id
GROUP BY f.title;

-- Películas con más de 2 actores
SELECT f.title AS movie_title, COUNT(fa.actor_id) AS number_of_actors
FROM film f
LEFT JOIN film_actor fa ON f.film_id = fa.film_id
GROUP BY f.title
HAVING COUNT(fa.actor_id) > 2
ORDER BY number_of_actors ASC;

-- Agregar una columna
ALTER TABLE reviews_im
ADD COLUMN review_stars SMALLINT;

ALTER TABLE reviews_im
RENAME COLUMN review_description TO review_opinion;

-- Crear una vista para películas con más de 2 actores
CREATE VIEW actors_per_movie AS
SELECT f.title AS movie_title, COUNT(fa.actor_id) AS actor_count
FROM film f
LEFT JOIN film_actor fa ON f.film_id = fa.film_id
GROUP BY f.title
HAVING COUNT(fa.actor_id) > 2
ORDER BY actor_count ASC;

-- Usar la vista de actores por película
SELECT * FROM actors_per_movie;

-- Crear una vista para los mejores clientes
CREATE VIEW top_customers AS
SELECT cu.customer_id, cu.first_name, cu.last_name, SUM(pa.amount) AS total_spent
FROM customer cu
LEFT JOIN payment pa ON cu.customer_id = pa.customer_id
GROUP BY cu.customer_id, cu.first_name, cu.last_name
ORDER BY total_spent DESC
LIMIT 3;

-- Usar la vista de mejores clientes
SELECT * FROM top_customers;

-- Subconsulta para películas en inglés
SELECT title
FROM film
WHERE language_id = (
    SELECT language_id
    FROM language
    WHERE name = 'English'
);

-- Subconsulta para clientes con direcciones específicas
SELECT first_name, last_name, address_id
FROM customer
WHERE address_id IN (
    SELECT address_id
    FROM address
    WHERE address LIKE '1%'
);
