import random

class Character:
    
    all_character = []
    def __init__( self , name, strength, speed, health ):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health
        self.record = {"winCount" : 0, "loseCount": 0, "totalCount": 0}
        Character.all_character.append(self)
    
    @classmethod
    def show_record(cls):
        for character in cls.all_character:
            print(character.record)
            
    @staticmethod
    def flee():
        rand = random.randint(0, 100)
        return rand > 50
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
    
    def attack ( self , character, missChance ):
        hitChance = random.randint(0, 100)
        if hitChance > missChance:
            character.health -= self.strength
            print(f"{self.name} hit {character.name} with {self.strength}")
            print(f"{character.name} have {character.health} left")
        else:
            print(f"{self.name} miss {character.name}")    
        return self