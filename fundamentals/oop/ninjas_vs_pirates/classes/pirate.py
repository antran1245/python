from classes.character import Character

class Pirate(Character):

    def __init__( self , name ):
        super().__init__(name, 15, 3, 100)

    def attack ( self , ninja ):
        super().attack(ninja, 60)
        return self
    

