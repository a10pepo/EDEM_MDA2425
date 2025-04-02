# IMDB Analysis with Spark

This repository contains the code to perform an analysis of IMDB movies using Spark. The project involves analyzing the IMDB dataset and storing the results in a MySQL database.

## Project Execution

To start the Spark containers, go to the docker folder and run the following command:
sh
docker-compose up -d


### Execution from Terminal
There are two scripts available depending on whether you want to store the results in MySQL or simply display them on the terminal.

#### Display on Terminal
To execute the script that shows the results directly on the terminal, use the following command:
sh
bash /spark/bin/spark-submit --master local /opt/project/src/python/imdb_ratings.py


#### Store in MySQL
To execute the script that saves the results in MySQL, use the following command:
sh
docker exec -it spark-master /spark/bin/spark-submit --jars /opt/project/jar/mysql-connector-j-8.0.33.jar /opt/project/src/python/imdb_ratings_sql.py


### Execution with MySQL
If you prefer to store the results in the database for later consultation, make sure the MySQL container is running and accessible from the Spark container. The connection parameters are set as follows:
- Host: mysql
- Port: 3306
- Database: pysparkdb
- User: edem2425
- Password: edem2425

## Project Description

1. *Data Loading:*
   - The script loads the IMDB dataset using PySpark and performs preprocessing to clean and structure the data.

2. *Analysis Performed:*
   - Top 10 highest-rated movies
   - Top 10 movies with the highest gross income
   - Top 10 movies with the most votes
   - Most common genres
   - Top-rated genres
   - Average rating by decade
   - Average gross by decade
   - Directors with the most movies

3. *Results Storage:*
   - The results are stored in a MySQL database, with each analysis saved in a separate table.

## Thanks :)