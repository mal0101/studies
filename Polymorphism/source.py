# Polymorphism vs Inheritance
# L'héritage est une relation entre deux classes qui permet à 
# une classe enfant d'hériter des attributs et des méthodes de la classe parent.
# Le polymorphisme est un concept qui permet à une classe de changer le comportement
# d'une méthode fournie par une classe parent. Il permet à une méthode existente dans d'autres classes
# de se comporter différemment en fonction de la classe qui l'appelle.

# Purpose of Polymorphism
# Cela permet à une classe de modifier le comportement d'une méthode fournie par une classe parent.

# Example of Polymorphism
# Dans cet exemple, nous avons une classe Animal avec une méthode make_sound().

class Animal:
    def make_sound(self):
        pass  # Placeholder method

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Outputs: Woof!
animal_sound(cat)  # Outputs: Meow!
