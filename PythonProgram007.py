'''
Tuples:
=======
Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered, unchangeable and allow duplicate values.

Ordered:
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable:
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Duplicate:
Since tuples are indexed, they can have items with the same value.

Type() : <class 'tuple'>
Tuples are written with round brackets.
A list can contain different data types.

'''

# Simple tuple with string values
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Simple tuple with duplicate string values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple length : To find the length of the tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Tuple with single value
# YES a tuple
thistuple = ("apple",)
print(type(thistuple))
'''
NOT a tuple
thistuple = ("apple")
print(type(thistuple))

'''

# Tuple values can have strings, Integers & Booleans and we can have the combined also.
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple1 = ("abc", 34, True, 40, "male")

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


# Tuple access can be made by index value with 
# positive number, Negetive, Range off, upto, Start with and with negetive indexes.
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Check if Item Exists with 'in' Keyword
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable.
# So there is work around on the same.
# Changing the values in the list
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Appending the values in tuple with help of List
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# Adding the tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# Removing the values in tuple with help of List
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

'''
If we delete the tuple and we can't call it back.

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

'''

# Tuple unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Second unpacking tuple example with artistick (*)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# Third unpacking tuple example with artistick (*)
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# Tuple in for loop 1
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Tuple in for loop 2
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Tuple in while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Joining the tuples to form another tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)


'''
List:
=====
List are used to store multiple items in a single variable.
List items are ordered, changeable, and allow duplicate values.

Ordered:
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
List items are indexed, the first item has index [0], the second item has index [1] etc.

Changable:
If you add new items to a list, the new items will be placed at the end of the list.
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Duplicate:
Since list are indexed, they can have items with the same value.

Type() : <class 'list'>
List are written with square brackets.
A list can contain different data types.

'''

# list example storing different string values
mylist = ["apple", "banana", "cherry"]
print(mylist)

# list length : To find the length of the list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# list type to find the type of the variable
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# List constructor : to create the list using the list() method.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# We can access the list in different ways as it is indexed;
# Index can be positive, negetive, start from -- end before, end before, start from and Negetive indexed
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#check if apple is present in the list through 'in' keyword
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Changing the list {To change the value of a specific item, refer to the index number:}
#In below example list[1] : banana will change to blackcrrant
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# changing two vlues in one time
#In below example list[1:3] : banana and cherry will change to blackcrrant and watermelon.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# changing one value to another two values
#In below example list[1:2] : banana will change to blackcrrant and watermelon.
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Same as above but not two values to one value
#In below example list[1:3] : banana and cherry will change to watermelon.
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#inserting the value in 2nd position
# Inserting a new value in 2nd position i.e., after banana 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# List Append function 
# Adding the value at the end of the list here orange will add after cherry
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend() combining the two list one after one
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Changing the list by extending the values at last
# adding the list to tuple and create extended list
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# List removing one values
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# List removing the values at last
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# List removing the values using del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# List removing the values using clear function
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# List with for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# List with while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# sorting the list of values in ascending order.
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# sorting the list of values in small to big order.
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# sorting the list of values in descending order.
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# sorting the list of values in big to small order.
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# copying the list from one to another list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# copying the list from one to another list
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# adding the list from one to another list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# copying the list from one to another list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

# copying the list from one to another list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

'''
Sorts methods and descriptions.
Method			Description
append()		Adds an element at the end of the list
clear()			Removes all the elements from the list
copy()			Returns a copy of the list
count()			Returns the number of elements with the specified value
extend()		Add the elements of a list (or any iterable), to the end of the current list
index()			Returns the index of the first element with the specified value
insert()		Adds an element at the specified position
pop()			  Removes the element at the specified position
remove()		Removes the item with the specified value
reverse()		Reverses the order of the list
sort()			Sorts the list
'''


'''
List examples using conditional statements

'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in fruits]
print(newlist)
newlist = [x.upper() for x in fruits]
print(newlist)
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
newlist = ['hello' for x in fruits]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)