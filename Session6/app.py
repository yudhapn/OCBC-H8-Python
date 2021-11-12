def my_generator():
  print("Inside my generator")
  yield 'a'
  yield True
  yield 100

x = my_generator()
# print(my_generator())

# for char in my_generator():
#   print(char)


print(next(x))
# y = my_generator()
# print(next(y))


# First-Class Objects
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello))
print(greet_bob(be_awesome))

# Inner Functions
print('\n=== Inner Functions ===')
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

parent()

# Returning Functions From Functions
print('\n=== Returning Functions From Functions ===')
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
        # return first_child()
    else:
        return second_child
        # return second_child()

first = parent(1)
# print(first)
print(first())

# Decorators
print('\n=== Decorators ===')
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

lol = my_decorator(say_whee)
# say_whee = my_decorator(say_whee)

lol()