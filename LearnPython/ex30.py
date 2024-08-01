people = 30
cars = 40
trucks = 15

# checks to see if cars are greater than people or trucks are
# greater than people and if true prints the message
if cars > people or trucks > people:
    print("We should not take the cars.")
# this will print when the if statement is false
else:
    print("We can't decide.")

# checks to see if trucks are greater than cars or trucks are
# greater than people and if true, prints the message
if trucks > cars or trucks == people:
    print("That's too many trucks.")
# checks to see if trucks are less than cars and if so, prints
# the message
elif trucks < cars:
    print("Maybe we could take the trucks.")
# this will print if the first two statements are false
else:
    print("We still can't decide.")

# checks to see if people are greater than trucks and cars are
# greater than trucks and if so, prints the message
if people > trucks and cars > trucks:
    print("Alright, let's just take the trucks.")
# this will print if the first statement is false
else:
    print("Fine, let's stay home then.")
