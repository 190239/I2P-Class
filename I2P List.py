fruitList = ["apple","banana","orange","grape","tomato","strawberry","mango"]
print(fruitList[0])
print(fruitList[2-1])

##Calling the list and choosing the variables I want to summon
print(fruitList[2:5])
print(fruitList[1:7])
fruitList[1] = "Kiwi"
print(fruitList)

v_fruit = fruitList.pop()

print("")
print("")
##Creating a number list which I can use to perform different mathematical forms
numberList1 = [1,2,3]
print(numberList1 * 3)

print("")

##Creaing a list of values that have two parts, then choosing which part I want to summon
olympicList = [["London",2012],["Beijing",2008],["Athens",2004]]
print(olympicList)
print(olympicList[1])
print(olympicList[1][0])

print("")
##Inventory List which I can add and subtract items from
inventoryList = ["sword","armor","shield","healing potion"]
print(inventoryList)
inventoryList.append("cabbage")
print(inventoryList)

##Adding an item to a specific location
inventoryList.insert(3,"water bottle")
print(inventoryList)
##Randomizing the list (shuffling the order of the inventory)
inventoryList.sort()
print(inventoryList)

#Counting the amount of an object in the inventory
print(inventoryList.count("sword")

##Broken Code
##Merging the two lists above
##inventoryList.extend(fruitList)
##print(inventoryList)
##print(fruitList)

