#------------------5 STRINGS------------------
#Get the character at position 1 of a string
a = "Hello, world!"
print(a[1])
#Console => e


#Substring. Get the characters from position 2 to position 5 (not included)
b = "Hello, world!"
print(b[2:5])
#Console => llo


#Remove whitespace from the beginning or at the end of a string
a =" Hello, world! "
print(a.strip())
#Console => Hello, world!


#Return the length of a string
a = "Hello, world!"
print(len(a))
#Console => 13


#Convert a string to lower case
a = "Hello, World!"
print(a.lower())
#Console => hello, world!


#Convert a string to upper case
a = "Hello, World!"
print(a.upper())
#Console => HELLO, WORLD!


#Replace a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))
#Console => Jello, World!


#Split a string into substrings / Array = Lista
a = "Hello, World!"
b = a.split(",")
print(b)
#Console => ['Hello', 'World!']

print(a.find("Hello")) #Extra: devuelve la posición donde comienza la palabra / índice caracter