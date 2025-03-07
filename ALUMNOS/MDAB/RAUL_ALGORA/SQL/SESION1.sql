SELECT actor_id, first_name, last_name, last_update FROM actor 
WHERE first_name = 'Ed' or first_name = 'Nick';

select actor_id, first_name, last_name from actor
where first_name ilike '%n'; --Para seleccionar los nombres que acaben en n--

select actor_id, first_name, last_name from actor
where first_name like 'N_%';--Para que te saque los que empiezan por n pero obligando que despues haya un caracter.

select actor_id, first_name, last_name from actor
where last_name is null -- Hay algun actor que no tenga apellido?

select count (first_name) as total_actores from actor --Para contar el numero de actores

select count ( distinct first_name) as nombres_unicos from actor --para contar el numero dfe nombres unicos 

select first_name from actor 
order by first_name ASC

select max(distinct first_name)

select * from film

select title from film
where replacement_cost >2 
AND title like'R%'
AND rental_duration >3

select * from film
where replacement_cost >2 
AND rental_duration between 0 and 5
AND release_year >= 2006
AND length >100
AND rental_rate > 2;

select title , ceil(replacement_cost / rental_rate) as punto_equilibrio 
from film order by punto_equilibrio DESC

select special_features[1] from film
where replacement_cost > 2
