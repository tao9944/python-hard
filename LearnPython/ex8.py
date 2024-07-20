# Create a variable with the string provided
formatter = "{} {} {} {}"

# Print the variable with the four string values that follow
print(formatter.format(1, 2, 3, 4))
# Print the variable with the four string values that follow
print(formatter.format("one", "two", "three", "four"))
# Print the variable with the four string values that follow
print(formatter.format(True, False, True, False))
# Print the variable with the four more string variables for each value
print(formatter.format(formatter, formatter, formatter, formatter))
# Print the variable with the four strings that follow
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
