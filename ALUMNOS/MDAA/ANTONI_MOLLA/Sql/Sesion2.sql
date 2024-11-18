select *
from film;


SELECT f.title, count(a.actor_id) as actor_account
FROM film f
left join film_actor fa on f.film_id=fa.film_id
left join actor a on fa.actor_id=a.actor_id
Group by f.title
order by actor_account desc;

--Dia 2

CREATE TABLE IF NOT EXISTS public.reviews (
film_id integer NOT NULL,
customer_id integer NOT NULL,
review_date timestamp not null default now(),
review_description varchar(50),
CONSTRAINT reviews_pkey PRIMARY KEY (film_id, customer_id)
	);

--Añadir columna 
alter table REVIEWS 
add Reviews_stars int2;

alter table reviews
rename column review_description
to review_opinion;

select *
from reviews;


--Cambiar tipo de dato

alter table reviews
alter column review_opinion type varchar(25);


--VIEWS	

select *
from actor_info ai 

create or replace view antoni_molla as
select f.title, a.first_name, a.last_name
from film f 
left join film_actor fa on f.film_id=fa.film_id
left join actor a  on fa.actor_id=a.actor_id;


select *
from antoni_molla am;


--Top 5
create or replace view Top5 as
select concat(c.first_name,'',c.last_name),sum(p.amount) as suma_amount, avg(r.return_date-r.rental_date) as rental_duration,
count(i.film_id) 
from customer c
left join payment p on c.customer_id=p.customer_id
left join rental r on p.rental_id=r.rental_id
LEFT JOIN inventory i on r.inventory_id=i.inventory_id
group by 1
order by sum(p.amount) desc
limit 5;


--Peores clientes

create view Down5 as 
select concat(c.first_name, ' ',c.last_name),sum(p.amount) as suma_amount, avg(r.return_date-r.rental_date) as rental_duration,
count(i.film_id) 
from customer c
left join payment p on c.customer_id=p.customer_id
left join rental r on p.rental_id=r.rental_id
LEFT JOIN inventory i on r.inventory_id=i.inventory_id
group by 1
order by sum(p.amount) asc
limit 5;

select *
from peoresclientes p 

select * from Down5
union all
select * from top5 t 

create view kpis as
select  avg(Down5.suma_amount), 'down5' as tipo from Down5
union all
select avg(top5.suma_amount), 'top5' as tipo from top5


-Fechas y cambios de datos
SELECT avg(return_date::date-rental::date) AS difference_in_days,
return_date::date, rental_date::date, rental_id::varchar
FROM rental r;


SELECT avg(return_Date::date-rental_date::date)AS difference_in_days
FROM rental r;


--Subconsultas

select sum(p.amount) from payment p 
where customer_id in (
select customer_id from customer c where first_name ilike 'C%')




select sum(p.amount), count(rental_id), sum(p.amount)/count(rental_id) as Tiket_Medio from payment p 
where customer_id in (
select customer_id from rental where return_date::date-rental_date::date>3)


--Clausula with


with my_sub_query as
(select customer_id, sum(amount) as total
from payment p 
group by 1)
select * from my_sub_query where total > 190;



with my_sub_query as
(select concat(first_name,'', last_name), 
from staff s
left join payment p on s.staff_id=p.staff_id
group by 1
limit 1)
select * from sub
order by payment.amount 
