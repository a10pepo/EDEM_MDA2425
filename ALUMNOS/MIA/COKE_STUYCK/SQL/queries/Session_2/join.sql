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