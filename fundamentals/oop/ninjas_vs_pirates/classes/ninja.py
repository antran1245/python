from classes.character import Character

class Ninja(Character):

    def __init__( self , name, strength = 10, speed = 5, health = 100  ):
        super().__init__(name, strength, speed, health)

    def attack( self , pirate ):
        super().attack(pirate, 50)
        return self