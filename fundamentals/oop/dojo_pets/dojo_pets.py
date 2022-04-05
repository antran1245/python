import pet
class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f"{self.first_name} bathe {self.pet.name}.")
        self.pet.noise()
        return self

pet = pet.Dog("Apple", "rabbit", "cloning", 100, 40)
ninja = Ninja("Bob", "Keeper", "carrots", "carrot sticks", pet)
ninja.walk()
ninja.feed()
ninja.bathe()