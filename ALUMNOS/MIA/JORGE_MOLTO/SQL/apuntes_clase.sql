-- sesión 1

select
	*
from 
	film t1
where 
	t1.replacement_cost > 2
	and t1.title ilike 'J%'
	and rental_duration between 2 and 4
	and release_year = 2006
	and t1."length" > 100
	and rental_rate > 2
; 
SELECT 
	title,
	CEIL(replacement_cost/rental_rate) as Break
FROM 
	film
order by 
	Break desc

-- sesión 2

SELECT 
	t1.rating as Rating,
	count(*) as NumPeliculas,
	cast(avg(t1.rental_rate) as numeric(4,2)) as PrecioMedio,
	min(t1.rental_rate) as PrecioMin,
	max(t1.rental_rate) as PrecioMin,
	cast(avg(t1.length) as float) as PrecioMin,
	min(t1.release_year) as AñoMin,
	max(t1.release_year) as AñoMax -- select count(*) 
FROM 
	film t1
GROUP BY
	t1.rating
HAVING 
	count(*) > 200 
	and avg(t1.rental_rate) > 3
	and avg(t1.length) > 115

----

SELECT 
	t1.title,
	t2.name as Idioma -- select *
FROM 
	film t1
	left OUTER JOIN -- select * from 
	language t2
	on t1.language_id = t2.language_id;
	
SELECT 
	t1.title,
	count(first_name) as NumActor-- select *
FROM 
	film t1
	inner join -- select * from
	film_actor t2
	on t1.film_id = t2.film_id
	inner join -- select * from
	actor t3
	on t2.actor_id = t3.actor_id
GROUP BY 
	t1.title
HAVING 
	count(first_name) > 30;
	
SELECT 
	concat(t3.first_name,' ', t3.last_name) as Actor,
	count(t1.title) as Peliculas
	-- select *
FROM 
	film t1
	inner join -- select * from
	film_actor t2
	on t1.film_id = t2.film_id
	inner join -- select * from
	actor t3
	on t2.actor_id = t3.actor_id
GROUP BY 
	concat(t3.first_name,' ', t3.last_name) 
ORDER BY
	Peliculas desc;
	
CREATE TABLE IF NOT EXISTS review_jorge (
	film_id serial4,
	customer_id int,
	review_date timestamp,
	review_descripcion varchar(250) not null
	--CONSTRAINT review_key PRIMARY KEY (film_id, custimer_id)
)

INSERT INTO review_jorge(film_id, customer_id,review_date,review_descripcion)
VALUES (4, 7, CURRENT_DATE, 'Vaya peli mas chula');

SELECT * FROM review_jorge

# En la clase 3 sea han tratado las CTE y las subconsultas 
# **CTE (Common Table Expressions) en SQL**
Una **CTE** es una consulta temporal que puedes definir al principio de una instrucción SQL para simplificar y reutilizar código. Se escribe usando `WITH` y se usa como si fuera una tabla.

**Ejemplo**:  
```sql
WITH EmpleadosAltos AS (
    SELECT Nombre, Altura
    FROM Empleados
    WHERE Altura > 180
)
SELECT * 
FROM EmpleadosAltos;
```
Aquí, `EmpleadosAltos` es la CTE que filtra empleados con altura mayor a 180.

---

### **Subconsultas en SQL**
Una **subconsulta** es una consulta dentro de otra consulta, que se ejecuta primero y su resultado se usa en la consulta externa. 

**Ejemplo**:  
```sql
SELECT Nombre
FROM Empleados
WHERE Salario > (SELECT AVG(Salario) FROM Empleados);
```
Esta subconsulta calcula el salario promedio y luego selecciona empleados que ganan más que ese promedio.