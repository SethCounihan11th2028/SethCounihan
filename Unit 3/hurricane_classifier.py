speed = int(input("What is the wind speed in miles per hour \n "))

if speed < 74:
    print("Tropical Storm.")
elif speed < 96:
    print("Category 1 Storm.")
elif speed < 111:
    print("category 2 Storm.")
elif speed < 130:
    print("Category 3 Storm.")
elif speed < 157:
    print("Category 5 Storm.")
elif speed >= 157:
    print("Category 5 Storm.")