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