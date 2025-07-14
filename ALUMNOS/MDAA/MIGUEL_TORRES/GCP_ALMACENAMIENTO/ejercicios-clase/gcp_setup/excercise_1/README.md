# Excercise with GCP Resources

We will work on the first components of the architecture we used in the end2end of the module `Cloud Intro`

In particular, we will focus on deploying the `orders-app` and the `delivery-app` in the Cloud, but we will use VM instances instead VMs in our local machine, and we will also use pub/sub topics instead of Kafka.

## Create a pub/sub topic

PubSub is a messaging service that allows you to send and receive messages between independent applications. It is similar to Kafka, but it is a managed service. 

To create a PubSub topic in la UI, follow these steps:

1. Go to pub/sub in the console.
2. Click on `Create Topic`.
3. Name the topic `order-events`.
4. Add another topic called `delivery-events`.
   

## Create the instance for the `orders-app`

For the `orders-app` we will create the VM instance using gcloud.

The command is the following:

```sh
gcloud compute instances create orders-app \
  --zone=europe-west1-b \
  --scopes=https://www.googleapis.com/auth/cloud-platform \
  --subnet=projects/<your-project-id>/regions/europe-west1/subnetworks/default \
  --machine-type=e2-micro \
  --image-project=debian-cloud \
  --image=debian-11-bullseye-v20241210 \
  --boot-disk-size=10GB
```

This command will create a VM instance with the following characteristics:

- Name: `orders-app`
- Zone: `europe-west1-b`
- Scopes: `https://www.googleapis.com/auth/cloud-platform`
- Subnet: `projects/<your-project-id>/regions/europe-west1/subnetworks/default`
- Machine type: `e2-micro`
- Image: `debian-11-bullseye-v20241210`
- Boot disk size: `10GB`
  
This configuration is requried to run the `orders-app` in the same network as the Kafka cluster.

Once the VM instance is created, you can log in to the instance using the following command:

```sh
gcloud compute ssh orders-app --zone=europe-west1-b
```

After you have successfully logged in, follow this steps to install docker:

1. Update de package index:
   ```sh
   sudo apt-get update
   ```

2. Install the necessary packages to allow apt to use a repository over HTTPS:
   ```sh
   sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
   ```

3. Add Docker’s official GPG key:
   ```sh
   curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ````

4. Add Docker's stable repository:
   ```sh
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

5. Update the package index again:
   ```sh
   sudo apt-get update
   ```

6. Install Docker:
   ```sh
   sudo apt-get install docker-ce docker-ce-cli containerd.io
   ```

7. Add your user to the docker group:
   ```sh
   sudo usermod -aG docker $USER
   ```

8. Log out and log back in so that your group membership is re-evaluated.

9. Verify that Docker is installed correctly by running the hello-world image:
   ```sh
   docker run hello-world
   ```

10. Install docker-compose by downloading the binary:
   ```sh
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   ```

11. Apply executable permissions to the binary:
   ```sh
   sudo chmod +x /usr/local/bin/docker-compose
   ```

12. Verify that docker-compose is installed correctly:
   ```sh
   docker-compose --version
   ```

Now that we have docker and docker-compose installed, we can clone the repository inside the `orders-app` instance.

1. Clone the repository:
   ```sh
   git clone https://github.com/mimove/EDEM2425.git
   ```

2. Change to the directory of the `orders-app`:
   ```sh
   cd EDEM2425/gcp_setup/excercise_1/
   ```

Lastly, we need to install the venv and the dependencies of the `orders-app`:

1. Install the venv:
   ```sh
   sudo apt-get install python3-venv
   ```

2. Create the venv:
   ```sh
   python3 -m venv .venv
   ```

3. Activate the venv:
   ```sh
   source .venv/bin/activate
   ```

4. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

Once all theses steps are followed, not we can create a `machine-image` of the `orders-app` instance. This will allow us to create new instances without having to install all the dependencies again, simplyfing the deployment process of this and the remaining classes.

To create the `machine-image` of the `orders-app` instance, go to the Google Cloud UI, search for `Compute Engine` and then click on the instance `orders-app`. Once you are in the instance, click on the `Create machine image` button and give it a name.


## Steps if you already have the `machine-image`

If you already have the `machine-image` of the `orders-app` instance, you can create a new instance using the following command:

```sh
gcloud compute instances create <instance-name> \
  --zone=europe-west1-b \
  --scopes=https://www.googleapis.com/auth/cloud-platform \
  --subnet=projects/<your-project-id>/regions/europe-west1/subnetworks/default \
  --machine-type=e2-micro \
  --source-machine-image=projects/<your-project-id>/global/machineImages/<MACHINE_IMAGE_NAME> \
  --boot-disk-size=10GB
```

For example, we also need an instance for the `delivery-app` so you need to execute the command, replacing the values with the correct ones.

Once both the orders-app and the delivery-app VMs are running, you can log in into the each instance and run the following commands:


### In both instances

1. Log in to the instance:
   ```sh
   gcloud compute ssh <instance-name> --zone=europe-west1-b
   ```

2. Move to the correct directory:
   ```sh
   cd EDEM2425/gcp_setup/excercise_1/
   ```

3. Activate the venv:
   ```sh
   source .venv/bin/activate
   ```

### For the `orders-app` instance

1. Move into the `orders-app` directory:
   ```sh
   cd orders-app
   ```

2. Run the docker-compose to start the postgres data base and the admin:
   ```sh
   docker-compose up -d
   ````

3. Move back to the `excercise_1` directory:
   ```sh
   cd ..
   ```

4. Run the `orders-app` using nohup so that it runs in the background (if you close the terminal, the app will still be running):
   ```sh
   nohup bash -c 'HOST_IP=localhost PROJECT_ID=<your-project-id> python -m orders_app.orders_to_db.main' > output.log 2>&1 &
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

Before we proceed with the running of the EL pipeline, we need allow traffic on port 5432 in Google Cloud, so that we can connect to the PostgresDB that is deployed in the orders-app instace from our local machine.

To do this, follow these steps:

1. Search for `Firewall` in the GCP console.
2. Click on `Create Firewall Rule`.
3. Name the rule `edem-excercises`.
4. On targets, select `All instances in the network`.
5. On Source IP ranges, write `0.0.0.0/0`.
6. Scroll down to the `Protocols and Ports` section. Click on TCP
7. Allow the following port:
   - `5432`
8. Click on `Create`.

### Running directly the script in our machine

To do so, we need to run the following commands:

1. Create your application-default credentials. This will allow us to identify to the GCP services with our user account:
   ```sh
   gcloud auth application-default login
   ```

2. Run the script to syncronize the PostgresDB database inside the ./excercise_1 directory:
   ```sh
   HOST_IP=localhost POSTGRES_IP=<orders-app-ip>  python -m analytical_layer.el_orders.main
   ```

   If you are using Windows CMD, you can run:

   ```sh
   set HOST_IP=localhost
   set POSTGRES_IP=<orders-app-ip>
   python -m analytical_layer.el_orders.main
   ```


   If you are using Windows Powershell, you can run:

   ```sh
   $env:HOST_IP = "localhost"; $env:POSTGRES_IP = "<orders-app-ip>"; python -m analytical_layer.el_orders.main
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
   -e POSTGRES_IP=<orders-app-ip> \
   -e HOST_IP=<clickhouse-docker-container-ip> \
   -v <path-to-your-pub-sub-sa>:/app/pub-sub-credentials.json \
   -e GOOGLE_APPLICATION_CREDENTIALS=/app/pub-sub-credentials.json \
   analytical-layer-cron
