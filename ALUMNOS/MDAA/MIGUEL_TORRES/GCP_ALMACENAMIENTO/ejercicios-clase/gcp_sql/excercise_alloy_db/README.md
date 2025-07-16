# GCP ALLOY DB EXERCISE

## Introduction

In this exercise, we will create an Alloy DB instance, and compare its performance with a PostgreSQL instance.

## Steps

1. Go to the GCP Console, search Alloy DB and create a new Alloy DB instance. 

2. In the ID cluster put `alloy-db-<edem-user>`

3. In Password put `EDEM2425`

4. In the region, select `europe-southwest1 (Madrid)`

5. In the network, select `default`

6. In the machine type select `4 vCPUs, 32 GB RAM`

7. Allow the IP public access

8. In the security of the network, sellect `Allow all connection without encryption`

9. Click on `Create`

After the instance is created (it will take a few minutes to be ready), we can move to the python script part


## Python script

1. First you should create a venv and install the requirements

2. Then you have to modify the IP variable of the alloy.py script to put the IP of your Alloy DB instance

3. Run the script with `python alloy.py`

4. To test it against a PostgreSQL instance, you can run the script `python postgresql.py` modifying the IP variable to the IP of your PostgreSQL instance

5. Once both scripts are run, you can log in both Cloud SQL Studio and Alloy DB Studio to check the performance of both instances

6. Run this query in both Studios:

    ```sql
    SELECT
    c.currency_code,
    er.base_currency_code,
    er.rate,
    er.timestamp
    FROM
    exchange_rates er
    LEFT JOIN
    currencies c
    ON
    c.id = er.currency_id
    ```