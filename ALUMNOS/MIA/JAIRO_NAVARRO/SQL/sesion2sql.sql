--Having màs de 200 peliculas 
SELECT 
    rating,
    COUNT(*) AS numero_peliculas,
    AVG(rental_rate) AS precio_medio_alquiler,
    MIN(rental_rate) AS precio_minimo_alquiler,
	MAX(rental_rate) AS preciomaximo,
	AVG(length) as maxduracion,
	MIN(release_year) as peliculamàsantigua,
	MAX(release_year) as peliculamasnueva
FROM 
    film
GROUP BY 
    rating
HAVING 
    count(*) > 200;

--precio medio de alquiler y 3 que ranting tenga precio superor a 3

SELECT 
    rating,
    COUNT(*) AS numero_peliculas,
    AVG(rental_rate) AS precio_medio_alquiler,
    MIN(rental_rate) AS precio_minimo_alquiler,
	MAX(rental_rate) AS preciomaximo,
	AVG(length) as maxduracion,
	MIN(release_year) as peliculamàsantigua,
	MAX(release_year) as peliculamasnueva
FROM 
    film
GROUP BY 
    rating
HAVING 
    AVG (rental_rate) > 3
	
--duracion media mayor a 115

SELECT 
    rating,
    COUNT(*) AS numero_peliculas,
    AVG(rental_rate) AS precio_medio_alquiler,
    MIN(rental_rate) AS precio_minimo_alquiler,
	MAX(rental_rate) AS preciomaximo,
	AVG(length) as maxduracion,
	MIN(release_year) as peliculamàsantigua,
	MAX(release_year) as peliculamasnueva
FROM 
    film
GROUP BY 
    rating
HAVING 
    AVG (length) > 115


create table if not exist reviews_jn (
	film_id INT PRIMARY KEY, 
	customer_id INT,
	review_date VARCHAR(50),
	review_description VARCHAR (300))

insert into reviews_jn (film_id, customer_id, review_date, review_description)
values ('1031', '15458798', '14-12-2024', 'Muy buena compra')

select * from reviews_jn
update reviews_jn
set review_date = '14-12-2024'
where review_Date = 2022