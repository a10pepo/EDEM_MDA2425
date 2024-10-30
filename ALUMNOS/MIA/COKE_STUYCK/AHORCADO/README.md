# Start services

`docker-compose up`

# Run the app passing 'palabras.txt' as a parameter

`docker-compose run app palabras.txt`

# Enter the database

`docker-compose exec db psql -U hangman hangman`

# Querie example

"""
  SELECT 
      palabra,
      COUNT(*) as attempts
  FROM attempts 
  GROUP BY palabra
  ORDER BY attempts DESC;
"""