SELECT actor_id,first_name, last_name, last_update 
from actor
WHERE first_name = 'Ed' or first_name = 'Nick';
-- nombre que es o nick o ed 

SELECT first_name
from actor
where first_name LIKE 'N%';
-- nombre que empieza por n

SELECT first_name
from actor
where first_name iLIKE '%n%'  ;
-- nombre que contenga n ilike especial

SELECT first_name
from actor
where first_name LIKE 'N_%' ;
-- 

SELECT last_name
from actor
where last_name is NULL ;
--que no tenga apellido

SELECT actor_id
count 
FROM actor  ;
-- cuantos actores tengo

SELECT count (actor_id) as actores_total
FROM actor ;
--renombrado columna

SELECT count (distinct first_name) as nombre_unico
FROM actor ;
--nombres unicos que tienen actores

Select max (distinct first_name) 
from actor ;
--maximo nombre de un actor

select replacement_cost
from film
where replacement_cost >2 ;
-- replacemtnt cos mayor a 2 euros

select replacement_cost, title
from film
where replacement_cost >2 and title ilike 'J%' ;
-- replacement cost mayor de 2 y que empiece por la J

select replacement_cost, title, rental_duration
from film
where replacement_cost >2 and title ilike 'J%' and rental_duration between  0 and 5 ;
-- replacement cost mayor de 2 y que empiece por la J y mayor duracion alquiler entre 0 y 5

select replacement_cost, title, rental_duration, release_year, length, rental_rate
from film
where replacement_cost >2 and title ilike 'J%' and rental_duration between  0 and 5 and release_year = 2006 and length >100 and rental_rate >2 ;
-- replacement cost mayor de 2 y que empiece por la J y mayor duracion alquiler entre 0 y 5 y pelicula 2006 y duracion mayor de 100 m y rental rate mayor de 200

Select title, ceil(replacement_cost/rental_rate) as breakeven
From film order by breakeven desc;
-- cuando comienza una pelicula a ser rentable en order descendiente

Select * from film
where special_features [1] ilike 'T%'  ;
-- primera feature empieza por T

SELECT rating, COUNT(*) AS title
FROM film
GROUP BY rating ;
-- numero de peliculas

SELECT rating, AVG(rental_rate) AS avg_rental_rate
FROM film
GROUP BY rating ;
--precio medio de alquiler

SELECT rating, MIN(rental_rate) AS min_rental_rate
FROM film
GROUP BY rating ;
-- minimo precio de alquiler

SELECT rating, MAX(rental_rate) AS max_rental_rate
FROM film
GROUP BY rating ;
-- maximo precio de alquiler

SELECT rating, avg(length) AS avg_length
FROM film
GROUP BY rating ;
-- duracion media de peliculas

SELECT rating, min(release_year) AS min_release_year
FROM film
GROUP BY rating ;
-- anio pelicula mas antigua

SELECT rating, max(release_year) AS max_release_year
FROM film
GROUP BY rating ;
-- anio pelicula mas nueva

SELECT rating, count(*) AS num_movies
FROM film
GROUP BY rating 
having count(*) > 200;
-- numero de peliculas y quedate con aquellos rating que tengan mas de 200 peliculas

SELECT rating, avg(rental_rate) AS avg_rental_rate
FROM film
GROUP BY rating 
having avg(rental_rate) > 3;
-- precio medio de alquiler y solo los rating con un precio medio superior a 3

SELECT rating, avg(length) AS avg_length
FROM film
GROUP BY rating 
having avg(length) > 115 ;
-- duracion media de peliculas y aquellos raring con duracion media mayor a 115

SELECT *
FROM film
LEFT JOIN language ON film.language_id = language.language_id ;
-- relacionar film con language a traves del id

SELECT film.title, language.name
FROM film
LEFT JOIN language ON film.language_id = language.language_id ;
-- select titulo de la pelicula y el idioma en el que esta

SELECT film.title, actor.first_name
FROM film
LEFT JOIN film_actor ON film.film_id = film_actor.actor_id
LEFT JOIN actor ON film.film_id = actor.actor_id ;
-- doble join

SELECT film.film_id, film.title, COUNT(actor.actor_id) AS num_actors
FROM film
LEFT JOIN film_actor ON film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
GROUP BY film.film_id, film.title
order by film_id ;
-- conteo por pelicula de los actores que participan en las peliculas

SELECT film.film_id, film.title, COUNT(actor.actor_id) AS num_actors
FROM film
LEFT JOIN film_actor ON film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
GROUP BY film.film_id, film.title
having count(actor.actor_id) >5
order by num_actors ;
-- conteo por pelicula de los actores que participan en las peliculas mayor a 10 actores

SELECT actor.actor_id, actor.first_name, COUNT(film.film_id) AS num_movies
FROM actor
LEFT JOIN film_actor ON actor.actor_id = film_actor.actor_id
LEFT JOIN film ON film_actor.film_id = film.film_id
GROUP BY actor.actor_id, actor.first_name
order by num_movies ;
-- actores y su numero de peliculas

create table if not exists reviews_jz(
	film_id serial4 NOT NULL,
	customer_id varchar(50) NOT NULL,
	review_date timestamp NOT NULL,
	review_description varchar
) ;
-- crear tabla

INSERT into reviews_jz (film_id, customer_id,review_date, review_description)
VALUES ('4', 7, '2023-10-11', 'La Pelicula es un poco aburrida') ;
-- insertar datos en la tabla

CREATE TABLE reviews
(	film_id serial4 not null,
	customer_id varchar(50) not null,
	review_date date not null,
	review_description varchar(50) not null)

ALTER TABLE reviews
ADD COLUMN review_stars int2
--añadir tabla

SELECT * FROM reviews

ALTER TABLE reviews
RENAME COLUMN review_description
TO review_opinion
--cambiar el nombre de una tabla

CREATE VIEW my_view_of_actor AS
SELECT actor_id, first_name, last_name, last_update FROM public.actor
where first_name IS NOT null

select * from juan_montoliu

CREATE VIEW juan_montoliu AS
SELECT film_id, title, description FROM public.film
where title is not null

CREATE VIEW mejor_cliente AS
SELECT customer.customer_id, payment.amount
FROM customer   
LEFT JOIN payment on customer.customer_id = payment.customer_id

CREATE VIEW top_tres AS
SELECT customer.customer_id, sum(payment.amount) as total_payment
FROM customer 
LEFT JOIN payment on customer.customer_id = payment.customer_id
GROUP BY customer.customer_id
ORDER BY total_payment DESC

SELECT film_id, title, release_year, rating
FROM public.film
WHERE film_id in (select film_id from
public.film where title ilike 'C%')

SELECT film_id, title, release_year, rating
FROM public.film
WHERE film_id in (select film_id from
public.film where title ilike 'C%')

SELECT * from customer
where address_id in (
select address_id from address where address ilike '1%'
)

with my_sub_query as
(SELECT title, rental_rate, replacement_cost,
round(replacement_cost / rental_rate, 2) as ratio
FROM public.film)
select * from my_sub_query where title = 'Ali Forever'

WITH high_payers AS 
(SELECT customer_id, SUM(amount) AS total_amount
FROM public.payment
GROUP BY customer_id
HAVING SUM(amount) > 190)
SELECT SUM(total_amount) AS total_amount_for_high_payers
FROM high_payers;
