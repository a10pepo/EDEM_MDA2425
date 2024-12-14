SELECT value, COUNT(value) FROM jokes
GROUP BY value
ORDER BY COUNT(value) DESC;
