'''numero de peliculas'''
Select count(title), rating from film group by rating 


'''media de precio de alquiler'''
select round (avg(rental_rate),2) rating from film group by rating

'''precio mínimo de alquiler'''
select MIN(rental_rate), rating from film group by rating

'''precio maximo de alquiler'''
select MAX(rental_rate), rating from film group by rating

'''duración media del alquiler'''
select AVG(length), rating from film group by rating

'''Año de la pelicula mas vieja'''
select MIN(release_year), rating from film group by rating

'''Año de la pelicula mas nueva'''
select MAX(release_year), rating from film group by rating;

'''numero de peliculas y quedate solo con aquellos rating que tenga mas de 200 peliculas'''
Select count(title), rating from film 
group by rating
having count(title) >200;

'''EL precio medio de alquiler y quedate solo con aquellos rating que tengan un precio medio superior a 3'''
Select round(AVG(rental_rate),2), rating from film 
group by rating
having AVG(rental_rate) >3;

'''la duración media de las peliculas y quedate solo con aquellos rating que tengan una duracion media superior a 115 min'''
Select round(AVG(length),2), rating from film 
group by rating
having AVG(length) >115;

'''CLAUSULA JOIN'''

select title, b.name
from film a
left join language b on a.language_id = b.language_id


select a.title, b.film_id, count (c.actor_id) as num_actors
from film a 
left join film_actor b on a.film_id = b.film_id
left join actor c on c.actor_id = b.actor_id
group by b.film_id, a.title
having count (c.actor_id) >5

'''conteo por pelicula de los actores que participan en cada pelicula'''
select c.first_name, count(a.film_id) as numero_peliculas
from film a 
left join film_actor b on b.film_id = a.film_id
left join actor c on actor_


'''conteo por actor las peliculas que ha hecho'''
SELECT c.first_name, COUNT(a.film_id) AS numero_peliculas
FROM film a 
LEFT JOIN film_actor b ON b.film_id = a.film_id
LEFT JOIN actor c ON c.actor_id = b.actor_id
GROUP BY c.first_name
ORDER BY count (a.film_id)desc 

'''crear una tabla'''

create table if not exists review_ra (
	film_id varchar(50) not null,
	customer_id serial4 not null,
	review_date timestamp not null,
	review_description varchar(50) not null
)

select * from review_ra

'''cláusula insert'''
INSERT into review_ra (film_id, customer_id, review_date, review_description)
values ('4', '7', '10-11-2023','la pelicula es un poco aburrida')

'''Para modificar registros de la tabla'''

UPDATE review_ra
SET review_description = 'no era tan mala'

