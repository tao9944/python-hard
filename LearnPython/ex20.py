# import the argv module from sys
from sys import argv

# get the runtime options and put them into argv
script, input_file = argv

# define a funtion to print all of a file
def print_all(f):
    print(f.read())

# define a function to return to the beginning of a file
def rewind(f):
    f.seek(0)

# define a funtion to print a line from a file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# set the current file to the opened input file
current_file = open(input_file)

# print a message to the user
print("First let's print the whole file:\n")

# call the function with the current file
print_all(current_file)

# print a message to the user
print("Now let's rewind, kind of like a tape.")

#call the function to return to the top of the file
rewind(current_file)

# print a message to the user
print("Let's print three lines:")

# set the current line variable to 1
current_line = 1
# call the print a line function with the current line and file
print_a_line(current_line, current_file)

# update the current line variable to 2
current_line += 1
# call the print a line function with the current line and file
print_a_line(current_line, current_file)

# set the current line variable to 3
current_line += 1
# call the print a line function with the current line and file
print_a_line(current_line, current_file)
