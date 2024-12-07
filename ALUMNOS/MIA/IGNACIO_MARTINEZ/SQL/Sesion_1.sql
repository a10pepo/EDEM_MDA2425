select actor_id, first_name, last_name, last_update
from actor
WHERE first_name = 'Ed' or first_name='Nick';

select * from actor
where first_name like 'N%'

--Si pones %N% busca cualquier N mayuscula en los nombres. en el caso de poner 'n%' busca los nombres que empiezan por N
--En el caso de '%n' busca las n al final de la palabra.

select * from actor
where first_name like '%n'

-- Que comiencen por la N que despues haya un caracter y luego cualquier otra cosa (ilike para que de igual minusculas y mayusculas)

select * from actor
where first_name ilike 'n_%'

--Cuantos actores tengo en mi base de datos

Select count (*) from actor

--Nombre único de todos los que hay

select distinct (first_name) from actor

select count (distinct (first_name)) from actor

--Peliculas que cuesten menos de 2€ y que empiecen por la letra N y que dure entre 0-5 dias el alquiler, que sea del 2006, duracion mayor de 100 m.

Select title from film where rental_rate >2 
	And title LIKE 'N%' 
	And rental_duration between 0 and 5 
	And release_year = 2006 
	And film.length >=100
	
--Cuantas veces tengo que alquilar una pelicula para que me salga rentable su coste
	
SELECT title, replacement_cost, rental_rate, 
       CEIL(replacement_cost / rental_rate) AS veces_alquiler_necesarias
FROM film
order by (veces_alquiler_necesarias) desc

select special_features [1] from film
where replacement_cost >2;
