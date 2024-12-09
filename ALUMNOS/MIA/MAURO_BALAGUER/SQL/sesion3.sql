--- sesion 3
SELECT 
    f.title AS "Film Title", 
    COUNT(fa.actor_id) AS "Actor Count"
FROM 
    film f
INNER JOIN 
    film_actor fa ON f.film_id = fa.film_id
GROUP BY f.title
order by f.title



-- CUALES SON LAS PELIS CON MAS DE 2 ACTORES
SELECT 
    f.title AS "Film Title", 
    COUNT(fa.actor_id) AS "Actor Count"
FROM 
    film f
INNER JOIN 
    film_actor fa ON f.film_id = fa.film_id
GROUP BY 
    f.title
HAVING 
    COUNT(fa.actor_id) > 2
ORDER BY 
    COUNT(fa.actor_id) DESC;
	
-- PELICULA CON MAS ACTORES, LIMITAR A UNO DESCENDIENTE
SELECT 
    f.title AS "Film Title", 
    COUNT(fa.actor_id) AS "Actor Count"
FROM 
    film f
INNER JOIN 
    film_actor fa ON f.film_id = fa.film_id
GROUP BY 
    f.title
ORDER BY 
    COUNT(fa.actor_id) DESC
LIMIT 1;

--- Lista de Actores que salen en cada pelicula
Select a.title, ARRAY_AGG (b.first_name|| ' ' || b.last_name) actors 
from film a
left join film_actor c
	on a.film_id = c.film_id
left join actor b
	on c.actor_id = b.actor_id	
Group by a.film_id

-- ALTER TABLE
ALTER TABLE staff
DROP COLUMN family_problems;

select *
from staff

--- CREAR VISTA
CREATE VIEW mauro_balaguer AS
SELECT 
    a.first_name || ' ' || a.last_name AS "Actores",
    f.title AS "Peliculas"
FROM 
    actor a
JOIN 
    film_actor fa ON a.actor_id = fa.actor_id -- Relaciona actores con películas
JOIN 
    film f ON fa.film_id = f.film_id -- Relaciona la película con la tabla 'film'
ORDER BY 
    f.title DESC;

SELECT * FROM mauro_balaguer;

SELECT * 
FROM mauro_balaguer
WHERE "Actores" = 'Lisa Monroe'
ORDER BY "Peliculas" DESC;

-- Muestra solo los 3 mejores clientes
CREATE VIEW best_customers AS
SELECT 
    c.customer_id,
    c.first_name || ' ' || c.last_name AS "Customer Name",
    SUM(p.amount) AS "Total Spent"  -- Asumiendo que 'amount' es el monto de pago
FROM 
    customer c
JOIN 
    payment p ON p.customer_id = c.customer_id  -- Relaciona clientes con sus pagos
GROUP BY 
    c.customer_id, c.first_name, c.last_name  -- Agrupa por cliente
ORDER BY 
    "Total Spent" DESC  -- Ordena por el total gastado, de mayor a menor
LIMIT 3;  

SELECT *
FROM best_customers

-- Muestra solo los 3 peores clientes
CREATE VIEW worst_customers AS
SELECT 
    c.customer_id, c.first_name || ' ' || c.last_name AS "Customer Name",
    SUM(p.amount) AS "Total Spent"  -- Asumiendo que 'amount' es el monto de pago
FROM 
    customer c
JOIN 
    payment p ON p.customer_id = c.customer_id  -- Relaciona clientes con sus pagos
GROUP BY 
    c.customer_id, c.first_name, c.last_name  -- Agrupa por cliente
ORDER BY 
    "Total Spent" ASC  -- Ordena por el total gastado, de mayor a menor
LIMIT 3;  

select *
from worst_customers

select * from best_customers
union
select * from worst_customers
order by "Total Spent" DESC

-- sacar todas las peliculas en ingles, con subconsulta WHERE
SELECT f.title
from film f

WHERE language_id IN 
(SELECT language_id
	  from language l
	  where l.name = 'English')
	  
SELECT f.title,l.name -- select count(*)
from film f
JOIN language l on f.language_id = l.language_id
WHERE l.name = 'English'

select *
from language

WITH clientes_mas_190_gasto AS
(
SELECT
	c.first_name || ' ' || c.last_name AS "Client Name", 
	SUM(p.amount) AS Total_Spent
FROM 
	customer c
JOIN 
	payment p ON c.customer_id = p.customer_id
GROUP BY 
	c.first_name, c.last_name, c.customer_id
ORDER BY 
	Total_Spent DESC
) 
SELECT * FROM clientes_mas_190_gasto
WHERE Total_Spent > 190