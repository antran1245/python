from classes.character import Character

class Ninja(Character):

    def __init__( self , name ):
        super().__init__(name, 10, 5, 100)

    def attack( self , pirate ):
        super().attack(pirate, 50)
        return self