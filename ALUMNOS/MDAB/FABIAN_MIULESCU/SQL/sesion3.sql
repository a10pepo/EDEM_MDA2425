SELECT title, COUNT(fa.actor_id)
FROM film AS f
LEFT JOIN film_actor AS fa ON f.film_id = fa.film_id
GROUP BY title;

SELECT title, COUNT(fa.actor_id)
FROM film AS f
LEFT JOIN film_actor AS fa ON f.film_id = fa.film_id
GROUP BY title
HAVING COUNT(actor_id) > 2
ORDER BY COUNT ASC;

SELECT title, COUNT(fa.actor_id)
FROM film AS f
LEFT JOIN film_actor AS fa ON f.film_id = fa.film_id
GROUP BY title
ORDER BY COUNT DESC LIMIT 1;

ALTER TABLE IF EXISTS reviews
ADD COLUMN review_starts INT2;

ALTER TABLE IF EXISTS reviews
RENAME review_starts TO lolaso;

CREATE VIEW mas_actores AS 
SELECT title, COUNT(fa.actor_id)
FROM film AS f
LEFT JOIN film_actor AS fa ON f.film_id = fa.film_id
GROUP BY title
ORDER BY COUNT DESC LIMIT 1;

SELECT * FROM mas_actores;

CREATE VIEW mejores_clientes AS
SELECT cu.customer_id, first_name, last_name, SUM(pa.amount)
FROM customer AS cu
LEFT JOIN payment AS pa ON cu.customer_id = pa.customer_id
GROUP BY cu.customer_id, first_name, last_name
ORDER BY SUM DESC LIMIT 3;

SELECT * FROM mejores_clientes;

CREATE VIEW peores_clientes AS
SELECT cu.customer_id, first_name, last_name, SUM(pa.amount)
FROM customer AS cu
LEFT JOIN payment AS pa ON cu.customer_id = pa.customer_id
GROUP BY cu.customer_id, first_name, last_name
ORDER BY SUM ASC LIMIT 3;

SELECT * FROM peores_clientes;

SELECT * FROM mejores_clientes
UNION
SELECT * FROM peores_clientes
ORDER BY SUM ASC;

SELECT film_id, title 
FROM film 
WHERE language_id IN (
    SELECT language_id
    FROM language 
    WHERE name = 'English'
);