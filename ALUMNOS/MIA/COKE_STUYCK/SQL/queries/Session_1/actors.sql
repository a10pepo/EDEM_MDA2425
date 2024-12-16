/* Select actors with first name containing n */

SELECT
	* -- SELECT COUNT(*)
FROM
	actor a
WHERE
	a.first_name ILIKE '%n%';


/* Select actors with first name starting with N,
followed by a character and followed by anything else */

SELECT
	* -- SELECT COUNT(*)
FROM
	actor a
WHERE
	a.first_name LIKE 'N_%'


/* Select actors with first name containing the letter n */

SELECT
	* -- SELECT COUNT(*)
FROM
	actor a
WHERE
	a.first_name ILIKE '%N%'


/* Count actors without lastname */

SELECT
	COUNT(*)
FROM
	actor a
WHERE
	a.last_name IS null
