from initial_info import airplanes, flights, passengers
from datetime import datetime

def airplanes_hangar():
    for a in airplanes:
        print(f"- {a['plateNumber']} ({a['type']}) | Owner: {a['ownerName']} | Hangar: {a['hangarId']}")

def landed_flights():
    now = datetime.now()
    for f in flights:
        arrival = datetime.strptime(f['arrivalTime'], "%Y-%m-%dT%H:%M:%S")
        if arrival < now:
            print(f"- {f['flightId']} | From {f['origin']} to {f['destination']} | Arrived: {arrival.strftime('%Y-%m-%d %H:%M')}")

def boarded_passengers():
    for f in flights:
        for pid, status in f['passengerIds']:
            if status == 'Boarded':
                print(f"- Passenger {pid} on flight {f['flightId']}")

def empty_seats():
    for f in flights:
        airplane = next((a for a in airplanes if a['plateNumber'] == f['plateNumber']), None)
        if airplane:
            empty = airplane['capacity'] - f['occupiedSeats']
            if empty / airplane['capacity'] > 0.10:
                print(f"- {f['flightId']} has {empty} empty seats ({round(100*empty/airplane['capacity'], 1)}%)")

def maintenance():
    today = datetime.today()
    for a in airplanes:
        next_date = datetime.strptime(a['nextMaintenanceDate'], "%Y-%m-%d")
        days_left = (next_date - today).days
        if days_left < 100:
            print(f"- {a['plateNumber']} | {days_left} days left")

def fuel_consumption():
    for f in flights:
        airplane = next((a for a in airplanes if a['plateNumber'] == f['plateNumber']), None)
        if airplane:
            ratio = f['fuelConsumption'] / airplane['fuel_capacity']
            if ratio > 0.10:
                print(f"- {f['flightId']} used {f['fuelConsumption']}L ({round(ratio*100, 1)}% of capacity)")

def main():
    print("\nWelcome to Jacinto's Aerodrome System")
    print("1. View airplanes in hangar")
    print("2. View landed flights")
    print("3. View boarded passengers")
    print("4. Alerts: Empty seats")
    print("5. Alerts: Maintenance soon")
    print("6. Alerts: High fuel consumption")
    
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        airplanes_hangar()
    elif choice == "2":
        landed_flights()
    elif choice == "3":
        boarded_passengers()
    elif choice == "4":
        empty_seats()
    elif choice == "5":
        maintenance()
    elif choice == "6":
        fuel_consumption()

if __name__ == "__main__":
    main()
