SELECT
	"title" AS "Movie",
	"special_features" AS "Special Features",
	"rental_rate" AS "Rate",
	"release_year" AS "Year",
	CONCAT("length" / 60, ':', "length" % 60) AS "Duration",
	CEIL("replacement_cost" / "rental_rate") AS "Break Even"
	-- SELECT COUNT(*)
FROM
	film f
WHERE
	f.replacement_cost > 2
	AND f.title LIKE 'C%'
	AND f.rental_duration BETWEEN 0 AND 5
	AND f.release_year = 2006
	AND f.length > 100
	AND f.rental_rate > 2
	AND f.special_features[1] ILIKE 'D%'