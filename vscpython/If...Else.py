#------------------11 If ... Else------------------
#The if statement
a = 33
b = 200

if b > a:
    print("b is greater than a")
#Console => b is greater than a


#The elif statement
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
#Console => a and b are equal


#The else statement
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
#Console => a is greather than b


#Short hand if
a = 200
b = 33
if a > b: print("a is greater than b")
#Console => a is greater than b


#Short hand if ... else
a = 2
b = 330
print("A") if a > b else print("B")
#Console => B


#The 'and' keyword
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
#Console => Both conditions are True


#The 'or' keyword
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
#Console => At least one of the conditions is True