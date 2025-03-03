## Consultar los datos

```sql
select count (title) from film;

select count (*) from film;

select avg(rental_rate) from film;

select title, 
	rental_rate, 
	replacement_cost, 
	round(replacement_cost/rental_rate, 2) as percentage 
from public.film;

select title,
	ceil(replacement_cost/rental_rate) as rents_to_profit
from public.film;

select *
from film
where 2 < rental_rate and rental_rate > 3;

select title, rental_rate
from public.film
where rental_rate between 2 and 3;

select title, 
	rental_rate, 
	release_year
from public.film
where title like 'A%s'
	and rental_rate between 2 and 3
	and release_year = 2006
	and title is not null;

select first_name,
	last_name
from public.actor
where first_name like 'A%';

select title,
	rental_rate
from public.film
where rental_rate > 10;

select title,
	rental_rate
from public.film
where rental_rate between 5 and 10;

select title,
	rental_rate,
	f.length
from public.film as f
where rental_rate < 5
	and length < 100;
	
select title, 
	rental_rate
from public.film
where title like 'Gi%';

select title, 
	rating,
	f.length
from public.film as f
where title = 'Ali Forever';

select title,
	rental_rate
from public.film
where rental_rate is null;

select title,
	f.length
from public.film as f
order by length
limit 5;

select rating,
	count(distinct title) as películas,
	round(avg(rental_rate),2) as precio_medio,
	min(rental_rate) as precio_más_bajo,
	max(rental_rate) as precio_más_alto,
	round(avg(f.length),2) as duración,
	min(release_year) as más_antigua,
	max(release_year) as más_nueva
from public.film as f
group by rating
having avg(f.length) > 110;

select rating,
	count(distinct title) as películas,
	round(avg(rental_rate),2) as precio_medio,
	round(avg(f.length),2) as duración
from public.film as f
group by rating
having count(distinct title) > 200
	and avg(rental_rate) > 3
	and avg(f.length) > 115;
	
select customer.first_name,
	customer.last_name,
	address.address
from public.customer customer
	inner join public.address address 
	on customer.address_id = address.address_id
limit 10;

-- ficha de cliente: nombre, país, ciudad y dirección
select customer.first_name,
	customer.last_name,
	country.country,
	city.city,
	address.address
from public.customer customer
	left join public.address address 
		on customer.address_id = address.address_id
	left join public.city city
		on address.city_id = city.city_id
	left join public.country country
		on city.country_id = country.country_id
limit 10;

-- ¿cuántos actores tiene cada película?
select f.title,
	count(distinct a.actor_id) as actores
from public.actor a
	left join public.film_actor fa
		on a.actor_id = fa.actor_id
	left join public.film f
		on fa.film_id  = f.film_id
group by f.title
order by count(distinct a.actor_id) desc;

-- ¿cuáles son las películas que tienen más de dos actores?
select f.title,
	count(distinct a.actor_id) as actores
from public.actor a
	left join public.film_actor fa
		on a.actor_id = fa.actor_id
	left join public.film f
		on fa.film_id  = f.film_id
group by f.title
having count(distinct a.actor_id) > 2
order by count(distinct a.actor_id) desc;

-- ¿cuál es la película que tiene más actores?
select f.title,
	count(distinct a.actor_id) as actores
from public.actor a
	left join public.film_actor fa
		on a.actor_id = fa.actor_id
	left join public.film f
		on fa.film_id  = f.film_id
group by f.title
order by count(distinct a.actor_id) desc
limit 1;
```

## Editar los datos

```sql
-- crear tabla
create table if not exists public.reviews(
	film_id integer not null,
	customer_id integer not null,
	review_date date not null,
	review_description character varying(50) not null,
	constraint film_customer_pkey
		primary key (film_id, customer_id) -- una sola primary key compuesta por dos campos
	);
```

```sql
-- insertar datos en nuestra tabla reviews
insert into public.reviews (film_id, customer_id, review_date, review_description)
	values (1234,5678,'01-01-2024','ok');

-- sobreescribir un campo
update public.reviews
set review_description = 'good'
where film_id = 1234

-- borrar un registro
delete
from public.reviews
where film_id = 1234

-- borrar tabla entera
drop table public.reviews
```

