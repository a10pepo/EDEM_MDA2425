# dbt-postgres

This repo contains a docker file to run  PostgreSQL and PGAdmin using docker compose. It also contains some raw data from a fictional app and some indications to get started with dbt. 

## PostgreSQL - PGAdmin

Change to the right directory and run:

```docker compose up ```

## dbt steps

1. Create a new virtual environment in your project and activate it.
```
python3 -m venv .venv

source .venv/bin/activate
```

Windows:  

```
python -m venv .venv

.venv\Scripts\activate
```

2. Then install dbt-core and the postgres adapter. 

```python3 -m pip install dbt-core dbt-postgres```

3. Create profiles.yml file to connect dbt to postgres. 

```
mkdir ~/.dbt 

vi ~/.dbt/profiles.yml
```
(copy code)

Windows:

C:\Users\yourUser\
Create folder: .dbt and add profiles.yml.

4. dbt init to create a new dbt project.

 ```dbt init jaffle_shop```

 "The profile jaffle_shop already exists in /Users/...../profiles.yml. Continue and overwrite it? [y/N]:" --> n

5. Delete the folder: jaffle_shop/models/example

6. In dbt_project.yml, delete lines 35 and 36.

7. Check connection

```
cd jaffle shop

dbt run
```

8. Add csv files in seeds folder.

9. Run seed to upload files to postgres

 ```dbt seed```

10. Verify the data is available in pgAdmin and delete CSV files from seeds folder.

11. Start modeling.


## Commands

```
dbt seed
dbt run
dbt test
dbt test --select test_type:generic
dbt test --select test_type:singular
dbt test --select one_specific_model
dbt docs generate
dbt docs serve
```
