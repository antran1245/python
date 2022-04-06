from classes.ninja import Ninja
from classes.pirate import Pirate
from classes.character import Character
import random

# Characters
michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")

# Fighting funtion
def startBattle(fighter1, fighter2):
    
    # Show the current record and the stats of each characters
    fighter1.record["totalCount"] +=1
    fighter2.record["totalCount"] +=1
    fighter2.show_stats()
    fighter1.show_stats()
    
    # character keep fighting till one health reach 0 or below
    while(fighter1.health > 0 and fighter2.health > 0):
        
        # Attack or flee attempt random
        rand = random.randint(1,100)
        if(rand > 20):    
            fighter1.attack(fighter2) #attack the other character
        else:
            # Invoke the flee function
            flee = fighter2.flee()
            print(f"{fighter2.name} attempting to flee")
            if(flee == "flee"):
                print(f"{fighter2.name} ran away")
                break
            else:
                print(f"{fighter2.name} failed to flee")
        
        # if the fighter2's health reach 0 after the fighter1's attack
        if fighter2.health <= 0:
            break
        if(rand > 20):    
            fighter2.attack(fighter1)
        else:
            flee = fighter1.flee()
            print(f"{fighter1.name} attempting to flee")
            if(flee == "flee"):
                print(f"{fighter1.name} ran away")
                break
            else:
                print(f"{fighter1.name} failed to flee")
    
    # Increment the record by 1
    if fighter1.health > 0:
        fighter1.record["winCount"] +=1
        fighter2.record["loseCount"] +=1
    else:
        fighter2.record["winCount"] +=1
        fighter1.record["loseCount"] +=1
    print(f"{fighter1.name}'s record {fighter1.record}")
    print(f"{fighter2.name}'s record {fighter2.record}")

for x in range(3):
    startBattle(michelangelo, jack_sparrow)

Character.show_record()