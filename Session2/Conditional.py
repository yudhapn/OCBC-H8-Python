a = 33
b = 200
if b > a: print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

print("A") if a > b else print("B") 


e = 200
f = 33
g = 500

if e > f and g > e:
  print("Both conditions are True")

if e > f or g > e:
  print("At least one of the conditions is True")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


a = 33
b = 200

if b > a:
  pass