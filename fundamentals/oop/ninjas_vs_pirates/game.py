from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

def startBattle(fighter1, fighter2):
    fighter2.show_stats()
    fighter1.show_stats()
    while(fighter1.health > 0 and fighter2.health > 0):
        fighter1.attack(fighter2)
        if fighter2.health <= 0:
            break
        fighter2.attack(fighter1)

startBattle(michelangelo, jack_sparrow)