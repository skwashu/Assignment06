class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
        
    def description(self):
        print(f"{self.name} is {self.age} years old.")
        
    def get_info(self):
        print(f"{self.name} has a {self.coat_color} coat.")
        
        
class JackRussellTerrier(Dog):
    def bark(self):
        print("Woof! Woof!")
        
    def hunt(self):
        print("I'm good at hunting rats.")
        
        
class Bulldog(Dog):
    def sleep(self):
        print("Zzzz... Zzzz...")
        
    def drool(self):
        print("I tend to drool a lot.")
# Create a Dog object and call its methods
my_dog = Dog("Buddy", 3, "black")
my_dog.description() # Output: Buddy is 3 years old.
my_dog.get_info() # Output: Buddy has a black coat.

# Create a JackRussellTerrier object and call its methods
my_jack = JackRussellTerrier("Jackie", 2, "white")
my_jack.description() # Output: Jackie is 2 years old.
my_jack.get_info() # Output: Jackie has a white coat.
my_jack.bark() # Output: Woof! Woof!
my_jack.hunt() # Output: I'm good at hunting rats.

# Create a Bulldog object and call its methods
my_bulldog = Bulldog("Tiger", 4, "brown")
my_bulldog.description() # Output: Benny is 4 years old.
my_bulldog.get_info() # Output: Benny has a brown coat.
my_bulldog.sleep() # Output: Zzzz... Zzzz...
my_bulldog.drool() # Output: I tend to drool a lot.
