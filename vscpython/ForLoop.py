#------------------13 For Loop------------------
#The for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#Console => apple
#           banana
#           cherry


#Loop through a string
for x in "banana":
    print(x)
#Console => b
#           a
#           n
#           a
#           n
#           a


#Using the break statement in a for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
#Console => apple
#           banana


#Using the continue statement in a for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
#Console => apple
#           cherry


#Using the range() function in a for loop
for x in range (6):
    print(x)
#Console => 0
#           1
#           2
#           3
#           4
#           5


#Else in for loop
for x in range (6):
    print(x)
else:
    print("Finally finished!")
#Console => 0
#           1
#           2
#           3
#           4
#           5
#           Finally finished!


#Nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
#Console => red apple
#           red banana
#           red cherry
#           big apple
#           big banana
#           big cherry
#           tasty apple
#           tasty banana
#           tasty cherry


