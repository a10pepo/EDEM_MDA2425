resource "google_storage_bucket" "dataflow_bucket" {
    name = var.bucket_name_dataflow
    location = var.location
    force_destroy = true
    public_access_prevention = "enforced"
}
