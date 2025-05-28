Para almacenar tu estado de Terraform en GCP, necesitas crear un bucket en Cloud Storage. Para ello, puedes usar el siguiente comando:

```bash
gcloud storage buckets create gs://<NOMBRE_BUCKET> --location <REGION>
```

Una vez creado el bucket en Cloud Storage, puedes configurar tu backend de Terraform con el siguiente código dentro de tu main.tf:

```hcl
terraform {
  backend "gcs" {
    bucket  = "<NOMBRE_BUCKET>"
    prefix  = "terraform/state"
  }
}
```
