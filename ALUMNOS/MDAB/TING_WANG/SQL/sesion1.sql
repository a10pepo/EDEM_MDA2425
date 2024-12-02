--SELECT * FROM actor
-- WHERE first_name = 'Ed' or first_name = 'Nick';
-- WHERE first_name ILIKE '%n%';
-- WHERE first_name ILIKE 'N_%';
--WHERE last_name is null
--SELECT count(actor_id) as Total_Actores from actor 
-- SELECT DISTINCT first_name FROM actor;
--SELECT COUNT(DISTINCT first_name) FROM actor;
--SELECT max(first_name) FROM actor; 
--SELECT first_name FROM actor ORDER BY first_name DESC

SELECT * FROM film
where replacement_cost > 2 
and title ilike 'T%' 
-- and rental_duration > 2
and rental_duration BETWEEN 0 and 5
and release_year = 2006
and length > 100
and rental_rate > 2;

SELECT title, rental_rate, replacement_cost, ceil(replacement_cost / rental_rate) 
as breakeven from film ORDER BY breakeven DESC;

select special_features[1] from film
where replacement_cost >2;

select * from film
where special_features[2] ilike 'D%';
