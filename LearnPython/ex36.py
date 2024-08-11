import random

def story():
    # welcome message - look up how to pause between prints
    print("After a long walk in the forest it's nearly sunset.")
    print("The path ahead splits, leading east or west.")
    print("An owl lands in a tree next to you an gracefully hoots to the moon.")

    # Where should this go?
    print("Which direction do you choose?")

def menu(room):
    print("Input a direction to move in that direction.")
    print("Input 1 to look around.")
    print("Input 2 to open something.")
    print("Input 3 to take an item.")
    print("Input 4 to view your inventory.")
    print("Input 5 to use and item.")
    choice = int(input("> "))
    # check to see if input is a number/handle non-number inputs
    action(choice, room)

def action(option, room):
    print(f"You are on the {room} and chose {option}")

def puzzle():
    print("A strange object appears and asks for your concentration.")
    puzzle_number = round(random() * 5, 0)
    if puzzle_number == 0:
        # display a number puzzle
        print("A clerk at the butcher shop is six feet tall and wears size 10 shoes. What does he weight?")
        choice = int(input("> "))
        if choice == "Meat" or choice == "meat":
            print("You are correct. How would you like to proceed?")
            points += 5
        else:
            print("Sorry that's not correct.")
    elif puzzle_number == 1:
        # display a word puzzle
        print("It's as light as a feather, but the strongest person can't hold it for five minutes. What is it?")
        choice = (input("> ")
        if choice == 'Breath' or choice == "breath":
            print("You are correct. How would you like to proceed?")
            points += 5
        else:
            print("Sorry that's not correct.")
    elif puzzle_number == 2:
        # display a logic puzzle
        print("Which is heavier, a pound of feathers or a pound of rocks?")
        choice = (input("> ")
        if choice == 'neither' or choice == "Neither":
            print("You are correct. How would you like to proceed?")
            points += 5
        else:
            print("Sorry that's not correct.")
    elif puzzle_number == 3:
        # display a number puzzle
        print("When Ashley was 15, her mother was 37. Now her mother is twice her age. How old is Ashley?")
        choice = int(input("> "))
        if choice == 22:
            print("You are correct. How would you like to proceed?")
            points += 5
        else:
            print("Sorry that's not correct.")
    elif puzzle_number == 4:
        # display a color puzzle

    else:
        # display a word puzzle
story()

# Should this be in the instructions?
print("As you enbark on this new quest, your goal is to find you way.")
print("Feel free to explore each place completely and discover your destiny.")
print("In each spot you may look around, open, check your bag, take and use items.")

menu("path")
