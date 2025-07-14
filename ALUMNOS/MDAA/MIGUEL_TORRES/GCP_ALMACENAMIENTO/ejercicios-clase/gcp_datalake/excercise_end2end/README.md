# Excercise with GCP Resources

We will work on creating a small example of a Data Lake in GCS 


-----------------------------

# STEPS WITHOUT TERRAFORM


```sh
gcloud compute instances create orders-app \
  --zone=europe-west1-b \
  --scopes=https://www.googleapis.com/auth/cloud-platform \
  --subnet=projects/<your-project-id>/regions/europe-west1/subnetworks/default \
  --machine-type=e2-micro \
  --source-machine-image=projects/<your-project-id>/global/machineImages/<MACHINE_IMAGE_NAME> \
  --boot-disk-size=10GB
```


## Create the instance for the `delivery-app`

```sh
gcloud compute instances create delivery-app \
  --zone=europe-west1-b \
  --scopes=https://www.googleapis.com/auth/cloud-platform \
  --subnet=projects/<your-project-id>/regions/europe-west1/subnetworks/default \
  --machine-type=e2-micro \
  --source-machine-image=projects/<your-project-id>/global/machineImages/<MACHINE_IMAGE_NAME> \
  --boot-disk-size=10GB
```

## Create the Cloud SQL instance

To create a Cloud SQL instance, follow these steps:

Run the following command to create the instance:

```sh
gcloud sql instances create edem-postgres \
  --database-version=POSTGRES_15 \
  --tier=db-f1-micro \
  --region=europe-west1 \
  --availability-type=zonal \
  --storage-size=100 \
  --no-deletion-protection \
  --authorized-networks=0.0.0.0/0 \
  --root-password=EDEM2425
```

Run the following command to create a user for the database:

```sh
gcloud sql users create postgres \
  --instance=edem-postgres \
  --password=EDEM2425
```

Run the following command to create the ecommerce database:


```sh
gcloud sql databases create ecommerce \
  --instance=edem-postgres
```


Run the following command to create the BQ Datasets
```sh
gcloud bigquery datasets create orders_bronze --location=europe-west1 
gcloud bigquery datasets create delivery_bronze --location=europe-west1 
```

Run the following commands to create the BQ Tables
```sh
gcloud bigquery tables create orders_bronze.customers \
  --schema="id:INT64,customer_name:STRING,email:STRING"

gcloud bigquery tables create orders_bronze.products \
  --schema="id:INT64,product_name:STRING,price:FLOAT64"

gcloud bigquery tables create orders_bronze.orders \
  --schema="id:INT64,customer_id:INT64,created_at:TIMESTAMP,total_price:FLOAT64"

gcloud bigquery tables create orders_bronze.order_products \
  --schema="order_id:INT64,product_id:INT64,quantity:INT64,price:FLOAT64"

gcloud bigquery tables create delivery_bronze.raw_events_delivery \
  --schema="subscription_name:STRING,message_id:STRING,publish_time:TIMESTAMP,data:JSON,attributes:JSON" \
  --time_partitioning_field=publish_time \
  --clustering_fields=subscription_name,message_id \
  --labels=source=bq_subs
```

Run the following commands to create the pub/sub topics and subscriptions
```sh
# Create Pub/Sub Topics
gcloud pubsub topics create delivery-events
gcloud pubsub topics create order-events
gcloud pubsub topics create delivery-events-dead-letter

# Create the order-events subscription
gcloud pubsub subscriptions create order-events-sub \
  --topic=order-events

# Create Pub/Sub Subscriptions with BigQuery Sink
gcloud pubsub subscriptions create delivery-events-bq-sub \
  --topic=delivery-events \
  --bigquery-table=delivery_bronze.raw_events_delivery \
  --bigquery-use-table-schema=false \
  --bigquery-write-metadata \
  --dead-letter-topic=topics/delivery-events-dead-letter \
  --max-delivery-attempts=5


# Create Dead Letter Subscription
gcloud pubsub subscriptions create delivery-events-dead-letter-sub \
  --topic=delivery-events-dead-letter
```


-----------------------------

# STEPS WITH TERRAFORM

## Create a bucket to store the terraform state


## Move to the terraform directory

```sh
cd EDEM2425/gcp_datalake/excercise_end2end/terraform
```

## Modify the variables for the SA in the variables.tf file

Modify the `service_account_email` variable in the `variables.tf` file with the email of the service account of your project.

## Initialize the terraform directory

```sh
terraform init
terraform plan
```

## Create the infrastructure

```sh
terraform apply
```

Once we finished the excercise, we can destroy the infrastructure by running:

```sh
terraform destroy
```
-----------------------------


### In both instances

1. Log in to the instance:
   ```sh
   gcloud compute ssh <instance-name> --zone=europe-west1-b
   ```

