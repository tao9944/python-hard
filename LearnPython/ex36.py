import random

# A new varible to store the user's points
score = 0

def story():
    # welcome message - look up how to pause between prints
    print("After a long walk in the forest it's nearly sunset.")
    print("The path ahead splits, leading east or west.")
    print("An owl lands in a tree next to you and gracefully hoots to the moon.")

def menu(room):
    while True:
        print("Which direction do you choose?")
        choice = input("> ")
        if choice == "east" or choice == "west":
            return choice
            break

def puzzle(points):
    print("A strange object appears and asks for your concentration.")
    puzzle_number = random.randrange(0, 4, 1)
    if puzzle_number == 0:
        # display a number puzzle
        print("A clerk at the butcher shop is six feet tall and wears size 10 shoes. What does he weight?")
        choice = input("> ")
        if "meat" in choice.lower():
            print("You are correct.")
            points += 5
            return points
        else:
            print("Sorry that's not correct.")
            return points
    elif puzzle_number == 1:
        # display a word puzzle
        print("It's as light as a feather, but the strongest person can't hold it for five minutes. What is it?")
        choice = input("> ")
        if "breath" in choice.lower():
            print("You are correct. Good stuff:)")
            points += 5
            return points
        else:
            print("Sorry that's not correct.")
            return points
    elif puzzle_number == 2:
        # display a logic puzzle
        print("Which is heavier, a pound of feathers or a pound of rocks?")
        choice = input("> ")
        if "neither" in choice.lower():
            print("You are correct. Good guess?")
            points += 5
            return points
        else:
            print("Sorry that's not correct.")
            return points
    elif puzzle_number == 3:
        # display a number puzzle
        print("When Ashley was 15, her mother was 37. Now her mother is twice her age. How old is Ashley?")
        choice = int(input("> "))
        if choice == 22:
            print("You are correct.")
            points += 5
            return points
        else:
            print("Sorry that's not correct.")
            return points
    else:
        # display a word puzzle
        print("A farmer has 19 sheep on his land. One day a big storm hits and all but seven run away.")
        print("How many sheep does the farmer have left?")
        choice = input("> ")
        if choice.lower() == 'seven' or choice.lower() == '7':
            print("You are correct. Nice!")
            points += 5
            return points
        else:
            print("Sorry that's not correct.")
            return points

story()
rooms = ["path", "house", "cellar", "cemetary", "forest", "mountain", "cave", "summit"]
# Should this be in the instructions?
#print("As you enbark on this new quest, your goal is to find you way.")
#print("Feel free to explore each place completely and discover your destiny.")
#print("In each spot you may look around, open, check your bag, take and use items.")
location = "path"
choice = menu(location)

# Check for movement east or west and change rooms
if choice == "east":
    # Player has moved to the house
    location = "house"
    # house description and puzzle
    print("You find yourself in front of an old mansion that has seen better days. The roof was once solid with integrity.")
    score += puzzle(score)
    print("To the east lies the cellar, to the west lies the cemetary.")
    menu(location)
    if choice == "east":
        location = "cellar"
        print("You find yourself in a damp and dark cellar. You can faintly see the webs of spiders long ago.")
        score += puzzle(score)
    else:
        location = "cemetary"
        print("You find yourself in a small and overgrown family cemetary. A small eddy forms to your right.")
        score += puzzle(score)
else:
    # Player has moved to the mountain
    location = "mountain"
    # mouintain description and puzzle
    print("You find yourself in front of a large rugged mountain. A cool breeze begins to blow.")
    score += puzzle(score)
    print("To the east lies the cave, to the west lies the summit.")
    menu(location)
    if choice == "east":
        location = "cave"
        print("You find yourself in an underground cave of echoes. The sleeping bats are your only companions.")
        score += puzzle(score)
    else:
        location = "summit"
        print("You find yourself on the top of the mountain and can see for miles in every direction.")
        score += puzzle(score)

if score > 20:
    print(f"You have {score}. Nice job, you win!")
elif score > 10:
    print(f"You have {score}. Not bad, I hope you had fun.")
else:
    print(f"You have {score}. Ehh, try again?")
