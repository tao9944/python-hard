i = 0
numbers = []
# create a function to replace the while loop below
def new_while_loop(stop, step):
    for i in range(0, stop, step):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

#while i < 6:
  #print(f"At the top i is {i}")
  #numbers.append(i)

  #i = i + 1
  #print("Numbers now: ", numbers)
  #print(f"At the bottom i is {i}")

new_while_loop(6, 2)

print("The numbers: ")

for num in numbers:
    print(num)
