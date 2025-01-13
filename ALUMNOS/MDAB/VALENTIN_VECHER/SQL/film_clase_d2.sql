select rating, (count(film_id)) as n_de_pelis_por_rating 
from film 
Group by rating;
--agrupa el numero de pelis por su rating 

select rating, count(film_id) as n_pelis, ROUND(avg(rental_rate),2) as p_medio_alq, ROUND(min(rental_rate),2) as p_min, ROUND(max(rental_rate),2) as p_max, count(rating) as num_de_pelis
from film
group by rating;
--agrupar por rating, num de pelis, el precio medio de alquiler, precio minimo y precio maximo 

select rating, (round(avg(length),4)) as avg_duration, max(release_year) as peli_m_nuevas, min(release_year) as peli_m_vieja
from film 
group by rating;
--agrupar por duracion media, peli mas nueva y mas vieja 

--having sirve para buscar en los grupos, son filtros solo para los group by 

select rating, count(film_id) as n_pelis, ROUND(avg(rental_rate),2) as p_medio_alq, ROUND(min(rental_rate),2) as p_min, ROUND(max(rental_rate),2) as p_max, count(rating) as num_de_pelis
from film
group by rating
having count(film_id)>200;
-- seleccionar aquellos rating que tengan mas de 200 pelis 

select rating, count(film_id) as n_pelis, ROUND(avg(rental_rate),2) as p_medio_alq, ROUND(min(rental_rate),2) as p_min, ROUND(max(rental_rate),2) as p_max
from film
group by rating
having ROUND(AVG(rental_rate),2)>3;
--el precio medio del alquiler y quedate unicamente con aquellos rating que tebnga un precio medio superior a tres 


select rating, (round(avg(length),4)) as avg_duration, max(release_year) as peli_m_nuevas, min(release_year) as peli_m_vieja
from film 
group by rating
having (round(avg(length),4))>115;
--duracion mas larga de 115 minutos 

-- clausulas join : relacionar entre tablas que tengan la misma variable 

select language.name, film.title
from language
right join film  on language.language_id = film.language_id;
--asi no salen los idiomas que no existen solo me lista las peliculas

select language.name, film.title 
from language 
left join film on language.language_id=film.language_id;
--where title is not null si ponemos esto los nulos no salen 
--asi salen todos los idiomas a pesar de tener o no idioma 

select film.title as titulo_peli, film_actor.actor_id , actor.first_name as nombre_actor
from film 
left join film_actor on film.film_id=film_actor.film_id 
left join actor on film_actor.actor_id =actor.actor_id;
--where film_actor is not null: asi para que no salgan nulos 
--por cada actor en cuantas pelis ha salido 

select film.title as titulo_pelicula, count(actor.actor_id) as num_actores
from film_actor
left join film on film_actor.film_id=film.film_id 
left join actor on film_actor.actor_id=actor.actor_id
group by film.title
--vamos a contar por pelicula cuantos actores poarticipan 

select film.title as titulo_pelicula, count(actor.actor_id) as num_actores
from film_actor
left join film on film_actor.film_id=film.film_id 
left join actor on film_actor.actor_id=actor.actor_id
group by film.title 
having count(actor.actor_id)>6
--asi sacamos todos lo que tengan mas de 6 actores 

select actor.first_name as nombre_actor, count(film.film_id) as num_pelis 
from film_actor
left join actor on film_actor.actor_id=actor.actor_id
left join film on film_actor.film_id=film.film_id 
group by actor.first_name 
order by  actor.first_name ASC
-- ordenado alfabeticamente el njumero de pelis por actor 

--crear una tabla 
create table if not exists reviews_buena(
	film_id serial4 not null, 
	customer_id varchar(50) not null, 
	review_date varchar(50) not null,
	review_description varchar(50) not null
);

select * from reviews_buena;

--insertar los datos 
Insert into reviews_buena
Values 
(4, 7, '10-11-2023', 'la pelicula es un poco aburrida');

select * from reviews_buena;

--borrar los datos 
--DELETE FROM nombre_tabla
--WHERE condicion;

--updatear los datos para cambiarlos 
--update tabla 
--set variable= 'nuevo valor'
--where variable (id_producto) = 'id del necesario'