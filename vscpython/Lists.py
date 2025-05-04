#------------------7 LISTS------------------
#Create a list  |   NameList = ["item", "item", "item"]
thislist = ["apple", "banana", "cherry"]
print(thislist)
#Console => ['apple', 'banana', 'cherry']


#Access list items  |   print(Nlist[0|1|2])
thislistTwo = ["apple", "banana", "cherry"]
print(thislistTwo[1])
#Console => banana


#Change the value of a list item    |   Nlist[0] = "newValue"
thislistThree = ["apple", "banana", "cherry"]
thislistThree[1] = "blackcurrant"
print(thislistThree)
#Console => ['apple', 'blackcurrant', 'cherry']


#Loop through a list    |   for x in Nlist print(x)
thislistFour = ["apple", "banana", "cherry"]
for x in thislistFour:
    print(x)
#Console => apple
#           banana
#           cherry


#Check if a list item exists    |   if "item" in Nlist
thislistFive = ["apple", "banana", "cherry"]
if "apple" in thislistFive:
    print("Yes, 'apple' is in the fruits list")
#Console => Yes, 'apple' is in the fruits list


#Get the length of a list   |   print(len(Nlist))
thislistSix = ["apple", "banana", "cherry"]
print(len(thislistSix))
#Console => 3


#Add an item to the end of a list   |   Nlist.append("item")
thislistSeven = ["apple", "banana", "cherry"]
thislistSeven.append("orange")
print(thislistSeven)
#Console => ['apple', 'banana', 'cherry', 'orange']


#Add an item at a specified index   |   Nlist.insert(1, "item")
thislistEight = ["apple", "banana", "cherry"]
thislistEight.insert(1, "orange")
print(thislistEight)
#Console => ['apple', 'orange', 'banana', 'cherry']


#Remove an item |   Nlist.remove("item")
thislistNine = ["apple", "banana", "cherry"]
thislistNine.remove("banana")
print(thislistNine)
#Console => ['apple', 'cherry']


#Remove the last item   |   Nlist.pop()
thislistTen = ["apple", "banana", "cherry"]
thislistTen.pop()
print(thislistTen)
#Console => ['apple', 'banana']


#Remove an item at a specified index    |   del Nlist[0|1|2]
thislistEleven = ["apple", "banana", "cherry"]
del thislistEleven[0]
print(thislistEleven)
#Console => ['banana', 'cherry']


#Empty a list   |   Nlist.clear()
thislistTwelve = ["apple", "banana", "cherry"]
thislistTwelve.clear()
print(thislistTwelve)


#Using the list() constructor to make a list    |   Nlist = list(("item", "item", "item"))
thislistThirteen = list(("apple", "banana", "cherry"))
print(thislistThirteen)

