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

# exception handling
#try:
#    number = int(input("Give me a number: "))
#    print("Thank you!")
#except:
#    print("That wasn't a number.")

# run a string as python
exec('print("hello")')

# do this no matter what/try this block
try:
    number = int(input("Give me a number: "))
    print("Thank you!")
except:
    print("That wasn't a number.")
finally:
    print("The code has completed.")

# loop over a collection
sports = ['tennis', 'football', 'baseball']
print("The sports are: ")
for x in sports:
    print(x)

# import a function from a module
#import spell_check from custom

# declare a global variable
foo = 25
if True:
    print(f"The value of foo is {foo}")

# conditional branch
day = "Monday"
if day == "Monday":
    print("Back to work or school!")

# import module
import random

# part of for-loops
for x in range(3):
    print("The number is", x)

# anonymous function
x = lambda a, b, c : a + b + c
print("The total is",x(5,8,13))

# logical not
if not day == "Tuesday":
    print("It's another work day.")

# logical or
if day == 'Wednesday' or day == 'Monday':
    print("Exxxxceeellent!")

# empty block
def empty():
    pass

# print this
print("Print this string.")

# raise an exception
#raise ValueError("No")

# return this value from the function
def return_name():
    name = input("What's your name? ")
    return name
print("Hello,", return_name())

# start a while loop
while True:
    num = int(input("Please type the number 4: "))
    if num == 4:
        print("Thank you!")
        break

# True
0 == 0
True or False == True

# False
1 == 0
False and False == True

# None
y = None
if y == None:
    print("Y equals", y)

# Bytes
y = b"Goodbye!"
x = b"34"

# Strings
name = "Pete"
sport = "hockey"
weather = "It's going to be bright and sunny today."

# Numbers
y = 102232
x = 23
answer = 43

# Floats
y = 2.102
x = 14.982
length = 25.3492

# Lists
months = ["January","February", "March"]
sizes = [7,8,9,10,11]
to_do = ["do taxes","take test","go to movie"]

# Dicts
vocab = {1:'chide',2:'children',3:'Chicago'}
passwords = {'google':'password','usa today':'letmein','amazon':'primemember'}

# String escapes
print("""This is a test, 1//2 It\'s \"easy\" \a
\n\f\t when you learn the string escape ropes.\v \b""")

# operators
num = (1 + 3 - 2) * (6 - 2) / (1 + 2)
num2 = num // 4
num3 = num2 % 2
num4 = num3 ** 2
num += 5
num2 -= 1
num3 *= 4
num4 /= 2
