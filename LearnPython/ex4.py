# Create a varible named cars and assign it 100
cars = 100
# Create a variable named space_in_a_car and assign it 4
space_in_a_car = 4.0
# Create a variable named drivers and assign it 30
drivers = 30
# Create a variable named passengers and assign it 90
passengers = 90
# Create a variable named cars_not_driven and assign it the value of
# cars minus drivers
cars_not_driven = cars - drivers
# Create a variable named cars_driven and assign it the number of drivers
cars_driven = drivers
# Create a variable named carpool_capacity and assign it the value of
# cars_driven times space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# Create a variable named average_passengers_per_car and assign it the number
# of passengers divided by the number of cars_not_driven
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
