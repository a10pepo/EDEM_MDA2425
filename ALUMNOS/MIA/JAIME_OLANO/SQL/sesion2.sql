 --NUMERO DE PELÍCULAS

select count (title) , rating from film group by rating;

--PRECIO MEDIO DE ALQUILER

select rating, avg (rental_rate) as precio_medio from film group by rating;

--PRECIO MÍNIMO DE ALQUILER

select rating, min (rental_rate) as precio_minimo from film group by rating;

--PRECIO MAXIMO DE ALQUILER

select rating, max (rental_rate) as precio_maximo from film group by rating;

--DURACION MEDIA DE LAS PELICULAS

select round (avg(length),2), rating from film group by rating;

--AÑO DE LA PELICULA MAS AMTIGUA

select min (release_year),rating from film group by rating;

--AÑO DE LA PELICULA MAS RECIENTE

select max (release_year),rating from film group by rating;


--USAMOS AHORA EL HAVING (AGRUPACIOR GRUPOS, SE NECESITA GROUP BY PREVIO)

select rating, count (film_id)from film group by rating having count(film_id) >200;

select rating, round (avg (rental_rate), 2 )from film group by rating having avg (rental_rate) >3;

select rating, round (avg(length),2) from film  group by rating having avg (length) >115;

--CLAUSULA JOIN (RELACIONAR TABLAS)

SELECT *
from film
left join language on film.language_id = language.language_id;


select title , name ,a.language_id, b.language_id
from film a
left join language b on a.language_id = b.language_id