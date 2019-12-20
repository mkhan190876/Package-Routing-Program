# Mohammed Khan Student ID: 001107593
import datetime
import csv

with open("Distance_Table_Data.csv") as csv_data:  # Reads CSV files with distance data
    csv_read = csv.reader(csv_data, delimiter=',')
    csv_read = list(csv_read)
with open("Distance_Table_Name.csv") as csv_data_2:  # Reads CSV files with delivery location names
    csv_read_2 = csv.reader(csv_data_2, delimiter=',')
    csv_read_2 = list(csv_read_2)

    # Function stores row and column values then calculates total distance
    # Location distances returned and iterated through
    # Represents distance between two locations, O(1) space-time complexity
    def distance_check(row_val, col_val, total_val):
        distance = csv_read[row_val][col_val]
        if distance == "":
            distance = csv_read[col_val][row_val]
        total_val += float(distance)
        return total_val

    def current_distance(row_val, col_val):  # Returns current distance, O(1) space-time complexity
        distance = csv_read[row_val][col_val]
        if distance == "":
            distance = csv_read[col_val][row_val]
        return float(distance)

    truck_time_one = ["8:00:00"]  # Times trucks leaves hub
    truck_time_two = ["9:10:00"]
    truck_time_three = ["11:00:00"]

    # Functions below for three trucks, gets total distance for each truck
    # Divmod used to format time, O(N) space-time complexity
    def truck_one(total_distance):
        time = total_distance / 18
        distance_minutes = "{0:02.0f}:{1:02.0f}".format(*divmod(time * 60, 60))
        time_end = distance_minutes + ":00"
        truck_time_one.append(time_end)
        total = datetime.timedelta()
        for i in truck_time_one:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            total += d
        return total

    def truck_two(total_distance):
        time = total_distance / 18
        distance_minutes = "{0:02.0f}:{1:02.0f}".format(*divmod(time * 60, 60))
        time_end = distance_minutes + ":00"
        truck_time_two.append(time_end)
        total = datetime.timedelta()
        for i in truck_time_two:
            (h, m, s) = i.split(":")
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            total += d
        return total

    def truck_three(total_distance):
        time = total_distance / 18
        distance_minutes = "{0:02.0f}:{1:02.0f}".format(*divmod(time * 60, 60))
        time_end = distance_minutes + ":00"
        truck_time_three.append(time_end)
        total = datetime.timedelta()
        for i in truck_time_three:
            (h, m, s) = i.split(":")
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            total += d
        return total

    def address_check():  # Returns package information, O(1) space-time complexity
        return csv_read_2

    truck_one_state = []  # Variables created to list state of trucks
    truck_one_state_list = []
    truck_two_state = []
    truck_two_state_list = []
    truck_three_state = []
    truck_three_state_list = []

    truck_one_state_list.insert(0, "0")  # Truck state functions below, O(1) space-time complexity for all truck states

    def truck_one_index():
        return truck_one_state_list

    def truck_one_list():
        return truck_one_state

    truck_two_state_list.insert(0, "0")

    def truck_two_index():
        return truck_two_state_list

    def truck_two_list():
        return truck_two_state

    truck_three_state_list.insert(0, "0")

    def truck_three_index():
        return truck_three_state_list

    def truck_three_list():
        return truck_three_state

    # Function created to utilize Greedy sorting Algorithm for shortest path
    # Default value is set for distance, every distance checked against default value
    # Packages added to selected trucks after route determined, packages then added to list
    # Package is then removed from list with smallest value
    # O(N^2) space-time complexity
    def shortest_distance(truck_distance, truck, truck_location):
        if len(truck_distance) == 0:  # Initializes list
            return truck_distance
        else:
            try:
                value = 100.0
                location = 0
                for i in truck_distance:
                    if current_distance(truck_location, int(i[1])) <= value:
                        value = current_distance(truck_location, int(i[1]))
                        location = int(i[1])
                for i in truck_distance:
                    if current_distance(truck_location, int(i[1])) == value:
                        if truck == 1:
                            truck_one_state.append(i)
                            truck_one_state_list.append(i[1])
                            value_pop = truck_distance.index(i)
                            truck_distance.pop(value_pop)
                            truck_location = location
                            shortest_distance(truck_distance, 1, truck_location)
                        elif truck == 2:
                            truck_two_state.append(i)
                            truck_two_state_list.append(i[1])
                            value_pop = truck_distance.index(i)
                            truck_distance.pop(value_pop)
                            truck_location = location
                            shortest_distance(truck_distance, 2, truck_location)
                        elif truck == 3:
                            truck_three_state.append(i)
                            truck_three_state_list.append(i[1])
                            value_pop = truck_distance.index(i)
                            truck_distance.pop(value_pop)
                            truck_location = location
                            shortest_distance(truck_distance, 3, truck_location)
            except IndexError:
                pass
