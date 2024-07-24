# Import the argv module from the sys library
from sys import argv
# Get the command line and store them in the variables
script, filename = argv

# Display the function of the project and ask for input from the user
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Get the user input
input("? ")

# Open the file name provided by the user in the command line
print("Opening the file...")
target = open(filename, 'w')

# Print a message to the user and ask for four lines to write in the file
print("Now I'm going to ask you for four lines for poem.")

# Ask for and save the lines the user inputs
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
line4 = input("line 4: ")

#Let the user know the writing to a fiel step
print("I'm going to write these to a file.")

# write the four lines to the file
target.write(f"{line1}\n{line2}\n{line3}\n{line4}\n")

# Let the user knwo that the file will be closed and close the file
print("And finally, we close it.")
target.close()
