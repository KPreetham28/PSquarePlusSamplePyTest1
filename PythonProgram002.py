print("this is for variables and data types.")

#Variable declaration and assignment
kpt='Kompella Preetham Teja'
kmr='karre Balayya Mahesh Reddy'
print(kmr,'and',kpt,'are best friends.')
print('')
#calculation
length=8 
breath=7
area = 1/2 * length * breath;
print('Area is',area)
print('')
a = "28/08"
b = "/1998"
c = a + b
print('My dob is',c)
print('')

# Python Variable Names
# Valid
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
# Non Valid
'''
2myvar = "John"
my-var = "John"
my var = "John"
'''
# Python statement for assaigning multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Python statement for assaigning values to multiple variables
p = q = r = "Orange"
print(p)
print(q)
print(r)

# Python for Slicing the variable
b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])
b = "Hello, World!"
print(b[2:])
b = "Hello, World!"
print(b[-5:-2])


# Python for text conversion
a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.lower())
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!"
print(a.replace("H", "J"))
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Using format() method in Python
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Python Data types
'''
Text Type:		str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:		set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:		NoneType
'''

# Python statement for casting from one datatype to another datatype.
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

# Python the use of boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#false values
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

'''
NAMESPACE:
==========
	A namespace is a system that has a unique name for each and every object in Python. 
	An object might be a variable or a method. Python itself maintains a namespace in the form of a Python dictionary.

	Let’s go through an example, a directory-file system structure in computers. 
	Needless to say, that one can have multiple directories having a file with the same name inside every directory. 
	But one can get directed to the file, one wishes, just by specifying the absolute path to the file.

	Real-time example, the role of a namespace is like a surname. 
	One might not find a single “Alice” in the class there might be multiple “Alice” 
	but when you particularly ask for “Alice Lee” or “Alice Clark” (with a surname), 
	there will be only one (time being don’t think of both first name and surname are same for multiple students).

	On similar lines, the Python interpreter understands what exact method or variable one is trying to point to in the code, 
	depending upon the namespace. So, the division of the word itself gives a little more information. 
	Its Name (which means name, a unique identifier) + Space(which talks something related to scope). 
	Here, a name might be of any Python method or variable and 
	space depends upon the location from where is trying to access a variable or a method.

TYPES:
======
	When Python interpreter runs solely without any user-defined modules, methods, classes, etc. 
	Some functions like print(), id() are always present, these are built-in namespaces. 

	When a user creates a module, a global namespace gets created, 
	later the creation of local functions creates the local namespace. 

	The built-in namespace encompasses the global namespace and 
	the global namespace encompasses the local namespace.

	BUILT IN NAMESPACE(GLOBAL NAMESPACE(LOCAL NAMESPACE))

	The lifetime of a namespace :
 		A lifetime of a namespace depends upon the scope of objects, 
 		if the scope of an object ends, the lifetime of that namespace comes to an end. 
 		Hence, it is not possible to access the inner namespace’s objects from an outer namespace.

	Scope of Objects in Python :
 		Scope refers to the coding region from which a particular Python object is accessible. 
 		Hence one cannot access any particular object from anywhere from the code, 
 		the accessing has to be allowed by the scope of the object.

'''


# var1 is in the global namespace
var1 = 5
def some_func():
 
    # var2 is in the local namespace
    var2 = 6
    def some_inner_func():
 
        # var3 is in the nested local
        # namespace
        var3 = 7


# Python program processing
# global variable
count = 5
def some_method():
    global count
    count = count + 1
    print(count)
some_method()

# Python program showing
# a scope of object
 
def some_func():
    print("Inside some_func")
    def some_inner_func():
        var = 10
        print("Inside inner function, value of var:",var)
    some_inner_func()
#    print("Try printing var from outer function: ",var) 
# as var is defined inside the nested function outside that function we cannot access so there will be error 
# if we remove the coment above this comment. 
some_func()