```sql
-- cambiar las características de una tabla
alter table film
	alter column title varchar
	alter column description varchar

alter table public.reviews
	rename column review_description to review_opinion

-- añadir columnas
alter table public.reviews
	add column review_stars int2
```

## Vistas

```sql
create or replace view rental_duration_by_country as
select co.country as country,
	avg(r.return_date - r.rental_date) as rental_duration
from rental r
	left join customer cu
		on r.customer_id = cu.customer_id
	left join address a	
		on cu.address_id = a.address_id 
	left join city ci
		on a.city_id = ci.city_id
	left join country co
		on ci.country_id = co.country_id
group by co.country,
	ci.city
order by rental_duration desc
limit 10
```

```sql
create or replace view top_customer as
select c.first_name || ' ' || c.last_name as name,
	count(distinct r.rental_id) as películas_alquiladas,
	sum(p.amount) as amount,
	-- usamos los :: para castear a fecha (cambiar el tipo de datos)
	round(avg(r.return_date::date - r.rental_date::date),2) as rental_duration
from customer c
	left join rental r
		on c.customer_id = r.customer_id 
	left join payment p
		on p.rental_id = r.rental_id
where p.amount is not null
group by name
order by amount desc
limit 5
```

```sql
-- unión de vistas
select *, 'top_customer' as tipo
	from top_customer
union all
select *, 'low_customer' as tipo
	from low_customer

select avg(top_customer.amount), 'top_customer' as tipo
	from top_customer
union all
select avg(low_customer.amount), 'low_customer' as tipo
	from low_customer
```

## Subconsultas con `where`

```sql
-- estas dos consultas dan el mismo resultado

select sum(p.amount) from payment p
left join customer c on c.customer_id = p.customer_id 
where c.first_name ilike 'C%'

select sum(p.amount) from payment p
where customer_id in (
	select customer_id 
	from customer c 
	where first_name  
		ilike 'C%'
)
```

```sql
/* 
conteo de alquileres, suma de ingresos y ticket medio
para alquileres con una duración de más de 3 días
*/

select sum(p.amount) as amount,
	count(distinct p.rental_id) as alquileres,
	round(sum(p.amount)/count(distinct p.rental_id),2) as AOV
from payment p
where rental_id in (
	select r.rental_id
	from rental r
	where (r.return_date::date - r.rental_date::date) > 3
)
```

## Subconsultas con `with`

Declaras la query antes y luego la usas como si fuese una especie de vista

```sql
with
	subquery1 as
		(select)
	subquery2 as
		(select...)
select...
```

```sql
/*
clientes que han gastado más de 190: 
¿cuántos son y cuánto se han gastado en total?
*/

with over_190 as
	(select customer_id,
		sum(amount) as amount
	from payment
	group by customer_id
	having sum(amount) > 190
	)
select sum(amount),
	count(customer_id) as customers
from over_190
```

```sql
/* 
Identifica el empleado que más ingresos genera:
¿dónde vive?
¿cuántos clientes ha atendido?
¿cuál es la duración media?
*/

with top_employer as (
	select p.staff_id as staff_id,
		sum(p.amount) as amount,
		count(distinct customer_id) as total_customers
	from payment p
	group by p.staff_id
	order by sum(p.amount) desc
	limit 1
	),
sub_address as (
	select a.address as address,
		s.staff_id as staff_id,
		(s.first_name || ' ' || s.last_name) as full_name
	from staff s
		left join address a
		on a.address_id = s.address_id
	),
rental_duration as (
	select r.staff_id as staff_id,
		round(avg(r.return_date::date - r.rental_date::date),2) as avg_rental_duration
	from rental r
	group by r.staff_id
	)
select s.full_name,
	s.address,
	t.total_customers,
	r.avg_rental_duration
from top_employer t
left join sub_address s
	on t.staff_id = s.staff_id
left join rental_duration r
	on r.staff_id = s.staff_id
```