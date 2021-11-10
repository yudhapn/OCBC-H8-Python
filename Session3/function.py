# case 1
def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)

def printme(str_input):
    print(str_input)

printme("I'm first call to user defined function")
printme("Again second call to do the same function")

print("\n===processing input and return it===")
def changeme(myList):
    myList = myList+[1,2,3,4]
    print("\nValues inside the function: ",myList)
    return myList

myList = [10,20,30]
print("\nValues outside the function - before : ", myList)
myList = changeme( myList )
print("\nValues outside the function - after  : ", myList)

# Required arguments
print("\n===Required arguments===")
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)
 
# Now you can call printme function
printme("Hello")

# # This syntax will give you an error
# printme()

# argument order is important!
def personalInfoData(name, age):
    print("name:", name)
    print("age:", age)

personalInfoData("yudha", 24)
# wrong
personalInfoData(24, "yudha")
# Keyword Arguments
print("\n===Keyword Arguments===")
personalInfoData(age = 24,  name = "yudha")


# Default Arguments
print("\n===Default Arguments===")
def printinfo( name, age = 24 ):
   print("Name : ", name)
   print("Age  : ", age)
   print("")

# Now you can call printinfo function
printinfo( age=18, name="yudha" )


print("\n===Variable-length Arguments (Tuples)===")
def printinfo( arg1, *vartuple ):
   print('arg1     : ', arg1)
   print('vartuple : ', vartuple)
   print('')
   
   for var in vartuple:
      print('isi vartuple : ', var) 

printinfo( 10 )
printinfo( 70, 60, 50, "a" )

print("\n===Variable-length Arguments (Dictionary)===")
def person_car(total_data, **kwargs):
  '''Create a function to print who owns what car'''
  print('Total Data : ', total_data)
  print("kwargs:", kwargs)
  for key, value in kwargs.items():
    print('Person : ', key)
    print('Car    : ', value)
    print('')

person_car(3, jimmy='chevrolet', frank='ford', tina='honda')
person_car(3)
# person_car(3, {"jimmy":'chevrolet', "frank":'ford', "tina":'honda'})


sum = lambda arg1, arg2: arg1 + arg2

# That lambda function will be equal to :
# def sum(arg1, arg2):
#     return arg1+arg2

def calculate(sum):
    print(sum)
# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))
calculate(sum( 10, 20 ))