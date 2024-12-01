
Select actor_id, first_name, last_name
from actor
where first_name LIKE 'N%' ;
-- aqui seria todos los nombres que empiecen por N

Select actor_id, first_name, last_name
from actor
where first_name LIKE '%n' ;
--aqui seria todos los nombres que terminen en n

Select actor_id, first_name, last_name
from actor
where first_name LIKE 'N%n';
--aqui seria todos los nombres que empiecen por n y que terminen en n

Select actor_id, first_name, last_name
from actor
where first_name ILIKE '%n%';
--aqui no distingue que contenga n en el medio sino que todo aquello que contenga n

Select actor_id, first_name, last_name
from actor
where first_name ILIKE 'N_%';
--que empiecen por n y que luego contengan un caracter, al poner la _ es que tiene que ser un codigo alfanumerico despues de N,

Select first_name, last_name
from actor 
where last_name is null;
--de esta forma comprobamos si tenemos algun apellido en vacio 

Select count(actor_id) 
from actor;
--contar cuantos valores tenemos en actor_id

Select count(actor_id) as conteo_actores
from actor;
--de esta forma cambiamos el nombre de la tabla a conteo_actores para que se entienda mejor 

Select DISTINCT first_name 
from actor;
--nombre de actores solo 

SELECT count(DISTINCT first_name) 
from actor;
--solo el conteo de nombres diferentes

SELECT  MAX(first_name)
from actor;
--sacar el nombre que este mas cercao a la z(la letra mas lejos en el alfabeto)


--ahora trabajaremos con la tabla film 
select *
from film 
where replacement_cost >2;
--pelicula con rcost mayor a dos 

select *
from film 
where replacement_cost>2 
and title ilike 'v%';
--pelicula con rcost mayor a dos y titulo que empieze por v 

select *
from film 
where replacement_cost>2 
and title ilike 'v%' 
and rental_duration >3; 
--pelicula con rcost mayor a dos y titulo que empieze por v y que tengan rental duration mayor a 3 


select *
from film 
where replacement_cost>2 
and title ilike 'v%' 
and rental_duration >= 3 and rental_duration <=5;

select *
from film 
where replacement_cost>2 
and title ilike 'v%' 
and rental_duration between 3 and 5;
--pelicula con rcost mayor a dos y titulo que empieze por v y que tengan rental duration mayor a 3 y menor a 5 

select *
from film 
where replacement_cost>2 
and title ilike 'v%' 
and rental_duration between 3 and 5
and release_year = 2006
and length>100;
--pelicula con rcost mayor a dos y titulo que empieze por v y que tengan rental duration mayor a 3 y menor a 5 y que siga mes llarga de 100 mins 

select title, CEIL(replacement_cost/rental_rate) as break_even
from film; 
--sacar el punto de equilibrio de cuantas veces tengo que alquilar la peli para que se cubra el coste de esta

select title, CEIL(replacement_cost/rental_rate) as break_even
from film
ORDER BY break_even DESC;
--sacar el punto de equilibrio de cuantas veces tengo que alquilar la peli para que se cubra el coste de esta
--en orden de mayor a menor preocupacion 

select title, CEIL(replacement_cost/rental_rate) as break_even
from film
ORDER BY break_even ASC;
--las mejores peliculas

select * from film 
where special_features[1] ilike 't%';
-- buscar que los special empiezan por t 
