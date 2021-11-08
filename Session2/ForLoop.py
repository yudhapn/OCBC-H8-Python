#case 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("\n")
#case 2
for x in "banana":
  print(x)

print("\n")
#case 3
for x in fruits:
  print(x)
  if x == "banana":
    break

print("\n")
#case 4
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("\n")
#case 5
for x in range(6):
  print(x)

print("\n")
#case 6
for x in range(2, 6):
  print(x)

print("\n")
#case 7
for x in range(2, 30, 3):
  print(x)

print("\n")
#case 8
for x in range(6):
  print(x)
else:
  print("Finally finished!") 

print("\n")
#case 9
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

print("\n")
#case 10
for x in adj:
  for y in fruits:
    print(x, y)

print("\n")
#case 11
for x in [0, 1, 2]:
  pass