#------------------8 TUPLES------------------
#Create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Console => ('apple', 'banana', 'cherry')


#Access tuple items
thistupleOne = ("apple", "banana", "cherry")
print(thistupleOne[1])
#Console => banana


#Change tuple values
thistupleTwo = ("apple", "banana", "cherry")
thistupleTwo[1] = "blackcurrant"
#The value is still the same:
print(thistupleTwo)
#Console => ('apple', 'banana', 'cherry')


#Loop through a tuple
thistupleThree = ("apple", "banana", "cherry")
for x in thistupleThree:
    print(x)
#Console => apple
#           banana
#           cherry


#Check if a tuple item exists
thistupleFour = ("apple", "banana", "cherry")
if "apple" in thistupleFour:
    print("Yes, 'apple' is in the fruits tuple")
#Console => Yes, 'apple' is in the fruits tuple


#Get the length of a tuple
thistupleFive = ("apple", "banana", "cherry")
print(len(thistupleFive))
#Console => 3


#Delete a tuple
thistupleSix = ("apple", "banana", "cherry")
del thistupleSix
print(thistupleSix)
#This will raise an error because the tuple no longer exists
#Console => Traceback (most recent call last):
#               File "demo_tuple_del.py", line 3, in <module>
#                   print(thistupleSix)
#           NameError: name 'thistupleSix' is not defined


#Using the tuple() constructor to create a tuple
thistupleSeven = tuple(("apple", "banana", "cherry"))
print(thistupleSeven)
#Console => ('apple', 'banana', 'cherry')