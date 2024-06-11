print("python functions.")

#function
def print_hello(kpt):
	print('Hello',kpt)
	print("")
print('')
print_hello("Kompella Preetham Teja")

# functions
def my_function():
  print("Hello from a function")

my_function()
#function1
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#function2
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#function3
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#function4
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#function5
def my_function(**kid):
    for i,j in kid.items():
      count=1
      for m in j:
        print(str(i) + " of " + str(count) + ": " + str(m))
        print()
        count += 1

my_function(fname = ["Tobias","preetham","hima","mahesh"], lname = ["Refsnes","kompella","vellamuri","karre balaya"])
#function6
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#function8
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
#function9
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
#function10
def myfunction():
  pass
#function11
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# Global Variables in python
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

d = "awesome"

def myfunc2():
  d = "fantastic"
  print("Python is " + d)

myfunc2()

print("Python is " + d)

def myfunc3():
  global f
  f = "fantastic"

myfunc3()

print("Python is " + f)
