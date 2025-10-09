class Cow:
    def sound(self):
        return "Moo"

class Cat:
    def sound(self):
        return "Meow"

def animal_sound(animal):
    print(animal.sound())

cow = Cow()
cat = Cat()

animal_sound(cow)  
animal_sound(cat)  
