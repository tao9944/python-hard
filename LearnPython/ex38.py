ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!

# List examples
# 1 a player's inventory in a video game
player_Inventory = ["sword", "torch", "knife", "bread", "potion",
    "compass", "map", "shield", "meat"] 
# 2 the items in a person's to do List
# 3 the baseball cards in a collection
# 4 a mechanic's tools
# 5 an artist's paintings
# 6 the inventory of a small business
# 7 an investor's portfolio
# 8 a library's books
# 9 family recipes
# 10 vacation bucket list
