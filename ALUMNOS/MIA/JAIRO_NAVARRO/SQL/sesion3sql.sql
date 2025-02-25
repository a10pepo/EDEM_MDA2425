--Cuántos actores tiene cada película
select  film.title,  count (actor.actor_id )  from film
 join film_actor  on film.film_id=film_actor.film_id
 join actor  on film_actor.actor_id=actor.actor_id
 group by film.title 
 ORDER BY film.title DESC ;   
 
 -- Cuáles són las películas que tienen + de dos actores
 select film.title, count (film_actor.actor_id) from film
  join film_actor  on film.film_id=film_actor.film_id
 join actor  on film_actor.actor_id=actor.actor_id
 group by film.title
 having count (film_actor.actor_id)>2 ;
 
 --Cuál es la película que tiene más actores ?
 select film.title, count(film_actor.actor_id) as numero_Actores from film
 join film_actor  on film.film_id=film_actor.film_id
 join actor  on film_actor.actor_id=actor.actor_id
 group by film.title
 order by numero_actores DESC
 LIMIT 1 ;
 
 
 Lista de Actores que salen en cada pelicula (nombre+apellidos)
Select a.title, ARRAY_AGG (b.first_name|| ' ' || b.last_name) actors 
from film a
left join film_actor c
	on a.film_id = c.film_id
left join actor b
	on c.actor_id = b.actor_id	
Group by a.film_id ;
 
 
 alter table reviews_gonzalo 
 add column review_stars int2 ;
 
 
 
 select * from reviews_gonzalo;
 
 alter table reviews_gonzalo 
 rename column review_description to review_opinion ;
 
 alter table reviews_gonzalo 
 alter column review_stars type int2 ;
 
 alter table reviews_gonzalo
 drop column review_stars;
 
 
 
 
 CREATE VIEW my_view_of_actor AS
 SELECT actor_id, first_name, last_name, last_update
 FROM public.actor
 where first_name is not null;
 
 create or replace my_view_of_actor as
  SELECT actor_id, first_name,last_name  || ' ' || b.last_name
 FROM public.actor
 where first_name is not null;
 ;
 
 select * from my_view_of_actor ;
 
 create view actores_por_peicula as
select  film.title,  count (actor.actor_id )  from film
 join film_actor  on film.film_id=film_actor.film_id
 join actor  on film_actor.actor_id=actor.actor_id
 group by film.title 
 ORDER BY film.title DESC ; 
 
 select * from actores_por_pelicula;
 
 alter view actores_por_peicula rename to actores_por_pelicula;
 
 create view tres_peores_clientes as
 select customer.first_name, customer.last_name ,sum (payment.amount) as gasto_por_cliente from customer
 join payment on customer.customer_id=payment.customer_id
 group by customer.first_name, customer.last_name
 order by gasto_por_cliente asc
 LIMIT 3;
 
 select * from tres_peores_clientes ;
 
 drop view tres_peores_clientes;
 
  create view tres_mejores_clientes as
 select customer.first_name, customer.last_name ,sum (payment.amount) as gasto_por_cliente from customer
 join payment on customer.customer_id=payment.customer_id
 group by customer.first_name, customer.last_name
 order by gasto_por_cliente desc
 LIMIT 3;
 
 --puedes hacer queries sobre vistas 
 --nunca crear vistas de vistas ( si no es necesario)
 -- union:para unir datos
 select * from tres_mejores_clientes
 union
 select * from tres_peores_clientes ;
 
 --Subconsultas en WHERE (muñecas rusas:una dentro de otra...)
 --subconsultas:se pueden meter en los where y en los from, y en el with
 -- es como si haces una consulta en la que coges de filtro otra consulta
 select actor.actor_id,actor.first_name,actor.last_name,actor.last_update from actor
 join film_actor on actor.actor_id=film_actor.actor_id
 join film on film_actor.film_id=film.film_id
 where title in 
 (select title from film where title ilike 'C%');

--Haz una subconsulta con WHERE  de las películas que están en inglés (sin usar join)
 select film.title from film
 where film.title in ( select language.name from language  where language.name='English');
 --puedes hacer un join o una subconsulta (depende lo que te pidan)
 
 select customer.first_name from customer
 where customer.address_id in 
 (select address.address_id from address where address.address  ilike '1%') ;
 
 
 -- Subconsultas con cláusula WITH
 with gasto_por_cliente as (
 select customer.first_name, sum(payment.amount) as gasto_por_cliente from customer
 join payment on customer.customer_id=payment.customer_id
 group by customer.first_name )
 select * from gasto_por_cliente where gasto_por_cliente>190;
 
 
 with gasto_por_cliente as(
 select customer.first_name,sum(payment.amount)as gasto_por_cliente from customer
  join payment on customer.customer_id=payment.customer_id
  group by customer.first_name )
  select count(first_name),sum(gasto_por_cliente) from gasto_por_cliente where gasto_por_cliente>190;