5.1.
SELECT PALABRA
FROM palabras_stream2
WHERE PALABRA LIKE 'ca%' AND PALABRA LIKE '%o' AND LEN(PALABRA) > 6
EMIT CHANGES;

5.2
SELECT UCASE(PALABRA) AS PALABRA_UPPERCASE
FROM palabras_stream2
EMIT CHANGES;

