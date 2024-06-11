# Looping Statements
# While loop
i = 1
while i < 6:
  print(i)
  i += 1
# While loop with break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# While loop with continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# While loop with else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
# For loop on lists
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# For loop on strings
for x in "banana":
  print(x)
# For loop 
#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#4
for x in range(6):
  print(x)
#5
for x in range(2, 6):
  print(x)
#6
for x in range(2, 30, 3):
  print(x)
#7
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#8
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#9
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#10
for x in [0, 1, 2]:
  pass

