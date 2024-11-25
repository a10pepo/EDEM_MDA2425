--- sesion 2
CREATE TABLE IF NOT EXISTS public.reviews_ng (
    film_id int2 NOT NULL,
    customer_id int2 NOT NULL,
    review_date date NOT NULL,
    review_description text NOT NULL,
    CONSTRAINT reviews_ng_pkey PRIMARY KEY (film_id, customer_id)
)

/* Insert data into reviews_ng */

INSERT INTO
    public.reviews_ng (film_id, customer_id, review_description, review_date)
VALUES
    (4, 7, 'The movie is a bit boring', '10-11-2023')

/* Update */

UPDATE
	public.reviews_ng
SET
	review_date = '01-01-2024'
WHERE
	film_id = 4


SELECT *
FROM public.reviews_ng

/*
	Left Join:
	Every Movie (even if it's not linked to any language)
*/

SELECT
	* -- SELECT COUNT(*)
FROM
	film f
LEFT JOIN
	language l ON l.language_id = f.language_id


/*	
	Left Join:
	Every language being 'French' (even if it's not linked to any movie)
*/

SELECT
	l.name, f.title -- SELECT COUNT(*)
FROM
	language l
LEFT JOIN
	film f ON l.language_id = f.language_id
WHERE
	l.name = 'French'


/* 	
	Right Join equivalent:
	Every language being 'French' (even if it's not linked to any movie)
*/

SELECT
	l.name, f.title -- SELECT COUNT(*)
FROM
	film f
RIGHT JOIN
	language l ON l.language_id = f.language_id
WHERE
	l.name = 'French'
	
	
/*
	Join film, film_actor and actor tables
	to show every movie an actor appears in
*/

SELECT
    f.title, a.first_name, a.last_name -- SELECT COUNT(*)
FROM
    film f
LEFT JOIN
    film_actor fa ON f.film_id = fa.film_id
LEFT JOIN
    actor a ON a.actor_id = fa.actor_id


/*
	Join film, film_actor and actor tables
    to show number of movies an actor appears in descending order
	if number of movies > 40
    (name an last name together in one column)
*/

SELECT
    a.first_name || ' ' || a.last_name AS "Actor", COUNT(*) AS "Movies" -- SELECT COUNT(*)
FROM
    film_actor fa
LEFT JOIN
    film f ON f.film_id = fa.film_id
LEFT JOIN
    actor a ON a.actor_id = fa.actor_id
GROUP BY
    a.first_name, a.last_name
HAVING
	COUNT(*) > 40
ORDER BY
	COUNT(*) DESC


/*
	Join film, film_actor and actor tables
    to show number of actors appearing in a movie in descending order
	if number of actors > 10
    (name an last name together in one column)
*/

SELECT
    f.title AS "Film", COUNT(*) AS "Actors" -- SELECT COUNT(*)
FROM
    film f
LEFT JOIN
    film_actor fa ON f.film_id = fa.film_id
LEFT JOIN
    actor a ON a.actor_id = fa.actor_id
GROUP BY
    f.title
HAVING
    COUNT(*) > 10
ORDER BY
    COUNT(*) DESC

/* Count movies by rating */

SELECT
	COUNT(*) AS "Total"
FROM
	film f
WHERE
	f.rating IS NOT null
GROUP BY
	f.rating
	
	
/* Average rental rate by rating with only 1 decimal place */

SELECT
    ROUND(AVG(f.rental_rate), 1) AS "Avg. Rental Rate", f.rating AS "Rating" -- SELECT COUNT(*)
FROM
    film f
WHERE
    f.rental_rate IS NOT null
GROUP BY
    f.rating
	
/* Minimum rental rate by rating */

SELECT
	MIN(f.rental_rate) AS "Min. Rental Rate", f.rating AS "Rating" -- SELECT COUNT(*)
FROM
	film f
WHERE
	f.rental_rate IS NOT null
GROUP BY
	f.rating

/* Maximum rental rate by rating */

SELECT
	MAX(f.rental_rate) AS "Min. Rental Rate", f.rating AS "Rating" -- SELECT COUNT(*)
FROM
	film f
WHERE
	f.rental_rate IS NOT null
GROUP BY
	f.rating
	
/* Average movie duration by rating */

SELECT
	ROUND(AVG(f.length), 0) AS "Avg. Movie Duration", f.rating AS "Rating" -- SELECT COUNT(*)
FROM
	film f
WHERE
	f.rental_rate IS NOT null
GROUP BY
	f.rating
	
/* Year of oldest movie by rating */

SELECT
	MIN(f.release_year) AS "Oldest Movie", f.rating AS "Rating" -- SELECT COUNT(*)
FROM
	film f
WHERE
	f.rental_rate IS NOT null
GROUP BY
	f.rating
	
/* Year of oldest movie by rating */

SELECT
	MAX(f.release_year) AS "Oldest Movie", f.rating AS "Rating" -- SELECT COUNT(*)
FROM
	film f
WHERE
	f.rental_rate IS NOT null
GROUP BY
	f.rating


/* Grouped stats by rating */

SELECT
	f.rating AS "Rating",
	COUNT(*) AS "Total",
    ROUND(AVG(f.rental_rate), 1) AS "Avg. Rental Rate",
	MIN(f.rental_rate) AS "Min. Rental Rate",
	MAX(f.rental_rate) AS "Min. Rental Rate",
	ROUND(AVG(f.length), 0) AS "Avg. Movie Duration",
	MIN(f.release_year) AS "Oldest Movie",
	MAX(f.release_year) AS "Oldest Movie"
FROM
	film f
WHERE
	f.rental_rate IS NOT null
GROUP BY
	f.rating


/* Number of movies grouped by rating having at least 200 movies */

SELECT
	f.rating AS "Rating",
	COUNT(*) AS "Total"
FROM
	film f
WHERE
	f.rental_rate IS NOT null
GROUP BY
	f.rating
HAVING
	COUNT(*) > 200


/* Average rental rate grouped by rating having at least an average rental rate of 3 */

SELECT
	f.rating AS "Rating",
    ROUND(AVG(f.rental_rate), 1) AS "Avg. Rental Rate"
FROM
	film f
WHERE
	f.rental_rate IS NOT null
GROUP BY
	f.rating
HAVING
	AVG(f.rental_rate) > 3


/* Average movie duration grouped by rating having at least an average movie duration of 115 */

SELECT
	f.rating AS "Rating",
	ROUND(AVG(f.length), 0) AS "Avg. Movie Duration"
FROM
	film f
WHERE
	f.rental_rate IS NOT null
GROUP BY
	f.rating
HAVING
	ROUND(AVG(f.length), 0) > 115


/* Join */