from classes.character import Character

class Pirate(Character):

    def __init__( self , name, strength = 15, speed = 3, health = 100 ):
        super().__init__(name, strength, speed, health)

    def attack ( self , ninja ):
        super().attack(ninja, 60)
        return self
    

