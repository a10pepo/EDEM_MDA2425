--sacar con rating(columna) el numero total de peliculas
SELECT rating, count (*) as numero_peliculas
from film
group by rating
order by numero_peliculas desc
having count(title) > 200;

--obten por rating el precio medio de alquiler
select rating, round(avg(rental_rate)) as precio_medio
from film
where (rental_rate)>3
group by rating ;
--obten por rating el precio minimo del alquiler
select rating, round(min(rental_rate)) as precio_minimo
from film
group by rating ;

select rating, count (title)as titulo , round(max(rental_rate))
from film
group by rating ;

select rating, avg(rental_duration)as duracion_media 
from film
group by rating
order by duracion_media DESC
having count (rental_duration)>10;

--mirar clausula JOIN, SQL JOINS

--clausula JOIN
--relacionar film con language

select a.language_id , b.language_id
from film a
left join language b on a.language_id=b.language_id;


select a.title, b.name
from film a
left join language b on a.language_id=b.language_id;


select rating, min(release_year)as película_mas_antigua
from film
group by rating ;

select rating, max(release_year) as pelicula_mas_nueva
from film
group by rating;

--having : filtros en los group by (having= where)

--TABLAS= A:film , B:

SELECT rating, count(rating) from film group by rating;
SELECT rating, round(avg(rental_rate)) from film group by rating ;
SELECT rating, round(min(rental_rate)) from film group by rating ;
SELECT rating, round(max(rental_rate)) from film group by rating ;
SELECT rating, round(avg(length)) from film group by rating ;
SELECT rating, min(release_year) from film group by rating ;
SELECT rating, max(release_year) as pelicula_mas_nueva from film group by rating ;

-- Obten por rating, el nº peliculas y quédate unicamente con aquellos rating 
-- más de 200 películas --
SELECT rating, count(rating) as n_peliculas from film group by rating having count(title)>200  ;

SELECT rating, round(avg(rental_rate)) as precio_medio from film group by rating having count(rental_rate) > 3;

--Clausula JOIN--

SELECT a.language_id, b.language_id
FROM film a
LEFT JOIN language b on a.language_id = b.language_id;

SELECT a.title, b.name
FROM film a
LEFT JOIN language b on a.language_id = b.language_id ;

SELECT a.title, b.name
FROM film a
RIGHT JOIN language b on a.language_id = b.language_id;

select *
from film b
right join  language l on b.language_id = l.language_id;

-- Ahora un join con 3 tablas -- 
select f.title, a.first_name
FROM film f
LEFT join film_actor fa on f.film_id = fa.film_id
LEFT join actor a on fa.actor_id = a.actor_id
where first_name = 'Penelope';

-- Conteo de cuantos actores tiene cada película 
SELECT f.title, COUNT(a.actor_id) as n_actores
FROM film f
LEFT JOIN film_actor fa ON f.film_id = fa.film_id
LEFT JOIN actor a ON fa.actor_id = a.actor_id
GROUP BY f.title having count(a.actor_id) < 5 -- Having es una forma de filtrar dentro de un groupby

-- Cuantas películas ha hecho cada actor
SELECT a.first_name, COUNT(f.title) as n_peliculas
FROM film f
LEFT JOIN film_actor fa ON f.film_id = fa.film_id
LEFT JOIN actor a ON fa.actor_id = a.actor_id
GROUP BY a.first_name;


-- https://sqlformat.com
--Optmización de las columnas o los datos que queramos en las querys, como se ve eso en google cloud

--Creación de tablas

CREATE TABLE IF NOT EXISTS reviews_eaz(
	film_id serial4 NOT NULL,
	customer_id serial4 NOT NULL,
	review_date date NOT NULL,
	review_description varchar(255) NOT NULL,
	CONSTRAINT reviews_eaz_pkey PRIMARY KEY (film_id,customer_id)
);
select *
from reviews_gonzalo ;

Update reviews_gonzalo 
set film_id='5'
where film_id='4';

--inner join : coincidencias en ambas tablas
