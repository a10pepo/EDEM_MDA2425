import logging
import time

from data import initial_info
from data_processors import airplanes, flights, passengers

def app_jacinto():
    print("Initiating AWS Jacinto's app")
    while True:
        option = input("Please, select which data you want to process: airplanes, flights or passengers: ").lower()
        if option == "airplanes":
            airplanes.main_airplanes()
            logging.info("Airplanes completed")
        elif option == "flights":    
            flights.main_flights()
            logging.info("Flights completed")
        elif option == "passengers":
            passengers.main_passengers()
            logging.info("Passengers completed")
        else:
            print("Invalid option, please select on of the options.")
        continue_actions = input("\nDo you want to do something else? (yes/no): ").strip().lower()
        if continue_actions == "no":
            print("Exiting program.")
            break
    

if __name__ == '__main__':
    app_jacinto()
