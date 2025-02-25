select * from actor 
where first_name = 'Ed' or first_name = 'Nick';

--que comiencen por N
select * from actor
where first_name iLike 'n%';

--que terminen por N
select * from actor
where first_name iLike '%N';

-- que comiencen por N, tenga caracter y luego tenga otra cosa
select * from actor
where first_name ilike 'n_%';

-- que no tengan apellido/ tengan apellido is/is not
select * from actor;
where first_name is not null;
--conteo
select count (last_name) from actor;
-- as l
select count (last_name) as l from actor;
-- nombres unicos de actors
select distinct (first_name) from actor;

select count (distinct (first_name)) from actor ;


-- peliculas que cuesten menos de 5 euros
select title from film where rental_rate < 5;

select title, replacement_cost, rental_duration, release_year 
from film  
where replacement_cost > 2 and title ilike 'n%' and release_year = 2006  
and rental_duration between 0 and 5  
and film.length >= 100
and rental_Rate >2;

--cuantas veces se debe alquilar una pelicula para que salga rentable

select title, rental_Rate, CEIL(replacement_cost / rental_rate) as vecesalquilernecesarias from film
order by (vecesalquilernecesarias) desc;

select * from film

select * from film
where special_features[2] ilike 'D%'