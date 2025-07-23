***INSTRUCCIONES DEL EJERCICIO***
Excercise with GCP Resources
We will work on the first components of the architecture we used in the end2end of the module Cloud Intro

In particular, we will focus on deploying the orders-app and the delivery-app in the Cloud, but we will use VM instances instead VMs in our local machine, and we will also use pub/sub topics instead of Kafka.

Create a pub/sub topic
PubSub is a messaging service that allows you to send and receive messages between independent applications. It is similar to Kafka, but it is a managed service.

To create a PubSub topic in la UI, follow these steps:

Go to pub/sub in the console.
Click on Create Topic.
Name the topic order-events.
Add another topic called delivery-events.
Create the instance for the orders-app
For the orders-app we will create the VM instance using gcloud.

The command is the following:

gcloud compute instances create orders-app \
  --zone=europe-west1-b \
  --scopes=https://www.googleapis.com/auth/cloud-platform \
  --subnet=projects/<your-project-id>/regions/europe-west1/subnetworks/default \
  --machine-type=e2-micro \
  --image-project=debian-cloud \
  --image=debian-11-bullseye-v20241210 \
  --boot-disk-size=10GB
This command will create a VM instance with the following characteristics:

Name: orders-app
Zone: europe-west1-b
Scopes: https://www.googleapis.com/auth/cloud-platform
Subnet: projects/<your-project-id>/regions/europe-west1/subnetworks/default
Machine type: e2-micro
Image: debian-11-bullseye-v20241210
Boot disk size: 10GB
This configuration is requried to run the orders-app in the same network as the Kafka cluster.

Once the VM instance is created, you can log in to the instance using the following command:

gcloud compute ssh orders-app --zone=europe-west1-b
After you have successfully logged in, follow this steps to install docker:

Update de package index:

sudo apt-get update
Install the necessary packages to allow apt to use a repository over HTTPS:

sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
Add Docker’s official GPG key:

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
Add Docker's stable repository:

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
Update the package index again:

sudo apt-get update
Install Docker:

sudo apt-get install docker-ce docker-ce-cli containerd.io
Add your user to the docker group:

sudo usermod -aG docker $USER
Log out and log back in so that your group membership is re-evaluated.

Verify that Docker is installed correctly by running the hello-world image:

docker run hello-world
Install docker-compose by downloading the binary:

sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
Apply executable permissions to the binary:
sudo chmod +x /usr/local/bin/docker-compose
Verify that docker-compose is installed correctly:
docker-compose --version
Now that we have docker and docker-compose installed, we can clone the repository inside the orders-app instance.

Clone the repository:

git clone https://github.com/mimove/EDEM2425.git
Change to the directory of the orders-app:

cd EDEM2425/gcp_setup/excercise_1/
Lastly, we need to install the venv and the dependencies of the orders-app:

Install the venv:

sudo apt-get install python3-venv
Create the venv:

python3 -m venv .venv
Activate the venv:

source .venv/bin/activate
Install the dependencies:

pip install -r requirements.txt
Once all theses steps are followed, not we can create a machine-image of the orders-app instance. This will allow us to create new instances without having to install all the dependencies again, simplyfing the deployment process of this and the remaining classes.

To create the machine-image of the orders-app instance, go to the Google Cloud UI, search for Compute Engine and then click on the instance orders-app. Once you are in the instance, click on the Create machine image button and give it a name.

Steps if you already have the machine-image
If you already have the machine-image of the orders-app instance, you can create a new instance using the following command:

gcloud compute instances create <instance-name> \
  --zone=europe-west1-b \
  --scopes=https://www.googleapis.com/auth/cloud-platform \
  --subnet=projects/<your-project-id>/regions/europe-west1/subnetworks/default \
  --machine-type=e2-micro \
  --source-machine-image=projects/<your-project-id>/global/machineImages/<MACHINE_IMAGE_NAME> \
  --boot-disk-size=10GB
For example, we also need an instance for the delivery-app so you need to execute the command, replacing the values with the correct ones.

Once both the orders-app and the delivery-app VMs are running, you can log in into the each instance and run the following commands:

### In both instances

Log in to the instance:

gcloud compute ssh <instance-name> --zone=europe-west1-b
Move to the correct directory:

cd EDEM2425/gcp_setup/excercise_1/
Activate the venv:

source .venv/bin/activate
For the orders-app instance
Move into the orders-app directory:

