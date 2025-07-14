# Excercise with GCP Resources

We will work on the migration of the data warehouse (Clickhouse) that we used in the module `Cloud Intro`


-----------------------------

# STEPS WITHOUT TERRAFORM

## Create a pub/sub topic

PubSub is a messaging service that allows you to send and receive messages between independent applications. It is similar to Kafka, but it is a managed service. 

To create a PubSub topic in la UI, follow these steps:

1. Go to pub/sub in the console.
2. Click on `Create Topic`.
3. Name the topic `order-events`.
4. Add another topic called `delivery-events`.
   
## Create the instance for the `orders-app`

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



-----------------------------

# STEPS WITH TERRAFORM

## Create a bucket to store the terraform state

## Move to the terraform directory

```sh
cd EDEM2425/gcp_datawarehouse/excercise_end2end/terraform
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
   cd EDEM2425/gcp_datawarehouse/excercise_end2end
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
   nohup bash -c 'HOST_IP=<your-cloud-sql-ip> PROJECT_ID=<your-project-id> python -m orders_app.orders_to_db.main' > output.log 2>&1 &
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



# Use the analytical-layer with BigQuery as your Data Warehouse

Once you have the `orders-app` and the `delivery-app` running, we will focus in the analytical-layer.

First, we will go to BigQuery to create 2 datasets (one for the orders and another for the delivery events). 

1. Go to the BigQuery section in the GCP console.
2. Click on `Create Dataset` by clicking on the three dots on the right side of the name of your project.
3. Name the dataset `orders`.
4. Select the region `europe-west1`
5. Click on `Create Dataset`.
6. Click on `Create Dataset` again.
7. Name the dataset `delivery`.
8. Select the region `europe-west1`.
9. Click on `Create Dataset`.

Create the required tables in the `orders` dataset by running the following query in the BigQuery console:

```sql
-- Customers Table
CREATE TABLE IF NOT EXISTS `orders.customers` (
    id INT64,
    customer_name STRING,
    email STRING
);

-- Products Table
CREATE TABLE IF NOT EXISTS `orders.products` (
    id INT64,
    product_name STRING,
    price FLOAT64
);

-- Orders Table
CREATE TABLE IF NOT EXISTS `orders.orders` (
    id INT64,
    customer_id INT64,
    created_at TIMESTAMP,
    total_price FLOAT64
);

-- Order Products Table
CREATE TABLE IF NOT EXISTS `orders.order_products` (
    order_id INT64,
    product_id INT64,
    quantity INT64,
    price FLOAT64
);
```

For the `delivery`dataset, we will use what is called a BigQuery subscription to sync the events from the `delivery-events` topic to the `delivery` dataset.

To do this, follow these steps:

1. Create a raw_table in which the events will be stored:
 
```sql
CREATE TABLE IF NOT EXISTS `delivery.raw_events_delivery` (
    subscription_name STRING,
    message_id STRING,
    publish_time TIMESTAMP,
    data JSON,
    attributes JSON
)
PARTITION BY DATE(publish_time)
CLUSTER BY subscription_name, message_id
OPTIONS (
    labels=[('source','bq_subs')]
);
```

Now, we will create the subscription to the `delivery-events` topic:

1. Go to the Pub/Sub section in the GCP console.
2. Click on the `delivery-events` topic.
3. Click on `Create Subscription`.
4. Name the subscription `delivery-events-bq-sub`.
5. Select in type `Write to BigQuery`.
6. Select the `delivery` dataset.
7. Select the `raw_events_delivery` table.
8. Select `don't use schema`.
9. Select `Write metadata`
10. A message will appear that a SA doesn't have permissions. Copy the name of the SA and run the following command:
   ```sh
   gcloud projects add-iam-policy-binding <YOUR_PROJECT_ID> \
   --member=serviceAccount:<SA_email> \
   --role=roles/bigquery.dataEditor
   ```

11. On the `dead-letter` section, select `Create a new topic`.
12. Name the topic `delivery-events-dead-letter`.
13. Create a new subscription for the dead-letter topic.
14. Name the subscription `delivery-events-dead-letter-sub`.
15. Click on `Create`.
16. You might see two sections in the `Not delivered messages` with an error. Click in the `Grant` button to give permissions to publish and consume messages in the topic for the dead-lettering.


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
   cd EDEM2425/gcp_datawarehouse/excercise_end2end
   ```

2. Deploy the docker-compose of the analytical-layer:
   ```sh
   cd analytical-layer
   docker-compose up -d
   ```

3. Go to the browser and access to `http://localhost:3000` to access Metabase.
