module "pub_sub" {
    source = "./modules/pubsub"
    project_id  = var.project_id
    topic_name_environment = var.topic_name_environment
    topic_name_driving = var.topic_name_driving 
    topic_name_battery = var.topic_name_battery
    city_name = var.city_name 
    num_vehicle = var.num_vehicle
    }