# Mohammed Khan Student ID: 001107593
import datetime
from DistanceAlgorithm import shortest_distance
from DistanceAlgorithm import truck_one_index
from DistanceAlgorithm import distance_check
from DistanceAlgorithm import truck_one_list
from DistanceAlgorithm import current_distance
from DistanceAlgorithm import address_check
from DistanceAlgorithm import truck_one
from DistanceAlgorithm import truck_two_index
from DistanceAlgorithm import truck_two_list
from DistanceAlgorithm import truck_two
from DistanceAlgorithm import truck_three_index
from DistanceAlgorithm import truck_three_list
from DistanceAlgorithm import truck_three
from CSVHash import get_hash_map
from CSVHash import check_truck_one
from CSVHash import check_truck_two
from CSVHash import check_truck_one_trip_two

time = "8:00:00"  # Times each truck leaves hub
time_two = "11:00:00"
time_three = "9:10:00"

delivery_one = []
delivery_two = []
delivery_three = []
truck_distance_one = []
truck_distance_two = []
truck_distance_three = []

# Times formatted below for each variable
(h, m, s) = time.split(':')
time_one_convert = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = time_three.split(':')
time_two_convert = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = time_two.split(':')
time_three_convert = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# Loops and updates delivery status for first truck
# O(N) space-time complexity
i = 0  # Counter
for value in check_truck_one():
    check_truck_one()[i][9] = time
    delivery_one.append(check_truck_one()[i])
    i += 1

# Addresses looped through and compared to list of addresses
# Address added to index, O(N^2) space-time complexity
try:
    first_count = 0
    for n in delivery_one:
        for j in address_check():
            if n[2] == j[2]:
                truck_distance_one.append(j[0])
                delivery_one[first_count][1] = j[0]
        first_count += 1
except IndexError:
    pass
shortest_distance(delivery_one, 1, 0)  # Greedy sorting algorithm
truck_one_calculate = 0

# Truck 1 values looped through, total distance, and package distance for truck 1 calculated
# O(N) space-time complexity
truck_one_id = 0
for index in range(len(truck_one_index())):
    try:
        truck_one_calculate = distance_check(int(truck_one_index()[index]),
                                             int(truck_one_index()[index + 1]), truck_one_calculate)
        package_delivery = truck_one(current_distance(int(truck_one_index()[index]),
                                                      int(truck_one_index()[index + 1])))
        truck_one_list()[truck_one_id][10] = (str(package_delivery))
        get_hash_map().update(int(truck_one_list()[truck_one_id][0]), delivery_one)
        truck_one_id += 1
    except IndexError:
        pass
# Steps for truck one are identical for truck two, identical space-time complexity, identical algorithm utilized
i = 0
for value in check_truck_two():
    check_truck_two()[i][9] = time_three
    delivery_two.append(check_truck_two()[i])
    i += 1
try:
    second_count = 0
    for n in delivery_two:
        for j in address_check():
            if n[2] == j[2]:
                truck_distance_two.append(j[0])
                delivery_two[second_count][1] = j[0]
        second_count += 1
except IndexError:
    pass

shortest_distance(delivery_two, 2, 0)
truck_two_calculate = 0
truck_two_id = 0
for index in range(len(truck_two_index())):
    try:
        truck_two_calculate = distance_check(int(truck_two_index()[index]),
                                             int(truck_two_index()[index + 1]), truck_two_calculate)
        package_delivery = truck_two(current_distance(int(truck_two_index()[index]),
                                                      int(truck_two_index()[index + 1])))
        truck_two_list()[truck_two_id][10] = (str(package_delivery))
        get_hash_map().update(int(truck_two_list()[truck_two_id][0]), delivery_two)
        truck_two_id += 1
    except IndexError:
        pass

# Steps for truck one, two are identical for truck one trip two, identical space-time complexity and algorithm utilized
# Loop updates status of truck one trip two packages to "In Transit"
i = 0
for value in check_truck_one_trip_two():
    check_truck_one_trip_two()[i][9] = time_two
    delivery_three.append(check_truck_one_trip_two()[i])
    i += 1
try:
    third_count = 0
    for n in delivery_three:
        for j in address_check():
            if n[2] == j[2]:
                truck_distance_three.append(j[0])
                delivery_three[third_count][1] = j[0]
        third_count += 1
except IndexError:
    pass

shortest_distance(delivery_three, 3, 0)
truck_three_calculate = 0
truck_three_id = 0
for index in range(len(truck_three_index())):
    try:
        truck_three_calculate = distance_check(int(truck_three_index()[index]),
                                               int(truck_three_index()[index + 1]), truck_three_calculate)
        package_delivery = truck_three(current_distance(int(truck_three_index()[index]),
                                                        int(truck_three_index()[index + 1])))
        truck_three_list()[truck_three_id][10] = (str(package_delivery))
        get_hash_map().update(int(truck_three_list()[truck_three_id][0]), delivery_three)
        truck_three_id += 1
    except IndexError:
        pass


def truck_distances():  # Created Function to add and return total distance of each truck
    truck_distances = truck_one_calculate + truck_two_calculate + truck_three_calculate
    return truck_distances
