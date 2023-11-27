from classes.game import Game

from classes.mage import Mage
from classes.character import Character

def main():
    #warrior = Warrior("James")
    #mage = Mage("Coco")
    #
    #cars: list[Character] = [warrior, mage]
    #stats = {}
    #
    #char1 = random.choice(cars)
    #cars.remove(char1)
    #
    #char2 = random.choice(cars)
    #cars.remove(char2)
    #
    #print(char1)
    #print(char2)
    #
    #stats[char1.get_name()] = 0
    #stats[char2.get_name()] = 0
#
    #for i in range(100):
    #    print(f"--------------------")
    #    print(f"Round n°{i+1}")
    #    
    #    char1.regenerate()
    #    char2.regenerate()
    #    while char1.is_alive() and char2.is_alive():
    #        char1.attack(char2)
    #        char2.attack(char1)
    #    if (char1.is_alive()):
    #        stats[char1.get_name()] += 1
    #    else:
    #        stats[char2.get_name()] += 1
    #        
    #print(stats)
    
    game = Game()
    game.start_game()
       
def test():
    char1 = Mage.create_default_character("Michel")
    print(char1)
    print(char1.playerMove)
    char1.add_special()
    print(char1.playerMove)
       
if __name__ == "__main__":
    main()
    # test()