# Add the argv package from the sys library
from sys import argv

# Assing the command line inputs to two variables
script, filename = argv

# Prompt the user for a filename to open/Already provided by the command line
txt = input("Type the filename to open: ")
# Open the file provided by the user
txt = open(filename)

# Display the filename provided by the user
print(f"Here's your file {filename}:")
# Display the file contents to the user
print(txt.read())
# Close the text file after displaying
txt.close()
