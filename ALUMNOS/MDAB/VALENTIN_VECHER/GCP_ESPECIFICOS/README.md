# 🚗 Simulador de Sensores Tesla en GCP con Terraform

## 📌 Descripción
Este proyecto utiliza Terraform para desplegar en Google Cloud Platform (GCP) los recursos necesarios para simular los sensores de un coche Tesla. Los sensores monitorean el nivel de batería del vehículo y envían alertas a los usuarios cuando la batería está a punto de agotarse.

## 🏗️ Infraestructura en GCP
Terraform se encarga de provisionar los siguientes recursos en GCP:
- **Instancias de Compute Engine**: Representan los sensores del coche Tesla.
- **Pub/Sub**: Para la transmisión de eventos de bajo nivel de batería.
- **Cloud Functions**: Procesan los eventos de Pub/Sub y notifican a los usuarios.
- **Cloud Storage**: Para almacenar logs y configuraciones de los sensores.
- **BigQuery (Opcional)**: Para análisis posterior de los eventos generados.

## 🚀 Despliegue
### 1️⃣ Configurar el entorno
1. Instalar [Terraform](https://developer.hashicorp.com/terraform/downloads).
2. Configurar autenticación con GCP:
   ```bash
   gcloud auth application-default login
   ```
3. Clonar este repositorio y entrar en el directorio:
   ```bash
   git clone <repositorio>
   cd <directorio>
   ```

### 2️⃣ Inicializar y aplicar Terraform
1. Inicializar Terraform:
   ```bash
   terraform init
   ```
2. Aplicar la configuración para desplegar los recursos:
   ```bash
   terraform apply
   ```

## 📡 Funcionamiento
1. Las instancias de Compute Engine simulan los sensores del coche Tesla.
2. Cuando el nivel de batería baja de un umbral crítico, se envía un mensaje a Pub/Sub.
3. Una Cloud Function procesa el mensaje y notifica a los usuarios.
4. Los datos se pueden almacenar en BigQuery para análisis posterior.

## 📄 Archivos principales
- `main.tf` → Configuración principal de Terraform.
- `variables.tf` → Variables reutilizables.
- `outputs.tf` → Resultados clave tras la ejecución.
- `pubsub.tf` → Configuración de Pub/Sub.
- `compute.tf` → Definición de instancias de Compute Engine.
- `cloud_function.tf` → Configuración de la Cloud Function.
- `README.md` → Este documento.

## 📌 Referencias
- [Terraform en GCP](https://cloud.google.com/docs/terraform/getting-started-with-terraform)
- [Pub/Sub en GCP](https://cloud.google.com/pubsub/docs/overview)
- [Cloud Functions en GCP](https://cloud.google.com/functions/docs)
- [BigQuery en GCP](https://cloud.google.com/bigquery/docs/)

## 🔥 Notas
- Antes de desplegar, asegúrate de configurar correctamente tu cuenta de facturación en GCP.
- Los recursos generados pueden generar costos, por lo que se recomienda eliminarlos cuando no se usen:
  ```bash
  terraform destroy
  ```

