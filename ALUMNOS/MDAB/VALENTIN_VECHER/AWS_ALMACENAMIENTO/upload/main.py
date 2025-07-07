from initial_info import airplanes as planes
from initial_info import flights as flights
from initial_info import passengers as passengers 
from datetime import datetime 


def planes_hangar(): 
    plane_hangar= []
    for plane in planes:
        plane_hangar.append(plane)
    return plane_hangar 
    
        
def landed_planes():
    landed_planes = []
    for flight in flights:
        flight['arrivalTime'] = datetime.strptime(flight['arrivalTime'], "%Y-%m-%dT%H:%M:%S")
        if flight['arrivalTime'] < datetime.now():
            landed_planes.append(flight)
    return landed_planes
            
def choose_plane_passenger():
    passengers_on_hangar = []
    for flight in landed_planes():
        for passenger in flight['passengerIds']:
            if passenger[1] == 'Boarded':
                passengers_on_hangar.append(passenger)
    return passengers_on_hangar
        

        
            
def main():

    print("Welcome to the System, please choose an option: ")
    print("1. View Airplanes in the Hangar")
    print("2. View Landed Planes")
    print("3. See Passenger Arrival Status")
    print("4. Register plane on an hangar")
    choice = input("Please enter your choice: ")
    if choice == "1":
        planes_in_hangar = planes_hangar()
        print(planes_in_hangar)
    elif choice == "2":
        landed_planes_list = landed_planes()
        print(landed_planes_list)
    elif choice == "3":
        passengers_on_hangar = choose_plane_passenger()
        print(passengers_on_hangar)
        
        

if __name__ == "__main__":
   
    main()
    