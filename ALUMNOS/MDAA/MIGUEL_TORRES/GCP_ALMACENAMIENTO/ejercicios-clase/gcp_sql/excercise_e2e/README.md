# Excercise with GCP Resources

We will work on the migration of our operational DB (PostgresSQL) that we used in the module `Cloud Intro` to Cloud SQL 


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

-----------------------------

# STEPS WITH TERRAFORM

## Create a bucket to store the terraform state

```sh
gcloud storage buckets create gs://edem-terraform-state \
  --location=europe-west1 \
  --uniform-bucket-level-access
```

## Move to the terraform directory

```sh
cd EDEM2425/gcp_sql/excercise_e2e/terraform
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


## Create the required tables inside the PostgresDB instance

First, create a new database in the UI of Cloud SQL. Go to database, click on `Create Database` and call it `ecommerce`.

To create the tables inside the PostgresDB instance, you need to connect to the PostgresDB instance using Cloud SQL Studio, and run the following SQL commands:

```sql
CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY, 
    product_name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY, 
    customer_id INT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS order_products (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);
```






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
   cd EDEM2425/gcp_sql/exercise_e2e
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



## **Extra excercise: Use the analytical-layer**

Once you have the `orders-app` and the `delivery-app` running, you can also deploy the `analytical-layer` to process the delivery events and store them in ClickHouse in your local machine as we did in the Cloud INTRO end2end excercise.

To do this, we need a few steps

1. Go to the excercise directory in your local machine:
   ```sh
   cd EDEM2425/gcp_setup/excercise_1
   ```

2. Create the venv, activate it and install the requirements:
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Deploy the docker-compose of the analytical-layer:
   ```sh
   cd analytical-layer
   docker-compose up -d
   ```

Now that we have both the clickhouse and metabase running, we can deploy the EL pipeline to syncronize the PostgresDB and the Events from PubSub in two different ways.


### Running directly the script in our machine

To do so, we need to run the following commands:

1. Create your application-default credentials. This will allow us to identify to the GCP services with our user account:
   ```sh
   gcloud auth application-default login
   ```

2. Run the script to syncronize the PostgresDB database inside the ./excercise_1 directory:
   ```sh
   HOST_IP=localhost POSTGRES_IP=<postgres-ip>  python -m analytical_layer.el_orders.main
   ```

   If you are using Windows CMD, you can run:

   ```sh
   set HOST_IP=localhost
   set POSTGRES_IP=<postgres-ip>
   python -m analytical_layer.el_orders.main
   ```


   If you are using Windows Powershell, you can run:

   ```sh
   $env:HOST_IP = "localhost"; $env:POSTGRES_IP = "<postgres-ip>"; python -m analytical_layer.el_orders.main
   ```

3. To syncronize the events of the delivery app, you can run the following command:

   ```sh
   HOST_IP=localhost PROJECT_ID=<your-gcp-project-id> python -m analytical_layer.el_delivery.main
   ```

   If you are using Windows CMD, you can run:
   ```sh
   set HOST_IP="localhost"
   set PROJECT_ID="<your-gcp-project-id>"
   python -m analytical_layer.el_delivery.main
   ```

   If you are using Windows Powershell, you can run:
   ```sh
   $env:HOST_IP = "localhost"; $env:PROJECT_ID = "<your-gcp-project-id>"; python -m analytical_layer.el_delivery.main
   ```

### User the Docker image with the cronjob


1. To identify ourselves inside the Docker Container, we need to create a Service Account in GCP to allow the `analytical-layer` to consume the `delivery-events` topic.

   To do this, follow these steps:
   1. Go to the `IAM & Admin` section in the GCP console.
   2. Click on `Service Accounts`.
   3. Click on `Create Service Account`.
   4. Name the service account `pub-sub-get-subscription`.
   5. Add the role `Pub/Sub Subscriber`.
   6. Click on `Create`.
   7. Click on the service account you just created.
   8. Click on `Add Key`.
   9. Select `JSON` and click on `Create`.
   10. Copy the path of the JSON file you just downloaded.

2. Build the Docker image:
   ```sh
   docker build -t analytical-layer-cron -f analytical_layer/docker/DockerFile .
   ```

3. Run the following command (remember to change the variables within <> by your own values):
   ```sh
   docker run --network analytical_layer_default \
   -e PROJECT_ID=<your-gcp-project-id> \
   -e POSTGRES_IP=<postgres-ip> \
   -e HOST_IP=<clickhouse-docker-container-ip> \
   -v <path-to-your-pub-sub-sa>:/app/pub-sub-credentials.json \
   -e GOOGLE_APPLICATION_CREDENTIALS=/app/pub-sub-credentials.json \
   analytical-layer-cron
