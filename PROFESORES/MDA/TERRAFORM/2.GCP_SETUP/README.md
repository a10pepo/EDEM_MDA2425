# Guía de Configuración de Terraform y GCP

Esta guía te ayudará a configurar tu primer proyecto de Terraform en Google Cloud Platform (GCP). Aprenderás a configurar Terraform, crear los recursos necesarios en GCP y desplegarlos.

## Prerrequisitos

Antes de comenzar, asegúrate de tener lo siguiente:

1. **Cuenta de Google Cloud**: Regístrate en [Google Cloud Platform](https://cloud.google.com/).
2. **Google Cloud SDK**: Instala el [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
    1. MAC: 
    ```bash
    brew install --cask google-cloud-sdk
    ```
    2. Windows: Descarga e instala el [Google Cloud SDK](https://cloud.google.com/sdk/docs/install#windows).

    Una vez instalado, ejecuta el siguiente comando para autenticarte:
    ```bash
    gcloud init
    ```

3. **Terraform**: Instala Terraform siguiendo las instrucciones de la [guía de instalación de Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli).
    1. MAC: 
    ```bash
    brew install terraform
    ```
    2. Windows: Descarga e instala Terraform desde el [sitio oficial](https://developer.hashicorp.com/terraform/install).


4. **Proyecto y facturación**: Asegúrate de tener un proyecto en GCP y la facturación habilitada.

## Paso 1: Configuración del Proyecto en GCP

1. **Crea un nuevo proyecto**:
   - Ve a la [Consola de Google Cloud](https://console.cloud.google.com/).
   - Haz clic en el menú desplegable de proyectos y selecciona "Nuevo Proyecto".
   - Asigna un nombre y una ID de proyecto, y haz clic en "Crear".

2. **Habilita la facturación**:
   - Si aún no lo has hecho, habilita la facturación para tu nuevo proyecto.

3. **Habilita la API de Compute Engine**:
   - Navega a "APIs y servicios" en la consola.
   - Busca "Compute Engine" y habilita la API.

## Paso 2: Autenticación de Google Cloud

Configura la autenticación de Terraform para interactuar con GCP:

1. Abre la terminal y ejecuta el siguiente comando para autenticarte:

   ```bash
   gcloud auth login
   ````

## Paso 3: Creemos nuestro primer archivo de configuración de Terraform

1. Crea un directorio para tu proyecto y navega a él:

   ```bash
   mkdir terraform-gcp
   cd terraform-gcp
   ```
2. Crea un archivo `main.tf` y pega el siguiente código:

   ```hcl
   provider "google" {
     project = "your-project-id"
     region  = "europe-southwest1"
     zone    = "europe-southwest1-a"
   }

   resource "google_compute_instance" "vm_instance" {
    name         = "terraform-instance"
    machine_type = "e2-micro"

    boot_disk {
        initialize_params {
        image = "debian-cloud/debian-11"
        }
    }

    network_interface {
        # A default network is created for all GCP projects
        network = "default"
        access_config {
        }
    }
    }
   ```
3. Reemplaza `your-project-id` con el ID de tu proyecto de GCP.
4. Ejecuta el siguiente comando para loguearte en GCP:

   ```bash
   gcloud auth application-default login
   ```
5. Ejecuta el siguiente comando para inicializar Terraform:

   ```bash
    terraform init
    ```
6. Ejecuta el siguiente comando para planificar los recursos a crear:
   
   ```bash
   terraform plan
   ```

    Deberías obtener el siguiente resultado:

    ```bash
        Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
        + create

        Terraform will perform the following actions:

        # google_compute_instance.vm_instance will be created
        + resource "google_compute_instance" "vm_instance" {
            + can_ip_forward       = false
            + cpu_platform         = (known after apply)
            + creation_timestamp   = (known after apply)
            + current_status       = (known after apply)
            + deletion_protection  = false
            + effective_labels     = {
                + "goog-terraform-provisioned" = "true"
                }
            + id                   = (known after apply)
            + instance_id          = (known after apply)
            + label_fingerprint    = (known after apply)
            + machine_type         = "e2-micro"
            + metadata_fingerprint = (known after apply)
            + min_cpu_platform     = (known after apply)
            + name                 = "terraform-instance"
            + project              = "edem-363212"
            + self_link            = (known after apply)
            + tags_fingerprint     = (known after apply)
            + terraform_labels     = {
                + "goog-terraform-provisioned" = "true"
                }
            + zone                 = "europe-southwest1-a"

            + boot_disk {
                + auto_delete                = true
                + device_name                = (known after apply)
                + disk_encryption_key_sha256 = (known after apply)
                + kms_key_self_link          = (known after apply)
                + mode                       = "READ_WRITE"
                + source                     = (known after apply)

                + initialize_params {
                    + image                  = "debian-cloud/debian-11"
                    + labels                 = (known after apply)
                    + provisioned_iops       = (known after apply)
                    + provisioned_throughput = (known after apply)
                    + resource_policies      = (known after apply)
                    + size                   = (known after apply)
                    + type                   = (known after apply)
                    }
                }

            + network_interface {
                + internal_ipv6_prefix_length = (known after apply)
                + ipv6_access_type            = (known after apply)
                + ipv6_address                = (known after apply)
                + name                        = (known after apply)
                + network                     = "default"
                + network_ip                  = (known after apply)
                + stack_type                  = (known after apply)
                + subnetwork                  = (known after apply)
                + subnetwork_project          = (known after apply)

                + access_config {
                    + nat_ip       = (known after apply)
                    + network_tier = (known after apply)
                    }
                }
            }

        Plan: 1 to add, 0 to change, 0 to destroy.
    ```