2. Run a git pull inside the repository:
   ```sh
   cd EDEM2425
   git pull
   ```

3. Move to the correct directory:
   ```sh
   cd EDEM2425/gcp_datalake/excercise_end2end
   ```

4. Create a virtual environment:
   ```sh
   python3 -m venv .venv
   ```

5. Activate the venv:
   ```sh
   source .venv/bin/activate
   ```

6. Install the requirements:
   ```sh
   pip install -r requirements.txt
   ```

### For the `orders-app` instance


1. Run the `orders-app` using nohup so that it runs in the background (if you close the terminal, the app will still be running):
   ```sh
   nohup bash -c 'HOST_IP=<your-cloud-sql-ip> GCS_BUCKET_NAME=<your-bucket-name> PROJECT_ID=<your-project-id> python -m orders_app.orders_to_db.main' > output.log 2>&1 &
   ```

This will start creating orders, store them in the database and publish confirmation events to the `order-events` topic.

If you want to see the logs, run the following command:
```sh
tail -f output.log
```


### For the `delivery-app` instance

1. Run the following command to start the `delivery-app`:
   ```sh
   nohup bash -c 'PROJECT_ID=<your-project-id> python -m delivery_app.main' > output.log 2>&1 &
   ```

If you want to see the logs, run the following command:
```sh
tail -f output.log
```

This will start consuming the events from the `order-events` topic and publish delivery events to the `delivery-events` topic.



# Create a External Table in BigQuery to your Data Lake

Now that we have the parquet file created in our bucket, we will create a external table in BigQuery to access its content.

The steps you have to follow are:

1. Go to the dataset `orders_bronze`
2. Click on create table
3. Select `Google Cloud Storage` in `Create table from`
4. Select on Browse and choose your file from correct bucket
5. In the table field write `raw_additional_products_info`
6. In table type select `External Table`
7. Select the option `Auto detect` in the Schema Section
8. Click on `Create Table`

# Use the analytical-layer with BigQuery as your Data Warehouse

Now we can deploy the EL pipeline to syncronize the PostgresDB database with BigQuery.



To do so, we need to run the following commands:

1. Create your application-default credentials. This will allow us to identify to the GCP services with our user account (in case you haven't done it yet):
   ```sh
   gcloud auth application-default login
   ```

2. Create the venv, activate it and install the requirements:
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the script to syncronize the PostgresDB database
   ```sh
   POSTGRES_IP=<postgres-ip> GCP_PROJECT=<your-gcp-project-id> python -m analytical_layer.el_orders.main
   ```

   If you are using Windows CMD, you can run:

   ```sh
   set POSTGRES_IP=<postgres-ip>
   set GCP_PROJECT=<your-gcp-project-id>
   python -m analytical_layer.el_orders.main
   ```


   If you are using Windows Powershell, you can run:

   ```sh
   $env:POSTGRES_IP = "<postgres-ip>";
   $env:GCP_PROJECT = "<your-gcp-project-id>";
   python -m analytical_layer.el_orders.main
   ```


Now that we have the EL for orders_app. Let's use DBT to create a view for the delivery events.

1. Create a directory with the name of the project in the dbt directory:
   ```sh
   mkdir dbt_project_example
   ```

2. Move to the dbt directory:
   ```sh
   cd dbt_project_example
   ```

3. Install dbt-bigquery:
   ```sh
   pip install dbt-bigquery
   ```

3. Initialize the dbt project:
   ```sh
   dbt init edem_project
   ```

This will create the structure of the dbt project.

Now, you have a template prepare with the modifications needed to create the views for the delivery events.

1. Go to the folder `dbt_template` in the `excercise_end2end` directory.
2. Copy the dbt_project.yml content to the `dbt_project_example/edem_project/dbt_project.yml` file.
3. Copy the content of the `models` folder to the `dbt_project_example/edem_project/models` folder.
4. Copy the content of the `macros` folder to the `dbt_project_example/edem_project/macros` folder.
5. Run the command to create the views:
   ```sh
   cd dbt_project_example
   dbt run --select expanded_delivery_events
   ```

This will create the view for the delivery events in the `delivery` dataset in BigQuery.

We have also some tables for getting aggregations by running the analytics folder.

Run the following command to create the tables:
   ```sh
   dbt run --select analytics
   ```


Let's now deploy Metabase to visualize the data from BigQuery.

1. Go to the excercise directory in your local machine:
   ```sh
   cd EDEM2425/gcp_datalake/excercise_end2end
   ```

2. Deploy the docker-compose of the analytical-layer:
   ```sh
   cd analytical-layer
   docker-compose up -d
   ```

3. Go to the browser and access to `http://localhost:3000` to access Metabase.
