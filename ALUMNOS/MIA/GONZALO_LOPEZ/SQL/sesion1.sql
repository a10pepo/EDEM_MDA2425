select * from film;

select actor_id, first_name , last_name 
from actor
where first_name LIKE 'N%'; 
-- si quieres que empieze por N = '%N%'

select actor_id, first_name , last_name 
from actor
where first_name LIKE '%n';
-- si quieres que termine en n = '%n'

select *
from actor
where first_name ilike '%N%';
--significa que contenga la letra n
--ilike: no distingue entre mayúsculas y minúsculas

select *
from actor
where first_name ilike 'N_%';
--si quieres que lleve un caracter y después cualquier cosa = N_%
--% = cualquier cosa
-- _ = caracter
select*
from actor
where last_name is null
--is null = es nulo (no contiene ningún valor) // is not null= no es nulo


SELECT count(first_name) from actor ; 
-- utilizar función = SELECT función(columna_en_cuestión) from tabla

SELECT count(first_name) as contar_actores
from actor ;
-- renombrar función = select count(columna) as nuevo_nombre_función

SELECT distinct(first_name) from actor ;
-- coja los nombre sin que se repitan

SELECT  count(distinct first_name) from actor ;
--contar los nombres distintos = select count ( distinct first_name from actor)

SELECT MAX (distinct first_name) from actor ;
-- max = coge el mas próximo al último ; min = coge el más próximo al primero


SELECT title from film where replacement_cost <2 ;

SELECT title from film where replacement_cost>2 and title ilike 'R%';

SELECT title
from film
where replacement_cost>2 
and title ilike 'R%' 
and rental_duration between 0 and 5
and release_year < 2006 
and length > 100
and rental_rate>2;


--operaciones
--cuantas películas tengo que vender para recuperar su coste
SELECT title,rental_rate,replacement_cost,floor(replacement_cost/rental_rate) as punto_equilibrio from film;
--ceil : redondear hacia arriba 
--floor : redondear hacia bajo
-- la peli que tenga el punto_equilibrio más alto es la menos rentable ( más difícil de recuperar)

SELECT title,rental_rate,replacement_cost, floor(replacement_cost/rental_rate) as punto_equilibrio
FROM FILM
order by punto_equilibrio DESC ;


select * from film
where special_features[1] ilike 'D%' ;
-- selecciona las special_features [prrimera palabra] empieze por D