--- GROUP BY , EJERCICIO 6
select rating, count(rating)
FROM film
group by rating

select rating, round(avg(rental_rate),2)
FROM film
group by rating

select rating, min(rental_rate)
FROM film
group by rating

select rating, max(rental_rate)
FROM film
group by rating

select rating, round(avg(length),0)
FROM film
group by rating

select rating, min(release_year)
FROM film
group by rating

select rating, max(release_year)
FROM film
group by rating

--- HAVING , EJERCICIO 7

SELECT rating
from film
group by rating
having count(rating) > 200

SELECT rating, round(avg(rental_rate),2)
from film
group by rating
having round(avg(rental_rate),2) > 3

SELECT rating, round(avg(length),0)
from film
group by rating
having round(avg(length),0) > 115

--- JOIN

select f.title, l.name
from film f
left join language l on l.language_id = f.language_id;

select f.title, l.name
from language l
left join film f on f.language_id = l.language_id;

--- JOIN VARIOS para todas las películas, ¿qué actores participan?

select f.title, ac.first_name, ac.last_name
from film f
left join film_actor fa on fa.film_id = f.film_id
left join actor ac on ac.actor_id = fa.actor_id

--- ¿para cada pelicula dame numero de actores?

select f.title, count(ac.first_name)
from film f
left join film_actor fa on fa.film_id = f.film_id
left join actor ac on ac.actor_id = fa.actor_id
group by f.title
order by count(ac.first_name) desc

--- ¿cual sería la pelicula con mas de 30 actores?

select f.title, count(ac.first_name)
from film f
left join film_actor fa on fa.film_id = f.film_id
left join actor ac on ac.actor_id = fa.actor_id
group by f.title
having count(ac.first_name) > 30
order by count(ac.first_name) desc

--- ¿para cada actor dame numero de peliculas?

select ac.first_name, ac.last_name, count(f.title)
from film f
left join film_actor fa on fa.film_id = f.film_id
left join actor ac on ac.actor_id = fa.actor_id
group by ac.actor_id
order by count(f.title) desc

--- CREAR UNA TABLA

create table review_marc(
	film_id int NOT NULL,
	customer_id int NOT NULL,
	review_date timestamp NOT NULL,
	review_desciption varchar(50)
);

--- INSERTAR VALORES EN LA TABLA CREADA
insert into review_marc(film_id, customer_id, review_date,review_desciption)
values (4,7,'10-11-2023','la pelicula es un poco aburrida')

--- REVISAR LO INSERTADO

select *
from review_marc