# Mohammed Khan Student ID: 001107593
import datetime
from TruckPackages import truck_distances
from CSVHash import get_hash_map


class Main:  # User Interface to check package status
    print("WGUPS Package Status System.")
    print("Truck delivery route completed in", "{0:.2f}".format(truck_distances(), 2), "miles.")
    initialize = input("Enter 'search' to display an individual package or "  # User input to display package status
                       "\nEnter 'time' to display all package status at chosen time: ")
    while initialize != "exit":  # O(N) space-time complexity
        # Choosing 'Time' displays status for all packages at chosen time
        # O(N) runtime process
        if initialize == "time":
            try:
                status_time = input("Enter time in HH:MM:SS format: ")
                (h, m, s) = status_time.split(":")
                time_conversion = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # O(N^2) space-time complexity
                for i in range(1, 41):
                    try:
                        time_one = get_hash_map().get(str(i))[9]
                        time_two = get_hash_map().get(str(i))[10]
                        (h, m, s) = time_one.split(":")
                        time_conversion_one = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = time_two.split(":")
                        time_conversion_two = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    except ValueError:
                        pass
                    # Times checked to see if trucks still at hub
                    if time_conversion_one >= time_conversion:
                        get_hash_map().get(str(i))[10] = "At Hub"
                        get_hash_map().get(str(i))[9] = "Leaves " + time_one
                        print("Package ID:", get_hash_map().get(str(i))[0], "   Delivery address:",
                              get_hash_map().get(str(i))[2], get_hash_map().get(str(i))[3],
                              get_hash_map().get(str(i))[4], get_hash_map().get(str(i))[5],
                              "  Delivery deadline:", get_hash_map().get(str(i))[6],
                              " Package weight:", get_hash_map().get(str(i))[7], "  Truck status:",
                              get_hash_map().get(str(i))[9], "  Delivery status:",
                              get_hash_map().get(str(i))[10])
                    elif time_conversion_one <= time_conversion:
                        # Checks for packages that have left hub, but have not been delivered
                        if time_conversion < time_conversion_two:
                            get_hash_map().get(str(i))[10] = 'In transit'
                            get_hash_map().get(str(i))[9] = 'Left ' + time_one
                            print("Package ID:", get_hash_map().get(str(i))[0], "   Delivery address:",
                                  get_hash_map().get(str(i))[2], get_hash_map().get(str(i))[3],
                                  get_hash_map().get(str(i))[4], get_hash_map().get(str(i))[5],
                                  "  Delivery deadline:", get_hash_map().get(str(i))[6],
                                  " Package weight:", get_hash_map().get(str(i))[7], "  Truck status:",
                                  get_hash_map().get(str(i))[9], "  Delivery Status:",
                                  get_hash_map().get(str(i))[10])
                        # Checks if packages delivered, displays time and status of packages
                        else:
                            get_hash_map().get(str(i))[10] = "Delivered " + time_two
                            get_hash_map().get(str(i))[9] = "Left " + time_one
                            print("Package ID:", get_hash_map().get(str(i))[0], "   Delivery Address",
                                  get_hash_map().get(str(i))[2], get_hash_map().get(str(i))[3],
                                  get_hash_map().get(str(i))[4], get_hash_map().get(str(i))[5],
                                  "  Delivery deadline:", get_hash_map().get(str(i))[6],
                                  " Package weight:", get_hash_map().get(str(i))[7], "  Truck status:",
                                  get_hash_map().get(str(i))[9], "  Delivery Status:",
                                  get_hash_map().get(str(i))[10])
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print("Invalid entry.")
                exit()
        # If 'search' is selected, user prompted for id and time
        # Displays package and time for the package user specified
        elif initialize == "search":
            try:
                i = input("Enter package ID: ")
                time_one = get_hash_map().get(str(i))[9]
                time_two = get_hash_map().get(str(i))[10]
                status_time = input("Enter time in HH:MM:SS format: ")
                (h, m, s) = status_time.split(":")
                time_conversion = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = time_one.split(":")
                time_conversion_one = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = time_two.split(":")
                time_conversion_two = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # Checks if package left hub or package has left but not been delivered
                # Displays information if package has been delivered
                if time_conversion_one >= time_conversion:
                    get_hash_map().get(str(i))[10] = "At Hub"
                    get_hash_map().get(str(i))[9] = "Leaves " + time_one
                    print("Package ID:", get_hash_map().get(str(i))[0], "   Delivery Address",
                          get_hash_map().get(str(i))[2], get_hash_map().get(str(i))[3],
                          get_hash_map().get(str(i))[4], get_hash_map().get(str(i))[5],
                          "  Delivery deadline:", get_hash_map().get(str(i))[6],
                          " Package weight:", get_hash_map().get(str(i))[7], "  Truck status:",
                          get_hash_map().get(str(i))[9], "  Delivery Status:",
                          get_hash_map().get(str(i))[10])
                elif time_conversion_one <= time_conversion:
                    if time_conversion < time_conversion_two:
                        get_hash_map().get(str(i))[10] = "In transit"
                        get_hash_map().get(str(i))[9] = "Left " + time_one
                        print("Package ID:", get_hash_map().get(str(i))[0], "   Delivery Address",
                              get_hash_map().get(str(i))[2], get_hash_map().get(str(i))[3],
                              get_hash_map().get(str(i))[4], get_hash_map().get(str(i))[5],
                              "  Delivery deadline:", get_hash_map().get(str(i))[6],
                              " Package weight:", get_hash_map().get(str(i))[7], "  Truck status:",
                              get_hash_map().get(str(i))[9], "  Delivery Status:",
                              get_hash_map().get(str(i))[10])
                    else:
                        get_hash_map().get(str(i))[10] = "Delivered " + time_two
                        get_hash_map().get(str(i))[9] = "Left at " + time_one
                        print("Package ID:", get_hash_map().get(str(i))[0], "   Delivery Address",
                              get_hash_map().get(str(i))[2], get_hash_map().get(str(i))[3],
                              get_hash_map().get(str(i))[4], get_hash_map().get(str(i))[5],
                              "  Delivery deadline:", get_hash_map().get(str(i))[6],
                              " Package weight:", get_hash_map().get(str(i))[7], "  Truck status:",
                              get_hash_map().get(str(i))[9], "  Delivery Status:",
                              get_hash_map().get(str(i))[10])
            except ValueError:
                print("Invalid entry")
                exit()
        elif initialize == "exit":
            exit()
        else:
            print("Invalid entry")
            exit()