cd orders-app
Run the docker-compose to start the postgres data base and the admin:

docker-compose up -d
Move back to the excercise_1 directory:

cd ..
Run the orders-app using nohup so that it runs in the background (if you close the terminal, the app will still be running):

nohup bash -c 'HOST_IP=localhost PROJECT_ID=<your-project-id> python -m orders_app.orders_to_db.main' > output.log 2>&1 &
This will start creating orders, store them in the database and publish confirmation events to the order-events topic.

If you want to see the logs, run the following command:

tail -f output.log
For the delivery-app instance
Run the following command to start the delivery-app:
nohup bash -c 'PROJECT_ID=<your-project-id> python -m delivery_app.main' > output.log 2>&1 &
If you want to see the logs, run the following command:

tail -f output.log
This will start consuming the events from the order-events topic and publish delivery events to the delivery-events topic.

Extra excercise: Use the analytical-layer
Once you have the orders-app and the delivery-app running, you can also deploy the analytical-layer to process the delivery events and store them in ClickHouse in your local machine as we did in the Cloud INTRO end2end excercise.

To do this, we need a few steps

Go to the excercise directory in your local machine:

cd EDEM2425/gcp_setup/excercise_1
Create the venv, activate it and install the requirements:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Deploy the docker-compose of the analytical-layer:

cd analytical-layer
docker-compose up -d
Now that we have both the clickhouse and metabase running, we can deploy the EL pipeline to syncronize the PostgresDB and the Events from PubSub in two different ways.

Before we proceed with the running of the EL pipeline, we need allow traffic on port 5432 in Google Cloud, so that we can connect to the PostgresDB that is deployed in the orders-app instace from our local machine.

To do this, follow these steps:

Search for Firewall in the GCP console.
Click on Create Firewall Rule.
Name the rule edem-excercises.
On targets, select All instances in the network.
On Source IP ranges, write 0.0.0.0/0.
Scroll down to the Protocols and Ports section. Click on TCP
Allow the following port:
5432
Click on Create.
Running directly the script in our machine
To do so, we need to run the following commands:

Create your application-default credentials. This will allow us to identify to the GCP services with our user account:

gcloud auth application-default login
Run the script to syncronize the PostgresDB database inside the ./excercise_1 directory:

HOST_IP=localhost POSTGRES_IP=<orders-app-ip>  python -m analytical_layer.el_orders.main
If you are using Windows CMD, you can run:

set HOST_IP=localhost
set POSTGRES_IP=<orders-app-ip>
python -m analytical_layer.el_orders.main
If you are using Windows Powershell, you can run:

$env:HOST_IP = "localhost"; $env:POSTGRES_IP = "<orders-app-ip>"; python -m analytical_layer.el_orders.main
To syncronize the events of the delivery app, you can run the following command:

HOST_IP=localhost PROJECT_ID=<your-gcp-project-id> python -m analytical_layer.el_delivery.main
If you are using Windows CMD, you can run:

set HOST_IP="localhost"
set PROJECT_ID="<your-gcp-project-id>"
python -m analytical_layer.el_delivery.main
If you are using Windows Powershell, you can run:

$env:HOST_IP = "localhost"; $env:PROJECT_ID = "<your-gcp-project-id>"; python -m analytical_layer.el_delivery.main
User the Docker image with the cronjob
To identify ourselves inside the Docker Container, we need to create a Service Account in GCP to allow the analytical-layer to consume the delivery-events topic.

To do this, follow these steps:

Go to the IAM & Admin section in the GCP console.
Click on Service Accounts.
Click on Create Service Account.
Name the service account pub-sub-get-subscription.
Add the role Pub/Sub Subscriber.
Click on Create.
Click on the service account you just created.
Click on Add Key.
Select JSON and click on Create.
Copy the path of the JSON file you just downloaded.
Build the Docker image:

docker build -t analytical-layer-cron -f analytical_layer/docker/DockerFile .
Run the following command (remember to change the variables within <> by your own values):

docker run --network analytical_layer_default \
-e PROJECT_ID=<your-gcp-project-id> \
-e POSTGRES_IP=<orders-app-ip> \
-e HOST_IP=<clickhouse-docker-container-ip> \
-v <path-to-your-pub-sub-sa>:/app/pub-sub-credentials.json \
-e GOOGLE_APPLICATION_CREDENTIALS=/app/pub-sub-credentials.json \
analytical-layer-cron
