#------------------12 While Loop------------------
#The while loop
i = 1
while i < 6:
    print(i)
    i += 1
#Console => 1
#           2
#           3
#           4
#           5


#Using the break statement in a while loop
i = 1
while i < 6:
    print(i)
    if (i == 3):
        break
    i += 1
#Console => 1
#           2
#           3


#Using the continue statement in a while loop
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
#Note that number 3 is missing in the result
#Console => 1
#           2
#           4
#           5
#           6