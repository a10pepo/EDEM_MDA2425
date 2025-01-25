/* 
    Create table reviews with columns:
    - film_id
    - customer_id
    - review_date
    - review_description
*/

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