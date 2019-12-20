# Mohammed Khan Student ID: 001107593
import csv

# Hash table


class HashEntry:

    def __init__(self, key, item):
        self.key = key
        self.item = item


class HashTable:

    def __init__(self, capacity=10):  # O(1) space-time complexity
        self.map = []  # Generates empty list
        for i in range(capacity):
            self.map.append([])

    def _get_hash(self, key):  # Creates hash key, O(1) space-time complexity
        store = int(key) % len(self.map)
        return store

    def insert_package(self, key, value):  # Creates package insert function, O(N) space-time complexity
        key_hash = self._get_hash(key)
        values_hash = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([values_hash])
            return True
        else:
            for key_val in self.map[key_hash]:
                if key_val[0] == key:
                    key_val[1] = values_hash
                    return True
            self.map[key_hash].append(values_hash)
            return True

    def update(self, key, value):  # Creates package update function, O(N) space-time complexity
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for key_val in self.map[key_hash]:
                if key_val[0] == key:
                    key_val[1] = value
                    print(key_val[1])
                    return True
        else:
            print("Error updating key: " + key)

    def get(self, key):  # Creates function that gets value from hash table, O(N) space-time complexity
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for key_val in self.map[key_hash]:
                if key_val[0] == key:
                    return key_val[1]
        return None

    def delete_value(self, key):  # Creates function that deletes value from hash table, O(N) space-time complexity
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for val in range(0, len(self.map[key_hash])):
            if self.map[key_hash][val][0] == key:
                self.map[key_hash].pop(val)
                return True
        return False


with open("Distance_Packages_Data.csv") as csvfile:
    csv_read = csv.reader(csvfile, delimiter=",")

    hash_insert = HashTable()  # Creates hash map object
    truck_one = []  # Lists represent each truck for delivery
    truck_two = []
    truck_one_trip_two = []

    # Inserts CSV data to listed variables
    # O(N) space-time complexity
    for row in csv_read:
        package_ID = row[0]
        package_address = row[1]
        package_city = row[2]
        package_state = row[3]
        package_zip_code = row[4]
        package_delivery_deadline = row[5]
        package_size = row[6]
        package_note = row[7]
        start_location = ""
        delivery_location = ""
        package_status = "At Hub"
        value_iteration = [package_ID, delivery_location, package_address,
                           package_city, package_state, package_zip_code,
                           package_delivery_deadline, package_size, package_note,
                           start_location, package_status]

        key = package_ID
        value = value_iteration
        # Moves package data into list
        # Allows package status lookup and sorting
        if value[6] != "EOD":
            if "Must" in value[8] or "None" in value[8]:
                truck_one.append(value)
        if "Can only be" in value[8]:
            truck_two.append(value)
        if "Delayed" in value[8]:
            truck_two.append(value)
        # Moves incorrectly addressed package to correct address
        if "84104" in value[5] and "10:30" not in value[6]:
            truck_one_trip_two.append(value)
        if "Wrong address listed" in value[8]:
            value[2] = "410 S State St"
            value[5] = "84111"
            truck_one_trip_two.append(value)
        if value not in truck_one and value not in truck_two and value not in truck_one_trip_two:
            if len(truck_two) > len(truck_one_trip_two):
                truck_one_trip_two.append(value)
            else:
                truck_two.append(value)

        hash_insert.insert_package(key, value)  # Moves incorrectly addressed package to correct address

    def get_hash_map():  # Creates functions to retrieve list of values, O(1) space-time complexity
        return hash_insert

    # Functions below load packages into first truck, second truck, and first trucks second trip
    # O(1) space-time complexity for functions below
    def check_truck_one():
        return truck_one

    def check_truck_two():
        return truck_two

    def check_truck_one_trip_two():
        return truck_one_trip_two
