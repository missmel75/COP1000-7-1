#AutoCountry Car Finder
#initialize vehicle list
allowed_vehicles = [
        'Ford F-150',
        'Chevrolet Silverado',
        'Tesla CyberTruck',
        'Toyota Tundra',
        'Nissan Titan',
        'Rivian R1T', 
        'Ram 1500'
    ]

#display menu
print("********************************")
print("AutoCountry Vehicle Finder v0.4")  
print("********************************")
print("Please Enter the following number below from the following menu:")
print(" ")
print("1. PRINT all Authorized Vehicles")
print("2. SEARCH for Authorized Vehicle")
print("3. ADD Authorized Vehicle")
print("4. DELETE Authorized Vehicle")  
print("5. Exit")  
print(" ")

#user input
running = True
while running:
    userChoice = input("Enter your choice: ")

    if userChoice == "1":
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        print(" ")
        for vehicle in allowed_vehicles:
            print(vehicle)
        print(" ")
        print("********************************")
        print("AutoCountry Vehicle Finder v0.4")  
        print("********************************")
        print("Please Enter the following number below from the following menu:")
        print(" ")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. DELETE Authorized Vehicle")  
        print("5. Exit")  
        print(" ")

    elif userChoice == "2":
        vehicle_name = input("Please Enter the full Vehicle name: ")
        if vehicle_name in allowed_vehicles:
            print(f"{vehicle_name} is an authorized vehicle")
        else:
            print(f"{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again")
        print(" ")
        print("********************************")
        print("AutoCountry Vehicle Finder v0.4")  
        print("********************************")
        print("Please Enter the following number below from the following menu:")
        print(" ")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. DELETE Authorized Vehicle")  
        print("5. Exit")  
        print(" ")

    elif userChoice == "3":
        new_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
        allowed_vehicles.append(new_vehicle)
        print(f'You have added "{new_vehicle}" as an authorized vehicle')
        print(" ")
        print("********************************")
        print("AutoCountry Vehicle Finder v0.4")  
        print("********************************")
        print("Please Enter the following number below from the following menu:")
        print(" ")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. DELETE Authorized Vehicle")  
        print("5. Exit")  
        print(" ")

    elif userChoice == "4":  
        vehicle_to_remove = input("Please Enter the full Vehicle name you would like to REMOVE: ")
        if vehicle_to_remove in allowed_vehicles:
            confirmation = input(f'Are you sure you want to remove "{vehicle_to_remove}" from the Authorized Vehicles List?\n')
            if confirmation.lower() == "yes":
                allowed_vehicles.remove(vehicle_to_remove)
                print(f'You have REMOVED "{vehicle_to_remove}" as an authorized vehicle')
            else:
                print(" ")  
        else:
            print(f'"{vehicle_to_remove}" was not found in the Authorized Vehicles List')
        print(" ")
        print("********************************")
        print("AutoCountry Vehicle Finder v0.4")
        print("********************************")
        print("Please Enter the following number below from the following menu:")
        print(" ")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. DELETE Authorized Vehicle")
        print("5. Exit")
        print(" ")

    elif userChoice == "5":  
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        print(" ")
        running = False