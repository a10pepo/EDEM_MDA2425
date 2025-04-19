""" 
Script: Vehicle Data Generator

Description: Generate telemetry data for multiple vehicles within a given city.

EDEM. Master Big Data & Cloud 2024/2025
Professor: Javi Briones
"""

""" Import Libraries """

# A. Python Libraries
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import argparse
import logging
import random
import time

# B. Custom Classes
from pubsub import PubSubMessages

""" Input Params """

parser = argparse.ArgumentParser(description=('Vehicle Data Generator'))

parser.add_argument(
    '--project_id',
    required=True,
    help='GCP Project ID.')

parser.add_argument(
    '--telemetry_battery_topic',
    required=True,
    help='PubSub topic for battery telemetry.')

parser.add_argument(
    '--telemetry_driving_topic',
    required=True,
    help='PubSub topic for driving telemetry.')

parser.add_argument(
    '--telemetry_environment_topic',
    required=True,
    help='PubSub topic for environment telemetry.')

parser.add_argument(
    '--city_name',
    required=True,
    help='Name of the city where data will be generated.')

parser.add_argument(
    '--num_vehicles',
    required=False,
    default=5,
    help='Number of vehicles to generate data for.')

args, opts = parser.parse_known_args()

""" Code: Helpful Functions """

def generate_battery_data(
        vehicle_states: dict, timestamps: dict, charging_probability: float = 0.1):

    """
    Generates battery events for vehicles.

    Params:
        vehicle_states(dict): Dictionary with vehicle IDs as keys and their current battery levels.
        timestamps(dict): Dictionary with vehicle IDs as keys and their current timestamps.
        charging_probability(float): Probability that an event is of type 'charging'.

    Returns:
        data(list): List of battery events with vehicle ID, timestamp, battery level, and event type.
    """

    data = []

    for vehicle_id in random.sample(list(vehicle_states.keys()), len(vehicle_states)):

        battery_level = vehicle_states[vehicle_id]
        timestamp = timestamps[vehicle_id]

        event_type = "driving" if random.random() > charging_probability else "charging"

        if event_type == "driving":
            battery_change = -random.uniform(3.0, 10.0)

        else:
            battery_change = 100 - battery_level
   
        battery_level = min(100, max(10, battery_level + battery_change))
        vehicle_states[vehicle_id] = battery_level

        data.append({
            "vehicle_id": vehicle_id,
            "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "battery_level": round(battery_level),
            "event_type": event_type
        })

        timestamps[vehicle_id] += timedelta(seconds=random.randint(10, 60))
   
    return data

def generate_driving_style_data(
        vehicle_ids: list, timestamps: dict):

    """
    Generates driving style events for vehicles.

    Params:
        vehicle_ids(list): List of vehicle IDs.
        timestamps(dict): Dictionary with vehicle IDs as keys and their current timestamps.

    Returns:
        data(list): List of driving style events with vehicle ID, timestamp, speed, braking force, and steering angle.
    """

    data = []

    for vehicle_id in random.sample(vehicle_ids, len(vehicle_ids)):

        timestamp = timestamps[vehicle_id]

        data.append({
            "vehicle_id": vehicle_id,
            "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "speed": round(random.uniform(0, 120), 2),  # Speed in km/h
            "braking_force": round(random.uniform(-1, 0), 2),  # Braking force (-1 to 0)
            "steering_angle": round(random.uniform(-30, 30), 2)  # Steering angle (-30° to 30°)
        })

        timestamps[vehicle_id] += timedelta(seconds=random.randint(10, 60))

    return data

def get_city_coordinates(city_name: str):

    """
    Gets the coordinates (latitude and longitude) of a city using GeoPy.

    Params:
        city_name(str): Name of the city.

    Returns: 
        Dictionary with latitude and longitude.

    """

    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(city_name)

    if location:
        return {"latitude": location.latitude, "longitude": location.longitude}
    else:
        raise ValueError(f"No coordinates were found for the city.: {city_name}")

