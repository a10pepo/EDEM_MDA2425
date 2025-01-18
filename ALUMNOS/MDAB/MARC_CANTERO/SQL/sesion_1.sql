---Búscame nombres de actores que empiecen por N


SELECT first_name, last_name,  actor_id
FROM actor
WHERE first_name like 'N%'


---Búscame nombres de actores que terminen en n


SELECT first_name, last_name,  actor_id
FROM actor
WHERE first_name like '%n'


---Búscame nombres de actores que contengan n


SELECT first_name, last_name,  actor_id
FROM actor
WHERE first_name ilike '%n%';


---Búscame nombres de actores que empiecen por N, luego tenga un carácter y luego cualquier cosa:


SELECT first_name, last_name,  actor_id
FROM actor
WHERE first_name ilike 'N_%'


---Contar el numero de actores:


SELECT count(first_name) as num_actores
FROM actor


---lista de nombres únicos de actores:

SELECT distinct first_name
FROM actor


---cuenta los nombres únicos


SELECT count(distinct first_name)
FROM actor


---lista titulos de pelicula donde coste sea mayor de 2, el titulo empiece por m y la duración entre 3 y 5 días 


SELECT title
FROM film
where replacement_cost >= 2 and title ilike 'm%' and rental_duration between 3 and 5


---vamos a calcular el numero de veces a partir del cual necesitaríamos alquilar una película para que saliera rentable

SELECT ceil(replacement_cost/rental_rate) as p_eq, title
FROM film
ORDER BY p_eq desc