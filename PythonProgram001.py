# simple python program statements
#Python printing function helps to print the characters in the console.
print('Hi, Hello world..! I am preetham and now onwards I will start python programming as my career.')
#this is also another print statement but look closely "the statement is inside the double quotes" and 
#'some statements in the single quotes' why? because you can see the reason in output
print("Statement1: I completed my btech in 2020 and Now presently 'I am working in TCS as System Software Engineer'")
# please check this one it is vice versa
print('Statement2: Because He said "It will come as needed in the output"')
print('As in the Statement1 output needed single quotes and in Statement2 the output needed double quotes.')
#Every print statement starts in new line and if you need line space use below statement
print('')
#You can directly calculate the values like this
print('The value of 8*3+4 =',8*3+4)
print("Please note that ',' is seperator so in the output we will have space in between")
print('')
#Here you will know the Concatenate Operators '+' and ','
print('a'+ ' b',8+3,'a','b')
print("Please note that '+' is adding the two strings so you don't find the space in between")
print('')
# Print statement for printing different lines in one go
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Typedef in print statement
print( '23 is',type(23) ) # int
print( '3.14 is',type(3.14) ) # float
print( '"hello" is',type("hello") ) # str
print( '"23" is',type("23") ) # str
print( '"3.24" is',type("3.24") ) # str
print( "'None' is",type(None) ) # NoneType
print( "'True' is",type(True) ) # bool
print( "'False' is",type(False) ) # bool
print( "'[]' is",type([]) ) # list
print( "'()' is",type(()) ) # tuple
print( "'{}' is",type({}) ) # dict

'''
escape characters please check
  https://www.w3schools.com/python/python_strings_escape.asp
string methods please check
  https://www.w3schools.com/python/python_strings_methods.asp
'''
print("Hello")
print('Hello')

a1 = "Hello"
print(a1)

a2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a2)

a3 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a3)

a4 = "Hello, World!"
print(a4[1])

b1 = "Hello, World!"
print(b1[2:5])

b2 = "Hello, World!"
print(b2[:5])

b3 = "Hello, World!"
print(b3[2:])

b4 = "Hello, World!"
print(b4[-5:-2])

a5 = "Hello, World!"
print(len(a5))

for x1 in "banana":
  print(x1)

txt1 = "The best things in life are free!"
print("free" in txt1)

txt2 = "The best things in life are free!"
print("expensive" not in txt2)

txt3 = "The best things in life are free!"
if "expensive" not in txt3:
  print("No, 'expensive' is NOT present.")

a6 = "Hello, World!"
print(a6.upper())

a7 = "Hello, World!"
print(a7.lower())

a8 = "Hello, World!"
print(a8.replace("H", "J"))

a9 = "Hello, World!"
print(a9.split(",")) # returns ['Hello', ' World!'

a10 = "Hello"
b10 = "World"
c10 = a10 + b10
print(c10)

a11 = "Hello"
b11 = "World"
c11 = a11 + " " + b11
print(c11)

age1 = 36
txt4 = "My name is John, and I am {}"
print(txt4.format(age1))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity1 = 3
itemno1 = 567
price1 = 49.95
myorder1 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder1.format(quantity1, itemno1, price1))

txt5 = "We are the so-called \"Vikings\" from the north."
print(txt5)


price81 = 49
txt81 = "The price is {} dollars"
print(txt81.format(price81))

txt82 = "The price is {:.2f} dollars"

quantity81 = 3
itemno81 = 567
price81 = 49
myorder81 = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder81.format(quantity81, itemno81, price81))

quantity91 = 3
itemno91 = 567
price91 = 49
myorder91 = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder91.format(quantity91, itemno91, price91))

age98 = 36
name98 = "John"
txt98 = "His name is {1}. {1} is {0} years old."
print(txt98.format(age98, name98))

myorder88 = "I have a {carname}, it is a {model}."
print(myorder88.format(carname = "Ford", model = "Mustang"))


'''
Keyword					Description
=======					===========
and						A logical operator
as						To create an alias
assert					For debugging
break					To break out of a loop
class					To define a class
continue				To continue to the next iteration of a loop
def						To define a function
del						To delete an object
elif					Used in conditional statements, same as else if
else					Used in conditional statements
except					Used with exceptions, what to do when an exception occurs
False					Boolean value, result of comparison operations
finally					Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for						To create a for loop
from					To import specific parts of a module
global					To declare a global variable
if						To make a conditional statement
import					To import a module
in						To check if a value is present in a list, tuple, etc.
is						To test if two variables are equal
lambda					To create an anonymous function
None					Represents a null value
nonlocal				To declare a non-local variable
not						A logical operator
or						A logical operator
pass					A null statement, a statement that will do nothing
raise					To raise an exception
return					To exit a function and return a value
True					Boolean value, result of comparison operations
try						To make a try...except statement
while					To create a while loop
with					Used to simplify exception handling
yield					To end a function, returns a generator

'''