def generate_environment_data(
    vehicle_ids: list, timestamps: dict, city_coordinates: dict, radius: float = 0.005):

    """
    Generates environmental data for vehicles, including coordinates and weather.

    Params:
        vehicle_ids(list): List of vehicle IDs.
        timestamps(dict): Dictionary with vehicle IDs as keys and their current timestamps.
        city_center(tuple): Central coordinates (latitude, longitude) of the city.
        radius(float): Maximum deviation for latitude and longitude from the city center.

    Returns:
        data(list): List of environment events with vehicle ID, timestamp, coordinates, temperature, and humidity.
    """

    data = []

    for vehicle_id in random.sample(vehicle_ids, len(vehicle_ids)):

        lat = city_coordinates['latitude'] + random.uniform(-radius, radius)
        lon = city_coordinates['longitude'] + random.uniform(-radius, radius)

        timestamp = timestamps[vehicle_id]

        data.append({
            "vehicle_id": vehicle_id,
            "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "latitude": round(lat, 6),
            "longitude": round(lon, 6),
            "temperature": round(random.uniform(-10, 35), 2),
            "humidity": round(random.uniform(20, 80), 2) 
        })

        timestamps[vehicle_id] += timedelta(seconds=random.randint(10, 60))

    return data

""" Code: Entry Point """

def run_streaming(project_id: str, telemetry_battery_topic: str,
                  telemetry_driving_topic: str, telemetry_environment_topic: str,
                  city_coordinates: dict, num_vehicles: int):
    """
    Publishes telemetry data to Pub/Sub topics dynamically (event-by-event).

    Args:
        project_id (str): Google Cloud project ID.
        telemetry_battery_topic (str): Pub/Sub topic for battery telemetry.
        telemetry_driving_topic (str): Pub/Sub topic for driving telemetry.
        telemetry_environment_topic (str): Pub/Sub topic for environment telemetry.
        city_coordinates (dict): Coordinates of the city.
        num_vehicles (int): Number of vehicles to simulate.

    Returns:
        None
    """
    # Initialize PubSub
    pubsub_class = PubSubMessages(project_id=project_id)

    # Initialize vehicle states
    vehicle_ids = [f"V{str(i).zfill(3)}" for i in range(1, num_vehicles + 1)]
    vehicle_states = {vehicle_id: random.uniform(50, 100) for vehicle_id in vehicle_ids}
    timestamps = {vehicle_id: datetime.now() for vehicle_id in vehicle_ids}

    # Random category selection
    categories = ["battery", "driving", "environment"]

    try:
        while True:

            # Select a random category
            selected_category = random.choice(categories)

            # Generate a single event based on the selected category
            if selected_category == "battery":

                event = generate_battery_data(vehicle_states, timestamps)[0]
                topic_name = telemetry_battery_topic

            elif selected_category == "driving":

                event = generate_driving_style_data(vehicle_ids, timestamps)[0]
                topic_name = telemetry_driving_topic

            elif selected_category == "environment":

                event = generate_environment_data(vehicle_ids, timestamps, city_coordinates)[0]
                topic_name = telemetry_environment_topic

            # Publish the event
            pubsub_class.publishMessages(payload=event, topic_name=topic_name)
            logging.info("Message published to %s: %s", topic_name, event['vehicle_id'])

            # Control the streaming rate
            time.sleep(1)

    except KeyboardInterrupt:
        logging.info("Streaming stopped by user.")

    except Exception as err:
        logging.error("An unexpected error occurred: %s", err)


""" Run """

if __name__ == "__main__":

    # Set Logs
    logging.getLogger().setLevel(logging.INFO)

    # Run Generator
    logging.info('Initializing the data generator.')

    location_payload = get_city_coordinates(city_name=args.city_name)

    run_streaming(project_id = args.project_id,
        telemetry_battery_topic = args.telemetry_battery_topic,
        telemetry_driving_topic = args.telemetry_driving_topic,
        telemetry_environment_topic = args.telemetry_environment_topic,
        city_coordinates = location_payload,
        num_vehicles = args.num_vehicles)
    
    logging.info('Terminating the data generator.')