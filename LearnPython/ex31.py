print("""You enter a dark room with two doors/
Do you go through door #1, door #2 or door #3?""")

door = input(">")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif beaf == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("You travel through a wormhole and travel across the galaxy.")
    print("1. Sweet! I want to explore and boldly go.")
    print("2. What a rip! I wanted to finish the sixth castle of Super Mario.")
    print("3. Oh man! I'll never know if Ross and Rachel make it.")

    choices = input(">")

    if choices == "1" or choices == "3":
        print("Don't worry there's still television in this part of the galaxy.")
        print("Nice work!")
    else:
        print("I hope you're not out of hot pockets. You win!")
else:
    print("You stumble around and fall on a knife and die. Good job!")
