--Cuantos actores tiene cada pelicula

SELECT title, COUNT(fa.actor_id)
from film as f
Left Join film_actor as fa on f.film_id = fa.film_id
group by title;

--Cuales son las peliculas que tienen más de 2 actores

SELECT title, COUNT(fa.actor_id) as actor_count
from film as f
Left Join film_actor as fa on f.film_id = fa.film_id
group by title
HAVING COUNT(fa.actor_id) > 2
Order by actor_count asc

--Alter table

	ALTER TABLE reviews_im 
	ADD COLUMN review_stars INT2
	
--Renombrar

Alter table reviews_im
Rename review_description to review_opinion

--Vista 
create view numero_actores as 
SELECT title, COUNT(fa.actor_id) as actor_count
from film as f
Left Join film_actor as fa on f.film_id = fa.film_id
group by title
HAVING COUNT(fa.actor_id) > 2
Order by actor_count asc

--Utilizamos la vista

select* from numero_actores;

--Crearemos una vista para sacar los mejores clientes automáticamente

create view mejores_clientes as
SELECT cu.customer_id, first_name,last_name, sum(pa.amount)
from customer as cu
Left Join payment as pa on cu.customer_id = pa.customer_id
group by cu.customer_id, first_name, last_name
Order by sum desc limit 3;

--Ejecuto
Select * from mejores_clientes

--Subconsulta
SELECT title
FROM film
WHERE language_id = (
    SELECT language_id
    FROM language
    WHERE name = 'English'
);

SELECT first_name, last_name, address_id
FROM customer
WHERE address_id IN (
    SELECT address_id
    FROM address
    WHERE address LIKE '1%'
);