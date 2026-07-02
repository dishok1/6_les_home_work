class Animal:
    """Class creat object Animal"""
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    
    def make_sound(self):
        if self.species.lower() == "cat":
            print(f"{self.name} says: Meow!")
        elif self.species.lower() == "dog":
            print(f"{self.name} says: Woof!")
        else:
            print(f"{self.name} makes an unknown sound.")

cat = Animal(name="Whiskers", species="cat", age=3)

dog = Animal(name="Buddy", species="dog", age=5)

cat.make_sound()
dog.make_sound()
