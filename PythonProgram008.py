'''
Sets:
=====
Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, No Duplicates allowed and unindexed.

Unordered and unindexed:
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable:
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Duplicates:
Sets cannot have two items with the same value.

Type() : <class 'set'>
List are written with curly braces.
A set can contain different data types.

'''

# Simple set contains string values
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicate values will be ignored : Even any duplicates are in the set will be ignored and one instance will come in output.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# 1 and True are same and 0 and false are same.
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
thisset = {"apple", "banana", "cherry", 1, True, 2}
print(thisset)
thisset = {"apple", "banana", "cherry", False, 0, 2}
print(thisset)
thisset = {"apple", "banana", "cherry", 0, False, 2}
print(thisset)

# Length of the set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# different types of sets
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

# Set set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Set in for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Checking the value in Set (With 'in' keyword)
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Adding the value to the set (With 'add()' method)
# in this example orange will add to the end of the set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add sets through update() method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add Any Iterable means from either list or tuple
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove the iteam from the set
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# Clear() method
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# del() method
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# Union() method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# Update() method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# intersection_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# intersection()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# symmetric_difference() 1
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# symmetric_difference() 2
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)


'''
Dictionaries:
=============
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values.

Type() : <class 'dict'>

'''

# Simple Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Dictionary example 1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Dictionary example 2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2023
}
print(thisdict)
# length of the dictionary
print(len(thisdict))

# Dictionary example 3
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# dictionary type()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# Dict constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


# Acceessing the dictioinaries 1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#The value of the model key i.e., Mustang will move to x1 variable
x1 = thisdict["model"]

#The value of the model key i.e., Mustang will move to x2 variable using get() method
x2 = thisdict.get("model")

#The Keys are that dictionary will move to x3 variable
x3 = thisdict.keys()

#The Values are that dictionary will move to x4 variable
x4 = thisdict.values()

'''
print(x1, x2, x3, 'and', x4)
Mustang Mustang dict_keys(['brand', 'model', 'year']) and dict_values(['Ford', 'Mustang', 1964])

'''

#dictionaries example on adding the keys to the dictionaries
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#dictionaries example on adding the values to the dictionaries
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#dictionaries example on adding the iteams(values and keys) to the dictionaries
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


#dictionaries example 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


#dictionaries example 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#dictionaries example 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)

#dictionaries example on removing a key value pair from dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#dictionaries example on removing the last key value pair from dictionary
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#dictionaries example on removing a key value pair from dictionary
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

'''
Deleting the dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

'''

#dictionaries example on removing all the key value pairs from dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
  print(thisdict[x])

thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)

thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)


# Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

# Nested dictionaries 2
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

# Accessing the nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])


'''
Method        Description
clear()       Removes all the elements from the dictionary
copy()        Returns a copy of the dictionary
fromkeys()    Returns a dictionary with the specified keys and value
get()         Returns the value of the specified key
items()       Returns a list containing a tuple for each key value pair
keys()        Returns a list containing the dictionary's keys
pop()         Removes the element with the specified key
popitem()     Removes the last inserted key-value pair
setdefault()  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()      Updates the dictionary with the specified key-value pairs
values()      Returns a list of all the values in the dictionary
'''