module "pubsub" {
    source                  = "./modules/pubsub"
    project_id              = var.project_id
    region                  = var.region
    topic_name_environment  = var.topic_name_environment
    topic_name_driving      = var.topic_name_driving 
    topic_name_battery      = var.topic_name_battery
    city_name               = var.city_name 
    num_vehicle             = var.num_vehicle
    sub_env_name            = var.sub_env_name
    sub_driv_name           = var.sub_driv_name
    sub_batt_name           = var.sub_batt_name
    artifact_repo_generator = var.artifact_repo_generator
    image_name              = var.image_name
    }