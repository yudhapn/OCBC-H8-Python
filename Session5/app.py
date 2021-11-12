from dog import *

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)
jack = Dog("Jack", 3)
jim = Dog("Jim", 5)

print(miles)
print(miles.speak("Woof Woof"))
print(buddy.speak("Yap"))

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(jack)
print(miles.speak())
print(miles.speak("Grrr"))

miles = JackRussellTerrier("Miles", 4)
print(type(miles) is Dog)
print(isinstance(miles, Dog))
