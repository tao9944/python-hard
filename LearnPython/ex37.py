# logical and
True and False == False

# with-as statement
import random as Y
print("The random number is", Y.randint(1, 5))

# assert something is true
X = True
assert X

# stop this loop
for x in range(1, 10):
    if x % 3 == 0:
        print("X equals:", x)
        break

# define a class
class cat:
    sound = "meow"

# don't process more of the loop continue
check = 0
while True:
    if check > 1:
        print("Would you like to stop?")
        break
    check += 1
    continue
    print("This will never run:(")

# define a function
def print_helper():
    message = input("What would you like to print? ")
    print(message)

#print_helper()

# delete from dictionary
fruits = {"1": "banana", "2": "apple", "3": "pear"}
del fruits["2"]
#print(fruits["2"])

# braching practice
name = "Pete"
if name == "John":
    print("Hi, John!")
elif name == "Sam":
    print("Hi, Sam!")
else:
    print("Hi,", name)
