'''
Based on this conditions:
=========================
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''

#Python statement 'if' Condition

print("This is 'if' statement")
if 5 > 2:
  print("Five is greater than two!")
print('')

# Python 'if else' Condition
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# Python 'elif' Condition
c = 33
d = 33
if d > c:
  print("d is greater than c")
elif c == d:
  print("c and d are equal")
else:
  print("c is greater than d")

# Python 'one line if' Condition
if 44 > 4: print("44 is greater than 4")

# Python 'one line if else' Condition
a = 2
b = 330
print("A") if a > b else print("B")

# Python 'one line nested if' Condition
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Python 'if condition with logical operators' Condition
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# Python 'if condition with logical operators' Condition
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Python 'if condition with logical operators' Condition
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


# Python 'if else with in if' Condition
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Python 'if with pass keyword' Condition
a = 33
b = 200

if b > a:
  pass