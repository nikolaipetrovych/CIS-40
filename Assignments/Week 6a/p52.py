# p52.py
# Nikolai Petrovych
# 7/27/26
# Python 3.12.10
# Description:
'''Create a class Item which has:
- instance variables: itemName, itemCost
- class variable: numberItems (gets increased every time a new Item is created)
- a default constructor that allows the user to set itemName and itemCost
  (the default constructor sets itemName="apple", itemCost=2.49 if the user
  does not specify them)
- function to show() the item name and cost
- functions to get() and set() the item name and cost
Create a list named groceryBag to store the objects:
- Fill the list with several Item's such as eggs, milk, carrots, bread,
  apples, each with a different price.
- use Item.numberItems to show how many items you have created.
- use a loop to calculate and show the totalCost for all the items in the bag
HINT: See the Dog class example (class variable numberDogs, default
constructor arguments, show/get/set methods, list of objects, loop to total).'''


class Item:
    numberItems = 0  # set initial instance counter, class variable

    def __init__(self, itemName="apple", itemCost=2.49):  # constructor
        self.itemName = itemName
        self.itemCost = itemCost

        Item.numberItems += 1  # add an instance to the class variable

    def show(self):
        return f"Name = {self.itemName}; Cost = ${self.itemCost:.2f}"

    def getName(self):
        return self.itemName

    def getCost(self):
        return self.itemCost

    def setName(self, newName):
        self.itemName = newName

    def setCost(self, newCost):
        self.itemCost = newCost


# create and fill grocery bag
groceryBag = []
groceryBag.append(Item("eggs", 3.99))
groceryBag.append(Item("milk", 4.99))
groceryBag.append(Item("carrots", 1.99))
groceryBag.append(Item("bread", 2.50))
groceryBag.append(Item())

groceryBag[3].setCost(4.50)  # modify bread cost -> inflation

print(f"There are currently {Item.numberItems} items in the grocery bag.")

# calculate cost and display item by item entries
totalCost = 0
for item in groceryBag:
    totalCost += item.getCost()
    print(f"{item.show()} is in the bag.")
print(f"The total cost of the grocery bag is ${totalCost:.2f}")

'''

***PROGRAM OUTPUT***

Test Run:
There are currently 5 items in the grocery bag.
Name = eggs; Cost = $3.99 is in the bag.
Name = milk; Cost = $4.99 is in the bag.
Name = carrots; Cost = $1.99 is in the bag.
Name = bread; Cost = $4.50 is in the bag.
Name = apple; Cost = $2.49 is in the bag.
The total cost of the grocery bag is $17.96

'''
