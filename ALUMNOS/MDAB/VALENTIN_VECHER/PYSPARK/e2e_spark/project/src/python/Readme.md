# PySpark Data Processing and Integration with MySQL

This script processes movie data from three platforms: IMDb, Amazon, and Netflix. Its purpose is to perform data cleaning, transformations, and integration into a MySQL database for further analysis. By reading raw CSV files, the script extracts insights and saves both the raw and transformed data into MySQL tables for future queries and visualizations.

---

## Objective

1. **Data Integration**:
   - Load movie data from IMDb, Amazon, and Netflix CSV files into PySpark DataFrames.
     - IMDb: https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows
     - Amazon Prime Video: https://www.kaggle.com/datasets/shivamb/amazon-prime-movies-and-tv-shows
     - Netflix: https://www.kaggle.com/datasets/shivamb/netflix-shows
  
   - Save the raw data into MySQL tables (`imdb_notes`, `amazon_notes`, and `netflix_notes`) for centralized storage.

2. **Data Analysis**:
   - Perform transformations and aggregations to extract meaningful insights from the data.
   - Identify patterns such as the highest-rated movies, the number of movies per genre, and the longest movies on each platform.

3. **Cross-Platform Comparison**:
   - Analyze overlaps between platforms (e.g., movies available on Amazon, Netflix, and IMDb).
   - Calculate statistics like average IMDb ratings for movies available on multiple platforms.

4. **Save Results**:
   - Store the transformed datasets in MySQL for easier access and further analysis.

---

## Outcomes

1. **Centralized Data Storage**:
   - Raw data from all three platforms is stored in MySQL tables, allowing for unified access and querying.

2. **Insights Derived**:
   - List of the top-rated movies on IMDb.
   - Count and average IMDb ratings by genre.
   - Longest-duration movies on Amazon and Netflix, highlighting potential data inconsistencies.
   - Movies available across multiple platforms.
   - Average IMDb rating for cross-platform movies.

3. **Cross-Platform Analysis**:
   - Identification of movies shared between Amazon, Netflix, and IMDb.
   - Quantitative insights into overlaps and unique offerings of each platform.

---

All the project use mySQL and the docker is modified and completed.

![PySpark Process](https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif)

