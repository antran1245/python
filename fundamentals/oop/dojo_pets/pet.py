class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, typeOfPet, tricks, health, energy):
        self.name = name
        self.type = typeOfPet
        self.tricks = tricks
        self.health = health
        self.energy = energy
        
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        print(f"{self.name} went to sleep.")
        self.energy += 25
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        print(f"Feeding {self.name} carrots.")
        self.energy += 5
        self.health += 5
        return self
    # play() - increases the pet's health by 5
    def play(self):
        print(f"Play with {self.name}")
        self.health += 5
        return self
    # noise() - prints out the pet's sound
    def noise(self):
        print(f"{self.name} purrr")
        return self

# Sub-classes
class Rabbit(Pet):
    def __init__(self, name, typeOfPet, tricks, health, energy):
        super().__init__(name, typeOfPet, tricks, health, energy)
    
class Dog(Pet):
    def __init__(self, name, typeOfPet, tricks, health, energy):
        super().__init__(name, typeOfPet, tricks, health, energy)
    
    def noise(self):
        print(f"{self.name} woof")
        return self