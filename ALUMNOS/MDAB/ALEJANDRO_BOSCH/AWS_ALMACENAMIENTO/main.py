from initial_info import flights as original_flights 
from initial_info import passengers as original_passengers
from initial_info import airplanes as original_airplanes 


def flights_info(): 
    return original_flights

def passengers_info(): 
    return original_passengers

def airplanes_info():
    return original_airplanes

def airplane_hangar():
    for airplane in original_airplanes:
        print(f"Plate Number: {airplane['plateNumber']}")
        print(f"HangarId: {airplane['HangarId']}")



if __name__ == "__main__":
    print(flights_info())
    print(passengers_info())
    print(airplanes_info())
    print(airplane_hangar())