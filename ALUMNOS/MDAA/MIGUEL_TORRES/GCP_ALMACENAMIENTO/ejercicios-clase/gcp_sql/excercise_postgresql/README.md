# GCP CLOUD SQL EXERCISE

## Introduction

In this first exercise, we will create a Cloud SQL instance in GCP. We will create a PostgreSQL instance, we will connect to it, and we will create a database using [Mockaroo](https://www.mockaroo.com/).

First, go to the website of Mockaroo and create a free account.


## Steps

First we need to go to Mockaroo and create the database. Mockaroo is a tool that allows you to create random data for your database. In this case, we will provide the DDL to create the database and Mockaroo will generate the data for us.

We will create a database with the following DDL (example of a public transportation system):

```sql
-- Create routes table
CREATE TABLE routes (
    route_id SERIAL PRIMARY KEY,
    route_name VARCHAR(50) NOT NULL,
    start_point VARCHAR(50) NOT NULL,
    end_point VARCHAR(50) NOT NULL
);

-- Create buses table
CREATE TABLE buses (
    bus_id SERIAL PRIMARY KEY,
    route_id INT NOT NULL,
    capacity INT NOT NULL CHECK (capacity > 0),
    status VARCHAR(100),
    FOREIGN KEY (route_id) REFERENCES routes(route_id) ON DELETE CASCADE
);

-- Create drivers table
CREATE TABLE drivers (
    driver_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    license_number VARCHAR(20) UNIQUE NOT NULL,
    assigned_route INT,
    FOREIGN KEY (assigned_route) REFERENCES routes(route_id) ON DELETE SET NULL
);

-- Create schedules table
CREATE TABLE schedules (
    schedule_id SERIAL PRIMARY KEY,
    bus_id INT NOT NULL,
    route_id INT NOT NULL,
    departure_time TIME NOT NULL,
    arrival_time TIME NOT NULL,
    FOREIGN KEY (bus_id) REFERENCES buses(bus_id) ON DELETE CASCADE,
    FOREIGN KEY (route_id) REFERENCES routes(route_id) ON DELETE CASCADE
);
```

If you want to create a different database, you can ask ChatGPT to generate the DDL for you.


After we have the DDL, we click on the Database tab, at the top of the page, and then in `Try Fabricate Now`


In the `Create a New Database` section, select a name for your database, select the type as PostgreSQL, and paste the DDL in the `Create Tables Script` section. Then click on `Create Database`. That will create our database, and it will create 100 rows for each table with random, but realistic data.



## Create a Cloud SQL instance

1. Go to the [Cloud SQL](https://console.cloud.google.com/sql) page in the GCP Console.

2. Click on `Create Instance`.

3. Select PostgreSQL as the database engine.

4. In Edition Preset, select `Sandbox`.

5. Select PostgreSQL 16 as the version.

6. Give the name `public-transport` to the Instance ID (or any other if you have chosen a different database in the previous step).

7. Give the password `EDEM2425`

8. Select `europe-sothwest1 (Madrid)` as the region.

9. Click on `Create Instance`.


## Connect to the Cloud SQL instance

Once the Instance is created, we have to connect to it. Follow this steps:

1. Go to the Cloud SQL studio.

2. Select Database: postgres

3. Select user: postgres

4. Select Password: EDEM2425


## Create tables and insert data

Once we are connected to the database, we have to create the tables and insert the data. We can do it using the SQL editor in the Cloud SQL studio.

1. Copy the DDL of the previous step and paste it in the SQL editor. Then click on `Run`.

2. Once the tables are created, we can insert the data. Download the Data from Mockaroo, open the `load.sql` file and paste its content in the SQL editor. You have to remove the `SET SESSION` lines from the load.sql script

3. Click on `Run`.

4. The command should fail, as the tables are introduced in alphabetical order, so the foreign keys will fail. This is because PostgreSQL is ACID compliant.

5. We can modify the definition of the tables to allow for the foreign keys to be created. We can do it by adding the `DEFERRABLE INITIALLY DEFERRED` clause to the foreign keys. We can do it by running the following script:

```sql
ALTER TABLE buses DROP CONSTRAINT buses_route_id_fkey;
ALTER TABLE buses ADD CONSTRAINT buses_route_id_fkey FOREIGN KEY (route_id) REFERENCES routes(route_id) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE drivers DROP CONSTRAINT drivers_assigned_route_fkey;
ALTER TABLE drivers ADD CONSTRAINT drivers_assigned_route_fkey FOREIGN KEY (assigned_route) REFERENCES routes(route_id) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE schedules DROP CONSTRAINT schedules_bus_id_fkey;
ALTER TABLE schedules ADD CONSTRAINT schedules_bus_id_fkey FOREIGN KEY (bus_id) REFERENCES buses(bus_id) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;
```

6. Try now to run the insert script again. It should work now.

7. Now you can try to run some queries to check that the data is correctly inserted.

