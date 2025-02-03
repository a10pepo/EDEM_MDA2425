select *
from actor
where first_name like 'A%';

select title
from film
where rental_rate >10;

select *
from film
where rental_rate between 5 and 10;

select *
from film
where rental_rate <5
and rental_duration <100;

select rental_rate
from film
where title='Giant Troopers';

select rating
from film
where title like 'Ali%'
and rental_duration;

select title
from film
order by rental_duration desc;

select lenght 
from film as f
order by lenght desc
limit 5;


select rental_rate, count(*)
from film
group by rental_rate;

--Ejercicio
SELECT rating,
       count(title),
       round(avg(rental_rate),2) as Precio_medio,
       min(rental_rate),
       max(rental_rate),
       round(avg(length),2) as Duracion_media,
       max(release_year),
       min(release_year)
FROM film
GROUP BY rating;


--Ejercicio 2
SELECT rating,
       count(title),
       round(avg(rental_rate),2) as Precio_medio,
       min(rental_rate),
       max(rental_rate),
       round(avg(length),2) as Duracion_media,
       max(release_year),
       min(release_year)
FROM film
GROUP BY rating
HAVING avg(length) >110;

--Ejercicio 3

SELECT rating,
       count(title) as Total_peliculas,
	   round(avg(rental_rate),2)as Precio_medio,
	   round(avg(length),2) as Duracion_media 	    
FROM film
GROUP BY rating
HAVING count(title) >200
and avg(rental_rate)>3
and avg(length) >115;

--Ejercicios Joins

select upper(c.first_name),upper(last_name), a.address
From customer c
left join address a on c.address_id=a.address_id;

--Ejercicio
select upper(c.first_name),upper(last_name), a.address, d.city, e.country
From customer c
left join address a on c.address_id=a.address_id
left join city d on a.city_id=d.city_id
left join country e on d.country_id=e.country_id


--Ejercicio

SELECT f.title, a.first_name, a.last_name 
FROM film f
left join film_actor fa on f.film_id=fa.film_id
left join actor a on fa.actor_id=a.actor_id
where a.last_name like 'C%';

--Ejercicio dificil

SELECT f.title, count(a.actor_id)
FROM film f
left join film_actor fa on f.film_id=fa.film_id
left join actor a on fa.actor_id=a.actor_id
where a.last_name like 'C%'
Group by 1
having count(a.actor_id)=1;

--Ejercicios

SELECT f.title, count(a.actor_id) as actor_account
FROM film f
left join film_actor fa on f.film_id=fa.film_id
left join actor a on fa.actor_id=a.actor_id
Group by f.title
order by actor_account desc;

SELECT f.title, count(a.actor_id) as Actores_Totales
FROM film f
left join film_actor fa on f.film_id=fa.film_id
left join actor a on fa.actor_id=a.actor_id
Group by f.title
having count(a.actor_id)>2
order by Actores_Totales desc;


SELECT f.title, count(a.actor_id) as Max_actors
FROM film f
left join film_actor fa on f.film_id=fa.film_id
left join actor a on fa.actor_id=a.actor_id
group by f. title
order by Max_actors desc
limit 1;


--Crear tabla

CREATE TABLE IF NOT EXISTS public.reviews (
film_id integer NOT NULL,
customer_id integer NOT NULL,
review_date timestamp not null default now(),
review_description varchar(50),
CONSTRAINT reviews_pkey PRIMARY KEY (film_id, customer_id)
	);

select *
from reviews;

--Añadir valores 
INSERT INTO reviews (film_id, customer_id, review_description)
values(1, 1,'Muy buena pelicula' );

--Update

update reviews
set review_description ='Es muy mala'
where film_id=1;

--Delete parte de una tabla

delete
from reviews
where review_description='Es muy mala'

--Borrar tabla
drop table public.reviews