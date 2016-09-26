class Vehicle(object):
    def __init__(self, brand, model, kilometers_done, general_service_date):
        self.brand = brand
        self.model = model
        self.kilometers_done = kilometers_done
        self.general_service_date = general_service_date


def main():
    vehicle_data_file = open("vehicle_data.txt", "r")

    vehicle_list = []

    for item in vehicle_data_file:
        brand, model, kilometers_done, general_service_date = item.split(";")

        vehicle = Vehicle(brand=brand, model=model, kilometers_done=kilometers_done, general_service_date=general_service_date)

        vehicle_list.append(vehicle)

    action = raw_input("Would you like to see a list of the vehicles, update the kilometers and general service date or ad a new vehicle? (list/update/new) ")

    if action == "list":
        list_of_vehicles(vehicle_list)
    elif action == "update":
        update_vehicles(vehicle_list)
    elif action == "new":
        add_new_vehicle(vehicle_list)
    else:
        print "Sorry, your input was incorrect. Please try again."

    save_changes(vehicle_list, vehicle_data_file)
    vehicle_data_file.close()


def list_of_vehicles(vehicles):
    for index, item in enumerate(vehicles):
        print str(index) + ") BRAND: " + item.brand
        print "Model: " + item.model
        print "Kilometers: " + item.kilometers_done
        print "General Service Date: " + item.general_service_date


def update_vehicles(vehicles):
    list_of_vehicles(vehicles)

    vehicle_index = int(raw_input("Enter the index number of the vehicle you'd like to edit: "))

    vehicle = vehicles[vehicle_index]

    print "You selected: "
    print "BRAND: " + vehicle.name
    print "MODEL: " + vehicle.model
    print "Kilometers: " + vehicle.kilometers_done
    print "General Service Date: " + vehicle.general_service_date

    # this is example only for changing task name. Status and due date have the same logic.
    new_kilometers = raw_input("Enter new kilometers (press enter to skip): ")
    vehicle.kilometers_done = new_kilometers
    print "Vehicle kilometers successfully changed"


def add_new_vehicle(vehicles):
    brand = raw_input("Enter the brand of the vehicle: ")
    model = raw_input("Enter the model: ")
    kilometers_done = raw_input("Enter the kilometers done so far: ")
    general_service_date = raw_input("Enter the general service date (in this format: 05-MAR-2017): ")

    new_vehicle = Vehicle(brand="\n"+brand, model=model, kilometers_done=kilometers_done, general_service_date=general_service_date)  # \n means new line. This will be helpful when saving tasks back to TXT file.

    vehicles.append(new_vehicle)

    print "New vehicle was successfully added!"


def save_changes(vehicles, vehicle_data_file):
    vehicle_data_file.close()
    vehicle_data_file = open("vehicle_data.txt", "w")

    for item in vehicles:
        vehicle_data_file.write(item.brand + ";" + item.model + ";" + item.kilometers_done + ";" + item.general_service_date)


if __name__ == "__main__":
    main()
    print "END"# vehicle_manager_program
