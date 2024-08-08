def story():
    # welcome message - look up how to pause between prints
    print("After a long walk in the forest it's nearly sunset.")
    print("The path ahead splits, leading east or west.")
    print("An owl lands in a tree next to you an gracefully hoots to the moon.")

    # Where should this go?
    print("Which direction do you choose?")

def menu():
    print("Input a direction to move in that direction.")
    print("Input 1 to look around.")
    print("Input 2 to open something.")
    print("Input 3 to take an item.")
    print("Input 4 to view your inventory.")
    print("Input 5 to use and item.")
    choice = int(input("> "))
    # check to see if input is a number
    print(f"The user chose ", choice)
story()

# Should this be in the instructions?
print("As you enbark on this new quest, your goal is to find you way.")
print("Feel free to explore each place completely and discover your destiny.")
print("In each spot you may look around, open, check your bag, take and use items.")

menu()
