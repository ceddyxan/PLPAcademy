# Assignment 1: Design Your Own Class! 🏗️
class lecturer:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

my_lecturer1 = lecturer("Dr. Smith", 45, "Computer Science")
my_lecturer2 = lecturer("Prof. Johnson", 50, "Mathematics")
my_lecturer3 = lecturer("Dr. Brown", 40, "Physics")
print(my_lecturer1.name)
print(my_lecturer2.age)
print(my_lecturer3.subject)

# Inheritance
class tutor(lecturer):
    pass
my_tutor1 = tutor("Mr. Omondi", 35, "Chemistry")
my_tutor2 = tutor("Ms. Kamau", 30, "Biology")
my_tutor3 = tutor("Mr. Mutua", 28, "History")
my_tutor4 = tutor("Ms. Moraa", 32, "English")

for tutor in (my_tutor1, my_tutor2, my_tutor3, my_tutor4):
    print(tutor.name, tutor.age)
    
    
    
#Activity 2: Polymorphism Challenge! 🎭
class human:
    def move(self):
        return "Walk and Run"
class kangaroo:
    def move(self):
        return "Jump and Hop"
class horse:
    def move(self):
        return "Gallop and Run"
class dog:
    def move(self):
        return "Run and Bark"
class bird:
    def move(self):
        return "Fly and Sing"
class fish:
    def move(self):
        return "Swim and Splash"

for animal in (human(), kangaroo(), horse(), dog(), bird(), fish()):
    print(animal.move())