from initial_info import airplanes, flights, passengers

def print_section(title: str, data: list):
    print(f"{title}:\n")
    for i, item in enumerate(data, 1):
        print(f"{title[:-1]} {i}:")
        for key, value in item.items():
            label = key.replace('_', ' ').replace('Id', 'ID').capitalize()
            print(f"  {label}: {value}")
        print()

if __name__ == "__main__":
    print_section("Aviones", airplanes)
    print_section("Vuelos", flights)
    print_section("Pasajeros", passengers)