#case 1
i = 1
while i < 6:
  print(i)
  i += 1

print("\n")
#case 2
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 

print("\n")
#case 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print("\n")
#case 4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")